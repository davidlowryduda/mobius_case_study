
# Running Int2Int #

These are example scripts to run Int2Int.

In practice, it's more convenient to wrap similar scripts in similar logic that
logs and persists after errors. For example, a GPU might hiccup and these
scripts won't automatically restart.


## Quickstart ##

For a quick start, one can run

    make run

This will attempt to

1. generate datafiles (after attempting to compile Möbius code if it's not
   already compiled),
2. train 200 epochs of $\mu(n)$ predictions, and
3. train 200 epochs of $\mu^2(n)$ predictions.

This should take a long time.
