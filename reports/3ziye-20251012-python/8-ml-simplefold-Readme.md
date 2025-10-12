
<h1 align="center"><strong>SimpleFold: Folding Proteins is Simpler than You Think</strong></h1>


<div align="center">

This github repository accompanies the research paper, [*SimpleFold: Folding Proteins is Simpler than You Think*](https://arxiv.org/abs/2509.18480) (Arxiv 2025).

*Yuyang Wang, Jiarui Lu, Navdeep Jaitly, Joshua M. Susskind, Miguel Angel Bautista*

[[`Paper`](https://arxiv.org/abs/2509.18480)]  [[`BibTex`](#citation)]

<img src="assets/intro.png" width="750">

</div>


## Introduction

We introduce SimpleFold, the first flow-matching based protein folding model that solely uses general purpose transformer layers. SimpleFold does not rely on expensive modules like triangle attention or pair representation biases, and is trained via a generative flow-matching objective. We scale SimpleFold to 3B parameters and train it on more than 8.6M distilled protein structures together with experimental PDB data. To the best of our knowledge, SimpleFold is the largest scale folding model ever developed. On standard folding benchmarks, SimpleFold-3B model achieves competitive performance compared to state-of-the-art baselines. Due to its generative training objective, SimpleFold also demonstrates strong performance in ensemble prediction. SimpleFold challenges the reliance on complex domain-specific architectures designs in folding, highlighting an alternative yet important avenue of progress in protein structure prediction.

</div>


## Installation

To install `simplefold` package from github repository, run
```
git clone https://github.com/apple/ml-simplefold.git
cd ml-simplefold
conda create -n simplefold python=3.10
python -m pip install -U pip build; pip install -e .
```
If you want to use MLX backend on Apple silicon: 
```
pip install mlx==0.28.0
pip install git+https://github.com/facebookresearch/esm.git
```

## Example 

We provide a jupyter notebook [`sample.ipynb`](sample.ipynb) to predict protein structures from example protein sequences. 

## Inference

Once you have `simplefold` package installed, you can predict the protein structure from target fasta file(s) via the following command line. We provide support for both [PyTorch](https://pytorch.org/) and [MLX](https://mlx-framework.org/) (recommended for Apple hardware) backends in inference. 
```
simplefold \
    --simplefold_model simplefold_100M \  # specify folding model in simplefold_100M/360M/700M/1.1B/1.6B/3B
    --num_steps 500 --tau 0.01 \        # specify inference setting
    --nsample_per_protein 1 \           # number of generated conformers per target
    --plddt \                           # output pLDDT
    --fasta_path [FASTA_PATH] \         # path to the target fasta directory or file
    --output_dir [OUTPUT_DIR] \         # path to the output directory
    --backend [mlx, torch]              # choose from MLX and PyTorch for inference backend 
```

## Evaluation

We provide predicted structures from SimpleFold of different model sizes:
```
https://ml-site.cdn-apple.com/models/simplefold/cameo22_predictions.zip # predicted structures of CAMEO22
https://ml-site.cdn-apple.com/models/simplefold/casp14_predictions.zip  # predicted structures of CASP14
https://ml-site.cdn-apple.com/models/simplefold/apo_predictions.zip     # predicted structures of Apo
https://ml-site.cdn-apple.com/models/simplefold/codnas_predictions.zip  # predicted structures of Fold-switch (CoDNaS)
```
We use the docker image of [openstructure](https://git.scicore.unibas.ch/schwede/openstructure/) 2.9.1 to evaluate generated structures for folding tasks (i.e., CASP14/CAMEO22). Once having the docker image enabled, you can run evaluation via:
```
python src/simplefold/evaluation/analyze_folding.py \
    --data_dir [PATH_TO_TARGET_MMCIF] \
    --sample_dir [PATH_TO_PREDICTED_MMCIF] \
    --out_dir [PATH_TO_OUTPUT] \
    --max-workers [NUMBER_OF_WORKERS]
```
To evaluate results of two-state prediction (i.e., Apo/CoDNaS), one need to compile the [TMsore](https://zhanggroup.org/TM-score/TMscore.cpp) and then run evaluation via:
```
python src/simplefold/evaluation/analyze_two_state.py \ 
    --data_dir [PATH_TO_TARGET_DATA_DIRECTORY] \
    --sample_dir [PATH_TO_PREDICTED_PDB] \
    --tm_bin [PATH_TO_TMscore_BINARY] \
    --task apo \ # choose from apo and codnas
    --nsample 5
```

## Train

You can also train or tune SimpleFold on your end. Instructions below include details for SimpleFold training. 

### Data preparation

#### Training targets

SimpleFold is trained on joint datasets including experimental structures from [PDB](https://www.rcsb.org/), as well as distilled predictions from [AFDB SwissProt](https://alphafold.ebi.ac.uk/download#swissprot-section) and [AFESM](https://afesm.foldseek.com/). Target lists of filtered SwissProt and AFESM targets thta are used in our training can be found:
```
https://ml-site.cdn-apple.com/models/simplefold/swissprot_list.csv # list of filted SwissProt (~270K targets)
https://ml-site.cdn-apple.com/models/simplefold/af