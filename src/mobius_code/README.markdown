
# Möbius Code #

When computing many values of $\mu(n)$, it's useful to have a quick evaluator.
This is a small, relatively efficient evaluator for $\mu(n)$. It is meant to be
built and then called from python.

To build the shared object file for python (on linux with g++ --- with the
typical modifications for other platforms and compilers), it should be
sufficient to call

    make mobius.so

If you do this, I recommend calling

    make test

to verify that the compilation works. One can examine
[mobius_test.py](./mobius_test.py) to see how one can use the built shared
library.


## Algorithm Description ##

This method of computing $\mu(n)$ is based on wheel factorization, where one
checks for square divisibility for each increasing factor before continuing
along the wheel. This means that if $n$ is divisible by the square of a small
prime, then this method terminates early (without completing the factorization)
and returns $0$.

The wheel is built from the primes $2$, $3$, and $5$.
