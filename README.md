

<p align="center">
  <img src="https://github.com/lucanest/Phyloformer/blob/main/phyloformer.png">
</p>

# Phyloformer: Towards fast and accurate Phylogeny estimation<br/> with self-attention Networks

- Luca Nesterenko
- Bastien Boussau
- Laurent Jacob

This repository contains the scripts for [the paper](https://arxiv.org/abs/???):


```bibtex
@article{Nesterenko2022phyloformer,
  author={Nesterenko Luca, Boussau Bastien, Jacob Laurent},
  title={PHYLOFORMER: TOWARDS FAST AND ACCURATE PHYLOGENY ESTIMATION
WITH SELF-ATTENTION NETWORKS},
  year={2022},
  doi={?},
  url={?},
  journal={bioRxiv}
}
```

![](sketch.png)

## Install
### First, install mamba:
```
conda install -n base -c conda-forge mamba
```

### To install it:
```
mamba env create -f environment.yml
```

### To run it:

`conda activate phylo`

### Test run
To check that the installation is successful one can run

```
python phyloformer/predict.py ./testdata/alignments
```
and then 
```
python testdata/test.py
```
the printed mean normalized Robinson-Fould distance should be equal to 0.063.


## Usage

We provide the software as a ready to use tool for phylogenetic inference, one can simply run
```
python phyloformer/predict.py
```
providing as argument a directory containing multiple sequence protein alignments in .fasta format,
the program will then predict a phylogenetic tree for each alignment and write them in Newick format in the same directory.

If the user wishes to choose a different directory where the predictions will be saved he can specify it with the `--o` flag.

By default the Phyloformer model used for inference is the one trained on simulations based on the PAM model of evolution, a different model to use can be specified with the `--m` flag (the other one currently available being the one trained on [evosimz](https://gitlab.com/ztzou/phydl/-/tree/master/evosimz) simulations).

Finally, if an NVIDIA gpu is available, `--gpu true` allows to exploit it offering a great speed up in inference.
## Tests and benchmarking
The data simulated using Seq-Gen is available at:

- PAM model: [https://plmbox.math.cnrs.fr/f/f5a2ed2667a841cba6f0/](https://plmbox.math.cnrs.fr/f/f5a2ed2667a841cba6f0/).
- WAG model: [https://plmbox.math.cnrs.fr/f/834248a35ba64752a6a4/](https://plmbox.math.cnrs.fr/f/834248a35ba64752a6a4/).

The simulations under the Evosimz model are available at [https://datadryad.org/stash/dataset/doi%253A10.5061%252Fdryad.rbnzs7h91](https://datadryad.org/stash/dataset/doi%253A10.5061%252Fdryad.rbnzs7h91).

## Disclaimer:

Phyloformer is still at the stage of the proof of concept. In
particular, we observed lower performances:

- For trees with more than 40 leaves. As discussed in the manuscript
  this will likely be fixed after we re-train on trees with larger
  evolutionary distances.

- For topologies generated under a birth-death model. The topologies
  used in the experiments reported in the manuscript were generated
  under the populate function of the ete3 package. We are still
  investigating the possible reasons for this discrepancy.

We are making the trained models available for transparency and would
be very interested to hear about cases where these models
underperform.
