"""
generate_corrupted_datafiles.py - make mobius datafiles for Int2Int

This also makes datafiles with incorrect values at the primes 2 and 3.

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


def make_line(input_func, output_func, n):
    return input_func(n) + "\t" + output_func(n) + "\n"


def make_correct_input(n):
    ret = []
    count = len(primes_100)
    ret.append(f"V{2*count}")
    for p in primes_100:
        ret.append(encode_integer(n % p))
        ret.append(encode_integer(p))
    return ' '.join(ret)


def make_23_wrong_input(n):
    ret = []
    count = len(primes_100)
    ret.append(f"V{2*count}")
    for p in primes_100[:2]:
        ret.append(encode_integer(random.randint(0, p-1)))
        ret.append(encode_integer(p))
    for p in primes_100[2:]:
        ret.append(encode_integer(n % p))
        ret.append(encode_integer(p))
    return ' '.join(ret)


def make_23_only_right_input(n):
    ret = []
    count = len(primes_100)
    ret.append(f"V{2*count}")
    for p in primes_100[:2]:
        ret.append(encode_integer(n % p))
        ret.append(encode_integer(p))
    for p in primes_100[2:]:
        ret.append(encode_integer(random.randint(0, p-1)))
        ret.append(encode_integer(p))
    return ' '.join(ret)


def make_p_random_input_func(q):
    def inner(n):
        ret = []
        count = len(primes_100)
        ret.append(f"V{2*count}")
        for p in primes_100:
            if p != q:
                ret.append(encode_integer(n % p))
                ret.append(encode_integer(p))
            else:
                ret.append(encode_integer(random.randint(0, p-1)))
                ret.append(encode_integer(p))
        return ' '.join(ret)
    return inner


def make_output(n):
    return str(dldmobius(n))


def make_output_sq(n):
    return str(dldmobius(n)**2)


def main():
    outdir = "../../input/"
    seen = set()
    with (
        open(outdir + "mu_only23_correct.txt", "w", encoding="utf8") as mu23file,
        open(outdir + "musq_only23_correct.txt", "w", encoding="utf8") as musq23file,
        open(outdir + "mu_2_random.txt", "w", encoding="utf8") as mu2hatfile,
        open(outdir + "musq_2_random.txt", "w", encoding="utf8") as musq2hatfile,
        open(outdir + "mu_p_3_random.txt", "w", encoding="utf8") as mu3hatfile,
        open(outdir + "musq_p_3_random.txt", "w", encoding="utf8") as musq3hatfile,
        open(outdir + "mu_23_random.txt", "w", encoding="utf8") as mu23hatfile,
        open(outdir + "musq_23_random.txt", "w", encoding="utf8") as musq23hatfile,
        open(outdir + "mu_true.txt", "w", encoding="utf8") as mu23truefile,
        open(outdir + "musq_true.txt", "w", encoding="utf8") as musq23truefile,
    ):
        while len(seen) < 10**5:
            n = random.randint(2, 10**13)
            if n in seen:
                continue
            seen.add(n)
            mu23file.write(
                make_line(make_23_only_right_input, make_output, n)
            )
            musq23file.write(
                make_line(make_23_only_right_input, make_output_sq, n)
            )
            mu2hatfile.write(
                make_line(make_p_random_input_func(2), make_output, n)
            )
            musq2hatfile.write(
                make_line(make_p_random_input_func(2), make_output_sq, n)
            )
            mu3hatfile.write(
                make_line(make_p_random_input_func(3), make_output, n)
            )
            musq3hatfile.write(
                make_line(make_p_random_input_func(3), make_output_sq, n)
            )
            mu23hatfile.write(
                make_line(make_23_wrong_input, make_output, n)
            )
            musq23hatfile.write(
                make_line(make_23_wrong_input, make_output_sq, n)
            )
            mu23truefile.write(
                make_line(make_correct_input, make_output, n)
            )
            musq23truefile.write(
                make_line(make_correct_input, make_output_sq, n)
            )


if __name__ == "__main__":
    print("Making good and corrupt datafiles in ../../input")
    main()
    print("Done")
