import math
import  random


def is_prime_number(n):
    arr.clear()
    if n % 10 != 5:
        if n <= prime_numbers[-1]:
            for i in prime_numbers:
                if n < int(i):
                    return False
                elif n == int(i):
                    return True
        for i in range(50):
            a = rand(5, n - 2)
            if (math.gcd(a, n) != 1):
                return False
            if (pow(a, n - 1, n) != 1):
                return False
        #  print("end of ferma test")
        for i in prime_numbers[:500]:
            if n % int(i) == 0:
                return False
            if int(i) > math.isqrt(n):
                break
        return True
    else:
        return False

def rand(a, b):
    while True:
        n = random.randint(a, b)
        if (n in arr):
            pass
            #print("тык")
        else:
            arr.append(n)
            return n


def factorization(n):
    if n % 2 == 0:
        print(2)
    for i in range(3, math.isqrt(n) + 2, 2):
        if n % i == 0:
            return i


def find_prime_number(n):
    n = n + (6 - n % 6)
    i = n
    while True:
        if is_prime_number(i + 1):
            return i + 1
        elif is_prime_number(i + 5):
            return i + 5
        i += 6


arr = []
prime_numbers = []
f = open('finalChek.txt', 'r')
for i in f:
    prime_numbers.append(int(i))
