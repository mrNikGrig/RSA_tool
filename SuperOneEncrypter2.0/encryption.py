import math


def gen_keys(p, q, e):
    n = p * q
    f = (p - 1) * (q - 1)
    while math.gcd(e, f) != 1:
        e += 2
        if e > f:
            print("error")
    d = pow(e, -1, f)
    e = e
    return (e, d, n)