import json
from hyperopt import hp
from hyperopt import fmin, tpe, space_eval
import numpy as np
import pandas as pd

def format_splitName(value):
    return "_".join(value.split("_")[1:]).capitalize()


def objective(args):
    ibatchSize, inrGPUs = args['batchSize'], args['nrGPUs']

    values = dfToOptimize[(dfToOptimize['batchSize'] == ibatchSize) & (dfToOptimize['nrGPUs'] == inrGPUs)]['throughput']

    if len(values)> 0:
        iThroughput = values.values[0]
        if pd.isna(iThroughput):
            return 99999999
        return iThroughput * -1 ## we want to maximize throughput
    else:
        return 99999999


hpBatchSize = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
hpNrGPUs = [1,2,4,8]
space = {
    'batchSize': hp.choice('batchSize', hpBatchSize),
    'nrGPUs': hp.choice('nrGPUs', hpNrGPUs),
    }


def navigate():
    loadDataset()

    metric = "throughput"
    for selectedHard in ["a100", "tesla"]:
        for anEgine in ["autohf", "vLLM"]:
            pass


def loadDataset():
    dataToAnalyze = "../allData.csv"
    print("Analyzing {}".format(dataToAnalyze))
    df1 = pd.read_csv(dataToAnalyze)
    df1 = df1[~((df1['model'] == "mistralai_Codestral-22B-v0.1") & (df1['hardware'] == "a100"))]
    df1["model"] = df1["model"].map(format_splitName)
    return df1

def testAll(originalHardware, targetHardware,  targetEngine = "autohf"):
    global dfToOptimize
    dfAll = loadDataset()

    print(dfAll['model'].unique())

    allResult = []
    for i, targetModel in enumerate(dfAll['model'].unique()):
        print(f"\n------model {i}/{len(dfAll['model'].unique())}: {targetModel}")
        result = improveForModel(dfAll, targetEngine, targetModel, originalHardware=originalHardware, targetHardware=targetHardware)
        allResult.append(result)

    print(f"\nFinal results: from {originalHardware} to {targetHardware}")
    allMedian = []
    for r in allResult:
        print(r)
        if 'median' in r and r['median'] >= 0:
            allMedian.append(r['median'])

    allPositive = [x for x in allMedian if x > 0]


    print(f"End- summary: results_hpo_{targetEngine}_from_{originalHardware}_to_{targetHardware} \nsummaryMedianMedian: {np.median(allMedian)} summaryMedianMean {np.mean(allMedian)} allMedians {allMedian} allPositive  {len(allPositive)},")
    root = {"summaryMedianMedian": np.median(allMedian), "summaryMedianMean": np.mean(allMedian), "allMedians": allMedian, "allPositive": len(allPositive), "summaryTotal": len(allMedian), "data" : allResult}
    f = open(f"results_hpo_{targetEngine}_from_{originalHardware}_to_{targetHardware}.json", "w")
    f.write(json.dumps(root, indent=4,  cls=NumpyEncoder))
    f.close()
    return root
def testSingle():
    global dfToOptimize
    dfAll = loadDataset()
    print(dfAll['model'].unique())
    targetModel = "Wizardcoder-15b-v1.0"#"Codellama-7b-hf" #"Phi-1"
    targetEngine = "autohf"
    allResult = []

    result = improveForModel(dfAll, targetEngine, targetModel)
    allResult.append(result)

    print("\nFinal results: ")
    for r in allResult:
        print(r)

def improveForModel(dfAll, targetEngine, targetModel,originalHardware = "tesla",  targetHardware = "a100", nrRepeat=10):
    global dfToOptimize
    dfAll = dfAll[(dfAll['model'] == targetModel) & (dfAll['engine'] == targetEngine)]
    dfAll = dfAll[["hardware", "batchSize", "nrGPUs", "throughput"]]

    ## Defining subdatasets
    dfTotalFromOriginal = dfAll[dfAll['hardware'] == originalHardware]
    dfTotalFromTarget = dfAll[dfAll['hardware'] == targetHardware]
    ### global variable used by Hyperopt
    dfToOptimize = dfTotalFromTarget

    bestInOriginal = None
    dfTotalFromOriginal = dfTotalFromOriginal.sort_values( by='throughput', ascending=False)
    dfTrInTargetWithBestOriginal = None
    for index, row in dfTotalFromOriginal.iterrows():
        print(f"--- hardware {row['hardware']} gpu {row['nrGPUs']} batchSize {row['batchSize']} throughput {row['throughput']}")
        dfTrInTargetWithBestOriginal = dfTotalFromTarget[
            (dfTotalFromTarget['batchSize'] == row['batchSize']) & (
                    dfTotalFromTarget['nrGPUs'] == row['nrGPUs'])]

        print(f"dfTrInTargetWithBestOriginal for current row: {dfTrInTargetWithBestOriginal}")

        if len(dfTrInTargetWithBestOriginal) > 0 and dfTrInTargetWithBestOriginal['throughput'].values[0] > 0:
            print("Found best in original in target")
            bestInOriginal = row
            break

    print(f"Best in original ({originalHardware}): \n{bestInOriginal}")
    if bestInOriginal is None:
        print("No value found for original hardware")
        return {"model": targetModel, "engine": targetEngine, "message":"Error-nothing in the original"}

    print(
        f"Same config from best in original {originalHardware} in target {targetHardware}: \n{dfTrInTargetWithBestOriginal}")

    if dfTrInTargetWithBestOriginal is None or len(dfTrInTargetWithBestOriginal) == 0:
        print("No value found for target hardware")
        return {"model": targetModel, "engine": targetEngine, "message":"Error-nothing in the target"}



    jsonBestInOriginal = {"originalHardware": originalHardware, "batchSize": bestInOriginal['batchSize'],
                          "nrGPUs": bestInOriginal['nrGPUs'], "throughput": bestInOriginal['throughput']}

    jsonBestOriginalInTarget = {"originalHardware": targetHardware,
                                "batchSize": dfTrInTargetWithBestOriginal['batchSize'].values[0],
                                "nrGPUs": dfTrInTargetWithBestOriginal['nrGPUs'].values[0], "throughput": dfTrInTargetWithBestOriginal['throughput'].values[0]}

    jsonTunings = []
    allImprovements = []
    for iRepet in range(nrRepeat):
        result = optimizeInference(maxEval=100)

        bestInTarget = result["obtained"]

       # print(f"Best in original ({originalHardware}): \n{bestInOriginal}")
        print(f"best In Target {targetEngine} found by TPE: \n{bestInTarget} ")
        print(
            f"Same config from best in original {originalHardware} in target {targetHardware}: \n{dfTrInTargetWithBestOriginal}")

        differece = bestInTarget['throughput'].values[0] - dfTrInTargetWithBestOriginal['throughput'].values[0]
        print(f"Difference between best in original and best in target: {differece}")


        improvement = (differece / dfTrInTargetWithBestOriginal['throughput'].values[0]) * 100
        jsonAtuning = {"nr": iRepet, "batchSize": bestInTarget['batchSize'].values[0],
                       "nrGPUs": bestInTarget['nrGPUs'].values[0], "throughput": bestInTarget['throughput'].values[0], "improvement":improvement}

        jsonTunings.append(jsonAtuning)
        allImprovements.append(improvement)
        print(f"Improvement: {improvement}%")

    print(f"All {targetModel} improvements: ", allImprovements)
    print(f"Mean improvement: {np.mean(allImprovements)}")
    print(f"Median improvement: {np.median(allImprovements)}")
    print(f"Std improvement: {np.std(allImprovements)}")
    print(f"Max improvement: {np.max(allImprovements)}")
    print(f"Min improvement: {np.min(allImprovements)}")

    return {"model":targetModel,
            "engine":targetEngine,
            "from": originalHardware,
            "to": targetHardware,
            "mean": np.mean(allImprovements),
            "median": np.median(allImprovements),
            "std": np.std(allImprovements),
            "max": np.max(allImprovements),
            "min": np.min(allImprovements),
            "bestInOriginal": jsonBestInOriginal,
            "bestOriginalInTarget":jsonBestOriginalInTarget,
            "allImprovements": jsonTunings,
            }

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer, np.int64)):
            return int(obj)
        elif isinstance(obj, (np.floating, np.float64)):
            return float(obj)
        elif isinstance(obj, (np.ndarray,)):
            return obj.tolist()
        return super(NumpyEncoder, self).default(obj)
def optimizeInference(maxEval=100):
    print("Max throughput: \n", dfToOptimize[dfToOptimize['throughput'] == dfToOptimize['throughput'].max()])
    best = fmin(objective, space, algo=tpe.suggest, max_evals=maxEval)
    print("best ", best)
    print("space_eval", space_eval(space, best))
    iThroughput = dfToOptimize[ (dfToOptimize['batchSize'] == hpBatchSize[best['batchSize']]) & (dfToOptimize['nrGPUs'] == hpNrGPUs[best['nrGPUs']])]
    print("\nResults: ")
    #print("\nGround-Truth: Max throughput: \n", dfToOptimize[dfToOptimize['throughput'] == dfToOptimize['throughput'].max()])
    print("\nObtained: Max throughput found \n", iThroughput)
    return {"obtained": iThroughput, "groundTruth": dfToOptimize[dfToOptimize['throughput'] == dfToOptimize['throughput'].max()]}

def plotAll(rAll, labels):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    # Create violin plots

    data = [ [x for x in r["allMedians"] if x < 300] for r in rAll]

    parts = ax.violinplot(data, showmeans=True, showmedians=True)
    # Customize the plot
    #ax.set_xticks([1, 4])
    ax.set_xticks([1, 2, 3, 4])
    ax.set_xticklabels(labels)

    colors = ['skyblue', 'lightgreen','skyblue', 'lightgreen']
    for pc, color in zip(parts['bodies'], colors):
        pc.set_facecolor(color)
        pc.set_edgecolor('black')

    for partname in  ('cmeans', 'cmedians', 'cbars', 'cmins', 'cmaxes'):
        vp = parts[partname]
        vp.set_edgecolor('black')
        vp.set_linewidth(1.5)
    # ax.set_title('Violin Plots')
    ax.set_ylabel('Throughput Improvement %', fontsize=20)
    plt.xticks(fontsize=16)
    plt.yticks( fontsize=20)
    plt.xticks(rotation=15)
    #ax.set_yscale('log')
    # Display the plot
    #plt.show()
    plt.savefig("violin_hpo.pdf", bbox_inches='tight')
    plt.close()


if __name__ == '__main__':

    rUpAuto = testAll(originalHardware="tesla", targetHardware="a100", targetEngine="autohf")
    rDownAuto = testAll(originalHardware="a100", targetHardware="tesla", targetEngine="autohf")

    rUpvLLM = testAll(originalHardware="tesla", targetHardware="a100", targetEngine="vLLM")
    rDownLLM = testAll(originalHardware="a100", targetHardware="tesla", targetEngine="vLLM")

   # plot()
   # rUpAuto = json.load(open("results_hpo_autohf_from_tesla_to_a100.json"))
   # rDownAuto = json.load(open("results_hpo_autohf_from_a100_to_tesla.json"))
   # rUpvLLM = json.load(open("results_hpo_vLLM_from_tesla_to_a100.json"))
   # rDownLLM = json.load(open("results_hpo_vLLM_from_a100_to_tesla.json"))
    plotAll([rUpAuto,rDownAuto, rUpvLLM, rDownLLM ], labels = ['Upgr-HF', 'Downgr-HF', 'Upgr-vLLM', 'Downgr-vLLM'])