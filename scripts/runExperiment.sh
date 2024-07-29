#!/bin/bash

set_cuda_visible_devices() {
  if [ -z "$1" ]; then
    echo "Usage: set_cuda_visible_devices <i>"
    return 1
  fi

  local i="$1"
  local devices=""

  for ((j = 0; j < i; j++)); do
    devices="${devices}$j,"
  done

  devices="${devices%,}"
  export CUDA_VISIBLE_DEVICES="$devices"
  echo "CUDA_VISIBLE_DEVICES set to: $CUDA_VISIBLE_DEVICES"
}


outkey=$1
outpath="~/aimpetus-results/$1"
model=$2
vllm=$3
echo --out $outpath --model $model --vLLM $vllm

cuda_device_count=$(nvidia-smi --query-gpu=count --format=csv,noheader,nounits | head -1)
echo "Number of CUDA devices: $cuda_device_count"


inputSort="inputsizeinc"

if [ "$4" ]; then
  precision=$4
else
  precision="auto"
fi

echo "Input inputsizeinc: $inputSort"


modelKey=${model//\//_}
outlog="~/aimpetus-logs/${outkey}/${inputSort}/${vllm}/${modelKey}/"
mkdir -p $outlog

# Loop through the world sizes, batch sizes, and max tokens out.
for iw in 1 2 4 8
do
    set_cuda_visible_devices $iw
    echo CUDA_vD $CUDA_VISIBLE_DEVICES

     if [ "$iw" -gt "$cuda_device_count" ]; then
        break
    fi

    echo --world_size  $iw --out $outpath --model $model --typeInference $vllm --inputSort $inputSort --precision $precision
    echo echo `date`
    pkill -9 nvidia > /dev/null 2>&1
    pkill -9 python > /dev/null 2>&1
    echo Launching Python....
    timestamp=$(date +%s)
    time timeout -k 10s 240m  python ~/aimpetus/runInference.py --world_size  $iw  --out $outpath --model $model --typeInference $vllm --inputSort $inputSort --precision $precision > "${outlog}/ws_${iw}_ts_${timestamp}.txt" 2>&1
    if [ $? -eq 124 ]; then
       echo Timeout occurred --world_size  $iw --out $outpath --model $model --typeInference $vllm -inputSort $inputSort precision $precision
    fi
    echo END: --world_size  $iw --out $outpath --model $model --typeInference $vllm --inputSort $inputSort

done
echo `date`
echo DONE