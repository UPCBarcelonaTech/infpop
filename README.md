# Appendix of paper: ``The Impact of Hyperparameters on Large Language Model Inference Performance: An Evaluation of  vLLM and HuggingFace Pipelines``

## Results

### RQ 1

The data analyzed to respond to RQ 1 is available in the following files: [allData.md](allData.md) (also available in CVS format).
All hyperplane plots are available in the [hyperplane plots](RQ1/hyperplane_plots) folder.
For each model and engine, we show a static version of the plot (pdf) and a dynamic version where user can interact with the plot e.g., rotate, zoom. That is in the  HTML file.
Examples,[bloom-1b7-static](RQ1/hyperplane_plots/plot_hyperplane_a100_autohf_Bloom-1b7_mtg_5_throughput.html) [bloom-1b7-interactive](RQ1/hyperplane_plots/plot_hyperplane_a100_autohf_Bloom-1b7_mtg_5_throughput.pdf)

### RQ 2

Tables [Scale for A100 AutoHF](RQ2/table_gpuscale_a100_autohf.md) and [Scale for V100 AutoHF](RQ2/table_gpuscale_tesla_autohf.md) shows the throughput accoss different number of GPUs for HF.
Tables [Scale for A100 vLLM](RQ2/table_gpuscale_a100_vLLM.md) and [Scale for V100 vLLM](RQ2/table_gpuscale_tesla_vLLM.md) shows the throughput accoss different number of GPUs for vLLM.

The folder [statistics](RQ2/statistics) contains statistics computed for RQ2.

The folder [plots](RQ2/plots) contains plots for RQ2.

Table comparison of throughputf from HF and vLLM is available for [A100](RQ2/table_comparison_a100.md) and [v100 (tesla)](RQ2/table_comparison_tesla.md).

### RQ 3

The Tables and plots showing the throughput for different batch sizes and number of GPUs are in folder [tables](RQ3/tables), [plots (statics)](RQ3/plots), and [plots (interactive)](RQ3/plots_interactive).
The folder [statistics](RQ3/statistics) contains statistics computed for RQ3.

### RQ 4
Tables [improvement_hardware_vLLM.md](RQ4/2Fimprovement_hardware_vLLM.md)[improvement_hardware_autohf.md](RQ4/2Fimprovement_hardware_autohf.md) shows the improvements of using Nvidia A100 w.r.t Nvidia v100 (tesla) for vLLM and HF respectively.
The folder [statistics](RQ4/statistics) contains statistics computed for RQ4.

### RQ 5

Folder [RQ5](RQ5) contains the files that details of the improvements of applying HPO in GPU model upgrade (from v100 to A100) and downgrade (from A100 to V100) for vLLM and HF.


### Considerations

Nvidia V100 and Nvidia Tesla are used interchangeably in the paper/appendix.

## Scripts

The scripts used to generate the data and plots are available in the [scripts](scripts) folder.



