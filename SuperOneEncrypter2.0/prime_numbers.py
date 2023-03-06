import math
import random
import pathlib
import time


class Prime_number_Tool:
    # arr = []
    # prime_numbers = []
    # dir_path = pathlib.Path.cwd()
    # path = pathlib.Path(dir_path, 'finalChek.txt')
    # f = open(path, 'r')
    # for i in f:
    #     prime_numbers.append(int(i))


    # @classmethod
    def __init__(self):
        pass


    @classmethod
    def BPSW(self, n):
        if n == 2:
            return True
        if not n & 1:
            return False
        d = n - 1
        while d & 1 == 0:
            d >>= 1
        for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(100):
                x = pow(x, 2, n)
                if x == 1:
                    return False
                if x == n - 1:
                    a = 0
                    break
            if a:
                return False
        return True

    @classmethod
    def is_prime_number(self, n):
        self.arr.clear()
        if n % 10 != 5:
            if n <= self.prime_numbers[-1]:
                for i in self.prime_numbers:
                    if n < int(i):
                        return False
                    elif n == int(i):
                        return True
            for i in range(50):
                a = self.rand(5, n - 2)
                if (math.gcd(a, n) != 1):
                    return False
                if (pow(a, n - 1, n) != 1):
                    return False
            #  print("end of ferma test")
            for i in self.prime_numbers[:500]:
                if n % int(i) == 0:
                    return False
                if int(i) > math.isqrt(n):
                    break
            return True
        else:
            return False


    @classmethod
    def rand(self, a, b):
        while True:
            n = random.randint(a, b)
            if (n in self.arr):
                pass
                #print("тык")
            else:
                self.arr.append(n)
                return n

    @classmethod
    def factorization(self, n):
        if n % 2 == 0:
            print(2)
        for i in range(3, math.isqrt(n) + 2, 2):
            if n % i == 0:
                return i

    @classmethod
    def find_prime_number(self, n):
        n = n + (6 - n % 6)
        i = n
        while True:
            if self.BPSW(i + 1):
                return i + 1
            elif self.BPSW(i + 5):
                return i + 5
            i += 6


def primeFactors(n, factors):
    if (n % 2 == 0):
        factors.append(2)
    while (n % 2 == 0):
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if (n % i == 0):
            factors.append(i)

        while (n % i == 0):
            n = n // i

    if (n > 2):
        factors.append(n)

    return factors


def power(n, r, q):
    total = n

    for i in range(1, r):
        total = (total * n) % q

    return total




