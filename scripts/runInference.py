
import fire
from transformers import pipeline, AutoTokenizer, AutoConfig
import random
from human_eval_infilling.data import write_jsonl, read_problems
import time
from vllm import LLM, SamplingParams
from tqdm.auto import tqdm
from huggingface_hub import login
import os
import json
from torch.utils.data import Dataset
import statistics
import torch

def  generate_batch_completionVLLM(llm,  batch, sampling_params):

    prompts = [element["prompt"] for element in batch]

    keys = {}

    for element in batch:
        keys[element["prompt"]] = element["task_id"]

    outputs = llm.generate(
        #prompt_token_ids=[tokens.tolist() for tokens in batch],
        prompts=prompts,
        use_tqdm=False,
        sampling_params=sampling_params
    )
    generated_textAll = []
    for output in outputs:
        prompt_token_ids  = output.prompt_token_ids
        prompt = output.prompt
        keyOfPrompt = keys[prompt]
        generated_text = output.outputs[0].text
        token_ids = output.outputs[0].token_ids
        generated_textAll.append({"problem":keyOfPrompt, "prompt": prompt,  "generated_text":generated_text, "nr_token_ids": len(token_ids), "nr_prompt_token_ids": len(prompt_token_ids), "tokens_ids":output.outputs[0].token_ids})

    return generated_textAll

class MyDataset(Dataset):

    def __init__(self, list):
        self.list  = list
    def __len__(self):
        return len(self.list)

    def __getitem__(self, i):
        return self.list[i]

class CustomException(Exception):
    def __init__(self, data, e):
        self.data = data
        self.oe = e

def runAutoHG(tokenizer, text_generator, setOfProblems = [], max_length = 100, batchidentifier = "All", batch_size = None):
    mapsPromptTaskId, prompts = fromProblemsToPrompts(setOfProblems)

    if batch_size == None:
        batch_size = len(prompts)

    token_ids_all = [tokenizer.encode(prompt, add_special_tokens=False) for prompt in prompts]

    sizePrompts = [len(xp) for xp in token_ids_all]
    longest_prompt = max(sizePrompts)
    tinit = time.time()
    generatedCode = []
    times = []
    print("longest_prompt {} ,  max_length  {} ".format(longest_prompt, max_length))
    try:
        im = 0
        tcurrent = time.time()
        for solution in tqdm(text_generator(MyDataset(prompts), batch_size=batch_size, do_sample=False, max_new_tokens=max_length,
                                          num_return_sequences=1, return_full_text=False, output_scores=True,
                                          max_length=longest_prompt + max_length), total=len(prompts)):
            #print(f"i {im} b {solution}" )
            print(f" i {im} ", end="")
            generatedCode.append(solution)
            im+=1
            times.append(time.time() - tcurrent)
            tcurrent=time.time()

    except Exception as e:
         print("OMM Detected ", str(e))
         generated_textAll = []
         for  aPrompt, prompt_token_ids in zip( prompts, token_ids_all):
                 generated_textAll.append({"problem": mapsPromptTaskId[aPrompt], "nr_prompt_token_ids": len(prompt_token_ids)})

         raise CustomException(generated_textAll, e)

    print(f"batch_identifier {batchidentifier} - time  batch: {(time.time() - tinit)} \n")

    return createSolutionFromGeneratedCode(generatedCode, mapsPromptTaskId, prompts, tokenizer, times, token_ids_all)


def fromProblemsToPrompts(batch):
    prompts = [element["prompt"] for element in batch]
    mapsPromptTaskId = {}
    for element in batch:
        mapsPromptTaskId[element["prompt"]] = element["task_id"]
    return mapsPromptTaskId, prompts


def createSolutionFromGeneratedCode(generatedCode, mapsPromptTaskId, prompts, tokenizer, times, token_ids_all):
    generated_textAll = []
    for generated, aPrompt, prompt_token_ids, aTime in zip(generatedCode, prompts, token_ids_all, times):
        for gt in generated:
            generated_text = gt["generated_text"]
            # Convert the generated text back to token IDs
            token_ids = tokenizer.encode(generated_text, add_special_tokens=False)
            generated_textAll.append(
                {"problem": mapsPromptTaskId[aPrompt], "prompt": aPrompt, "generated_text": generated_text,
                 "nr_token_ids": len(token_ids),
                 "nr_prompt_token_ids": len(prompt_token_ids), "tokens_ids": token_ids, "time": aTime})
    return generated_textAll


def getvLLMConfig(enginevLLM):
    try:
        d = {"model": "%r"%enginevLLM.model_config.model,
                "tokenizer": "%r"%enginevLLM.model_config.tokenizer,
                "tokenizer_mode": "%s"%enginevLLM.model_config.tokenizer_mode,
                "revision": "%s"%enginevLLM.model_config.revision,
                "tokenizer_revision": "%s"%enginevLLM.model_config.tokenizer_revision,
                "dtype": "%s"%enginevLLM.model_config.dtype,
                #"max_seq_len": enginevLLM.model_config.max_seq_len,
                "load_format": "%s"%enginevLLM.model_config.load_format,
                "quantization": "%s"%enginevLLM.model_config.quantization,
                "device_config": "%s"%enginevLLM.device_config.device,
                "seed": "%s"%enginevLLM.model_config.seed,
                "enforce_eager": "%s"%enginevLLM.model_config.enforce_eager,
                "tensor_parallel_size":"%d"%enginevLLM.parallel_config.tensor_parallel_size,
                }
        print("Plain Config vLLM {}".format(d))
        return d
    except Exception as e:
        print("Error when getting the config {}".format(e))
        return None

def main(model:str="codellama/CodeLlama-7b-hf",
         world_size:int=2,
         gpu_memory_utilization:int=0.85,
         repetitions:int = 1,
         benchmark_name:str="single-line",
         allBatchSizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1028],
         allMaxtokensout = [5,10, 20],
         out = "./outResult",
         typeInference:str = None,
         inputSort:str = "natural",
         precision="auto",
         randomSeed = 0
         ):
    llm = None
    ## for autohf
    text_generator  = None
    tokenizer = None
    creationTime = None
    ### Confuguration the model
    hf_dev_map = None
    configLLM = None

    for batch_size in allBatchSizes:
        for maxtokensout in allMaxtokensout:

            print(f"batch_size {batch_size} maxtokensout {maxtokensout}")
            key = "" ### PUT your HF here
            login(key)
            print("\n----------\nSTART model {} precision {} world_size {} gpu_memory_utilization {}, repetitions {},    benchmark_name {} maxtokensout {} batch_size {}  out {} vLLM {} inputSort {}".format(model,
                precision, world_size,
               gpu_memory_utilization,
                repetitions,
                benchmark_name,
                 maxtokensout,
                 batch_size,
                 out, typeInference,inputSort))


            initTime = time.perf_counter()

            modelId = model.replace("/", "_")

            experimentId = "ws_{}_bs_{}_mg_{}".format(world_size,batch_size,  maxtokensout)

            vLLMConfig = None

            outDir = os.path.join(out, inputSort, typeInference, modelId, experimentId)
            if not os.path.exists(outDir):
                os.makedirs(outDir, exist_ok=True)
                print("Created {}".format(outDir))
            else:
                if len(os.listdir(outDir))>1 and os.path.exists('{}/perBatch_{}.json'.format(outDir,experimentId)):
                    print("Skip: Already analyzed {} {}".format(outDir,os.listdir(outDir)))
                    ## We continue because we already analyzed this experiment
                    continue
                else:
                    print("To Analyze because dir is empty  {} {}".format(outDir,os.listdir(outDir) ))

            print("Experiment to be saved in {}".format(outDir))


            initCreationTime = time.perf_counter()

            if typeInference.lower() == "vllm":
                if llm is None:
                    print("Init model:")
                    llm = LLM(
                        model=model,
                        tokenizer=model,
                         tensor_parallel_size=world_size,
                         gpu_memory_utilization=gpu_memory_utilization,
                        dtype=precision,
                        trust_remote_code=True
                    )
                    enginevLLM = llm.llm_engine
                    vLLMConfig = getvLLMConfig(enginevLLM)

                    if configLLM is not None:
                        with open('{}/llm_config.txt'.format(outDir), 'w', encoding='utf-8') as f:
                            f.write(str(configLLM))
                            f.close()
                        print("config vLLM {}".format(configLLM))

                else:
                    print("Reusing loaded model")
            elif typeInference.lower() == "autohf" or typeInference.lower() == "accelerate" or   typeInference.lower()  == "partialstate":
                if tokenizer is None or text_generator is None :
                    print("Init tokenizer and model")

                    tokenizer = AutoTokenizer.from_pretrained(model, trust_remote_code=True)

                    if model == "microsoft/phi-1_5":
                        deviceMapMode = "cuda"
                        text_generator = pipeline(model=model, device_map="cuda",  torch_dtype=precision,
                                                  pad_token_id=tokenizer.eos_token_id, trust_remote_code=True)

                    else:
                        deviceMapMode = "auto"
                        try:
                            text_generator = pipeline(model=model, return_dict=True, device_map="auto", torch_dtype=precision,
                                                      pad_token_id=tokenizer.eos_token_id, trust_remote_code=True)
                        except:
                            print("Catching error")
                            with open("{}/error.txt".format(outDir), "w") as f:
                                f.write("{}\n".format("Error catched when loading the model"))
                                f.close()


                            continue

                    text_generator.tokenizer.pad_token_id = tokenizer.eos_token_id
                    configLLM = AutoConfig.from_pretrained(model, trust_remote_code=True)

                    if deviceMapMode == "auto":
                        hf_dev_map = text_generator.model.hf_device_map

                else:
                    print("Reusing loaded tokenizer and models")

            else:
                print("Error: Option not recognized {}".format(typeInference))
                return

            endCreationTime = time.perf_counter()

            if creationTime is None:
                creationTime = endCreationTime-initCreationTime

            print("Loading time {}".format(endCreationTime-initCreationTime))
            with open("{}/time_loading_llm{}.txt".format(outDir, experimentId), "w") as f:
                f.write("{}\n".format(creationTime))
                f.close()
            problemsOriginal = read_problems(benchmark_name=benchmark_name)
            problems = []
            for p in problemsOriginal:
                problems.append(problemsOriginal[p])


            print("hf_dev_map {}".format(hf_dev_map))
            if hf_dev_map is not None:
                with open('{}/hf_dev_map.json'.format(outDir), 'w', encoding='utf-8') as f:
                    json.dump(hf_dev_map, f, ensure_ascii=False, indent=4)
                    f.close()
            if vLLMConfig is not None:
                with open('{}/vLLM_config.txt'.format(outDir), 'w', encoding='utf-8') as f:
                    json.dump(vLLMConfig, f, ensure_ascii=False, indent=4)
                    f.close()
                print("config {}".format(vLLMConfig))

            samples = []
            nrBatch = 0
            withErrors = []
            times = []
            promptsizesTokens = []

            print("total problems: {}".format(len(problems)))

            if inputSort.lower() == "random":
                print("Random shuffle the problems")
                random.seed(randomSeed)
                random.shuffle(problems)
            elif inputSort.lower() == "inputsizeinc":
                problems = sorted(problems, key=lambda x: len(x["prompt"]),reverse=False)
            elif inputSort.lower() == "natural":
                print("Problems sorted as given -by id-")

            batches = [problems[i:i + batch_size] for i in range(0, len(problems), batch_size)]
            print("Number of batches {}".format(len(batches)))
            rawResults = []
            rawBatchResults = []

            fPartialResults =  open('{}/temp_perBatch_{}.json'.format(outDir, experimentId), 'w', encoding='utf-8')

            startInference = time.perf_counter()
            thougputs = []
            print("Total batches {}:".format(len(problems)), end='')


            start_time = time.time()

            for batch in batches:

                bid = f"b{nrBatch}"

                try:
                    start = time.perf_counter()
                    if typeInference.lower() == "vllm":
                        resultsCompletion = generate_batch_completionVLLM(llm, batch=batch, sampling_params=SamplingParams(max_tokens=maxtokensout,ignore_eos=True))
                    elif typeInference.lower() == "autohf":
                        torch.cuda.empty_cache()
                        resultsCompletion = runAutoHG(tokenizer, text_generator, setOfProblems=batch, max_length = maxtokensout, batchidentifier=nrBatch)
                    else:
                        print("Error: Option not recognized {}".format(typeInference))
                        return

                    batchtime = time.perf_counter() - start
                    times.append(batchtime)
                    dataRow = {"batchId": nrBatch, "time": batchtime,"result":resultsCompletion }
                    rawBatchResults.append(dataRow)
                    fPartialResults.write(json.dumps(dataRow) + ",\n")
                    fPartialResults.flush()
                    computeOutVar(batchtime, promptsizesTokens, rawResults, resultsCompletion, samples, thougputs)


                except RuntimeError as e:

                    if "out of memory" in str(e):
                        print("Catched Error: out of memory")
                        torch.cuda.empty_cache()

                    ####  New: if we find an error, we stop, no need of continuing.
                    with open("{}/breaking_{}.txt".format(outDir, experimentId), "w") as f:
                        f.write("{" + ( "batch: {}, totalB: {},  time: {}, status='error', message='{}'".format(nrBatch, len(batches),
                                                                                      time.time() - start_time, str(e))) + "}\n")
                        f.close()
                    print("EARLY STOP Due to error at Batch {}".format(nrBatch))
                    break

                except Exception as e:
                    print(f"Exception detected!: {e.oe}")
                    dataRow = {"batchId": nrBatch, "status": "error", "message": str(e.oe), "time": None, "result": e.data}
                    rawBatchResults.append(dataRow)
                    withErrors.append({"batchid": nrBatch, "error": str(e.oe)})
                    fPartialResults.write(json.dumps(dataRow)+ ",\n")
                    fPartialResults.flush()

                    ####  New: if we find an error, we stop, no need of continuing.
                    with open("{}/breaking_{}.txt".format(outDir, experimentId), "w") as f:
                        f.write("{" + ("batch: {}, totalB: {},  time: {}, status='error'".format(nrBatch, len(batches),
                                                                                 time.time() - start_time)) + "}\n")
                        f.close()
                    print("EARLY STOP Due to error at Batch {}".format(nrBatch))
                    break


                finally:
                    pass

                nrBatch+=1


            print("\nWith errors {}".format(len(withErrors)))
            endInference = time.perf_counter()
            os.system("pkill -9 nvidia;")
            print(f"loading time {creationTime} inference {endInference - startInference}")
            print(f"Total Time {time.perf_counter() - initTime}")
            print("Loading time {}".format(creationTime))

            with open('{}/errors.json'.format(outDir), 'w', encoding='utf-8') as f:
                json.dump(withErrors, f, ensure_ascii=False, indent=4)
                f.close()

            with open("{}/time_total_inference{}.txt".format(outDir, experimentId), "w") as f:
                f.write("{}\n".format(endInference-startInference))
                f.close()

            write_jsonl("{}/samples_{}.jsonl".format(outDir,experimentId), samples)

            with open('{}/alldata_{}.json'.format(outDir,experimentId), 'w', encoding='utf-8') as f:
                json.dump(rawResults, f, ensure_ascii=False, indent=4)
                f.close()

            with open('{}/tp_{}.json'.format(outDir,experimentId), 'w', encoding='utf-8') as f:
                json.dump(thougputs, f, ensure_ascii=False, indent=4)
                f.close()

            with open('{}/perBatch_{}.json'.format(outDir,experimentId), 'w', encoding='utf-8') as f:
                json.dump(rawBatchResults, f, ensure_ascii=False, indent=4)
                f.close()

            fPartialResults.close()
            with open('{}/time_batches_{}.json'.format(outDir,experimentId), 'w', encoding='utf-8') as f:
                json.dump(times, f, ensure_ascii=False, indent=4)
                f.close()
            with open('{}/promptTokensSize_{}.json'.format(outDir,experimentId), 'w', encoding='utf-8') as f:
                json.dump(promptsizesTokens, f, ensure_ascii=False, indent=4)
                f.close()

            if len(times)> 0 and len(thougputs) > 0:
                stats = {"tp": {"median":statistics.median(thougputs), "mean":statistics.mean(thougputs), "max":max(thougputs), "min":min(thougputs), "len": len(thougputs)},
                         "latency":  {"median":statistics.median(times), "mean":statistics.mean(times), "max":max(times), "min":min(times), "len": len(times)}
                         }

                with open('{}/metrics_{}.json'.format(outDir, experimentId), 'w', encoding='utf-8') as f:
                    json.dump(stats, f, ensure_ascii=False, indent=4)
                    f.close()

            config = { "model" : model, "world_size":world_size, "repetitions":repetitions, "benchmark_name":benchmark_name, "maxtokensout": maxtokensout, "batch_size": batch_size,"out": batch_size,  "typeInference":typeInference,
           "inputSort":inputSort,
            "precision": precision,
            "randomSeed":randomSeed,
            "initTime":initTime,
            "endTime":time.perf_counter(),
                     }

            with open('{}/config_{}.json'.format(outDir, experimentId), 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=4)
                f.close()

            print("Results stored in {}".format(outDir))


def computeOutVar(batchtime, promptsizesTokens, rawResults, resultsCompletion, samples, thougputs):
    tokensGeneratedPerBatch = 0
    for aResult in resultsCompletion:
        rawResults.append(aResult)
        result = dict(task_id=aResult["problem"], completion=aResult["generated_text"])
        promptsizesTokens.append(aResult["nr_prompt_token_ids"])
        samples.append(result)
        tokensGeneratedPerBatch += int(aResult["nr_token_ids"])
    thougputs.append(tokensGeneratedPerBatch / batchtime)


if __name__ == "__main__":
    fire.Fire(main)