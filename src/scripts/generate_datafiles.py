"""
generate_datafiles.py - make mobius datafiles for Int2Int

NOTE: this implicitly assumes python3.10+. This could be made to work with
earlier version of python by using different context-manager syntax for opening
files.

## License Information ##

Copyright © 2025 David Lowry-Duda <david@lowryduda.com>

MIT License

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""
import random


from utils import dldmobius, encode_integer, primes_100


def make_line(inputfunc, outputfunc, n):
    return inputfunc(n) + "\t" + outputfunc(n) + "\n"


def make_input(n):
    ret = []
    count = len(primes_100)
    ret.append(f"V{2*count}")
    for p in primes_100:
        ret.append(encode_integer(n % p))
        ret.append(encode_integer(p))
    return ' '.join(ret)


def make_output_mu(n):
    return str(dldmobius(n))


def make_output_musq(n):
    return str(dldmobius(n)**2)


def main():
    outdir = "../../input/"
    seen = set()
    with (
        open(outdir + "mu_modp_and_p.txt", "w", encoding="utf8") as mufile,
        open(outdir + "musq_modp_and_p.txt", "w", encoding="utf8") as musqfile,
    ):
        while len(seen) < 10**1:
            n = random.randint(2, 10**13)
            if n in seen:
                continue
            seen.add(n)
            mufile.write(make_line(make_input, make_output_mu, n))
            musqfile.write(make_line(make_input, make_output_musq, n))


if __name__ == "__main__":
    print("Making datafiles in ../../input")
    main()
    print("Done.")
