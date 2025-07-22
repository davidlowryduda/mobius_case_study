
# Code Accompanying "Studying Number Theory with Deep Learning" #

This repository contains code to generate data and ML models as used in the
paper [Studying number theory with deep learning: a case study with the Möbius
and squarefree indicator functions](https://arxiv.org/abs/2502.10335) by David
Lowry_Duda. Building on Charton's [Int2Int](https://github.com/f-charton/Int2Int/tree/main)
transformer code, we train small transformer models to calculate the Möbius
function $\mu(n)$ and the squarefree indicator function $\mu^2(n)$.

The models attain nontrivial predictive power and we seek to explain why.
Ultimately we see that the models don't capture sophisticated computation.

This is more about the process towards figuring that out.

The preprint is on the
[arxiv:2502.10335](https://arxiv.org/abs/2502.10335).


**Contents**

1. [Code Requirements](#code-requirements)
1. [Code Overview](#code-overview)
1. [Description of Data](#description-of-data)
1. [Comments](#comments)
1. [License](#license)

## Code Requirements ##

This code requires [pytorch](https://pytorch.org/) to be installed and
configured. The running scripts assume that the user is using a
POSIX-compatible shell with GNU Core Utilities, such as `bash` on a modern
`Ubuntu`.

It is straightforward to adapt the running scripts to other environments.

Code to generate the training data calls the Gnu C++ compiler G++ to make
computing $\mu(n)$ more rapid. A pure python implementation of $\mu(n)$ is also
included (though *radically slower*) for the user's convenience.


## Code Overview ##

There are two parts to this problem: generating datafiles with $\mu(n)$ and
$\mu^2(n)$, and then training a small transformer model on these datafiles.

For the transformer, we use a pinned version of
[Int2Int](https://github.com/f-charton/Int2Int/tree/main).
Note that the API to use Int2Int has changed since these experiments were
carried out; to replicate the work here, be sure to use the pinned version
indicated in this repository.

If you have cloned this repository and want to clone the pinned Int2Int
submodule, you can call

    git submodule init
    git submodule update

The remainder of the code consists of helper scripts to generate the data and
sample scripts to show how to run Int2Int on the data.

One way to proceed is to do the following.

    cd src/run_int2int_scripts
    make run
    # If you're very patient and want to use a CPU:
    # make run-cpu

This will begin to train an Int2Int small transformer library. If you encounter
an error, let me know.

Some additional details are in

- My [general report](https://davidlowryduda.com/ml-mobius-general/) on this
  problem scenario.
- My [technical report](https://davidlowryduda.com/ml-mobius-technical/) on
  this problem scenario.


### Notebooks ###

The code also includes two notebooks demonstrating how the results were parsed.
These notebooks are records of parsing for the paper. Very small adjustments
would be necessary to use these on newly trained data.

- [make_model_plots.ipynb](./notebooks/make_model_plots.ipynb) parses the
  training logs of Int2Int and makes the plots of accuracy vs epoch (and a
  couple of other plots that are not included in the paper).
- [study_corrupted_inputs.ipynb](./notebooks/study_corrupted_inputs.ipynb)
  studies the trained models' behavior on corrupted input data. The datafiles
  are corrupted by one of: randomizing $n \bmod 2$, randomizing $n \bmod 3$,
  randomizing both $n \bmod 2$ and $n \bmod 3$, and randomizing *everything
  except* $n \bmod 2$ and $n \bmod 4$. Then these logs are parsed and plots are
  made.


## Description of Data ##

By default, this repository will create $10^6$ distinct inputs and separate
them into a training set of size $9 \cdot 10^5$ and a testing set of size
$10^5$.
The data consists of Int2Int encoded values of the form

    (n MOD p, p) for the first 100 primes \t mu(n) \n

This data will be created in `/input/`.

If models are used following the provided scripts, these models will be created
in `/models/`. The models created there include training logs and checkpoints
containing (pickled) pytorch models.


## Comments ##

This repository is not accepting contributions. But I will continue to
consider applications of ML to math (and vice versa) further. Feel free to
contact me with ideas, suggestions, or other proposals for projects and
collaboration.


## License ##

The code here is made available under the MIT License. See the [LICENSE
file](LICENSE) for more.
