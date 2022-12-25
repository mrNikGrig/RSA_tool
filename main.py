import random
import time
import math
import matplotlib.pyplot as plt
from tqdm import tqdm
import rsa
import numpy.random



class RSA_Tool:
    prime_numbers = []

    p = 0
    q = 0
    e = 0
    d = 0
    n = 0
    arr = []
    def __init__(self):
        f = open("finalChek.txt", "r")
        for i in f:
            self.prime_numbers.append(int(i))

    def get_bit_keys(self, col_bits, e=65577):
        p = self.find_prime_number(random.randint(2 ** (col_bits // 2), 2 ** ((col_bits//2) + 1)))
        q = self.find_prime_number(random.randint(2 ** (col_bits // 2)-1, 2 ** ((col_bits // 2))))
        return self.gen_keys(p, q, e)



    def gen_keys(self, p, q, e):
        self.n = p * q
        f = (p - 1) * (q - 1)
        while math.gcd(e, f) != 1:
            e += 2
            if e > f:
                print("error")
        self.d = pow(e, -1, f)
        self.e = e
        return self.e, self.d, self.n


    def rand(self, a, b):
        while True:
            n = random.randint(a, b)
            if (n in self.arr):
                pass
                #print("тык")
            else:
                self.arr.append(n)
                return n

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


    def find_prime_number(self, n):
        n = n + (6 - n % 6)
        i = n
        while True:
            if self.is_prime_number(i + 1):
                return i + 1
            elif self.is_prime_number(i + 5):
                return i + 5
            i += 6

    def factorization(self, n):
        if n % 2 == 0:
            print(2)
        for i in range(3, math.isqrt(n), 2):
            if n % i == 0:
                return i


    def encrypt(self, text):
        numKode = []
        for i in text:
            numKode.append(pow(ord(i), self.e, self.n))
        return numKode

    def decrypt(self, encrMessage):
        s = ''
        for i in encrMessage:
            s += chr(pow(i, self.d, self.n))

        return s


def test():
    my_RSA = RSA_Tool()
    basic_rsa = rsa

    m = numpy.random.randint(13, 1000, 20)
    isNorm = True
    for i in m:
        i = int(i)
        e, d, n = my_RSA.get_bit_keys(256)
        if (pow(pow(i, e, n), d, n)) != i:
            print("error")
            isNorm = False
            break
    if isNorm:
        print("eee i feel good")

    my_time_small_keys = []
    normal_time_small_keys = []
    for i in tqdm(range(100)):
        t1 = time.time()
        my_RSA.get_bit_keys(256)
        t2 = time.time()
        my_time_small_keys.append(t2 - t1)
    for i in tqdm(range(100)):
        t1 = time.time()
        basic_rsa.newkeys(256)
        t2 = time.time()
        normal_time_small_keys.append(t2 - t1)

    my_time_average_keys = []
    normal_time_average_keys = []
    for i in tqdm(range(100)):
        t1 = time.time()
        my_RSA.get_bit_keys(1024)
        t2 = time.time()
        my_time_average_keys.append(t2 - t1)
    for i in tqdm(range(100)):
        t1 = time.time()
        basic_rsa.newkeys(1024)
        t2 = time.time()
        normal_time_average_keys.append(t2 - t1)

    my_time_big_keys = []
    normal_time_big_keys = []
    for i in tqdm(range(100)):
        t1 = time.time()
        my_RSA.get_bit_keys(4096)
        t2 = time.time()
        my_time_big_keys.append(t2 - t1)
    for i in tqdm(range(100)):
        t1 = time.time()
        basic_rsa.newkeys(4096)
        t2 = time.time()
        normal_time_big_keys.append(t2 - t1)

    print("all data for small numbers(256bit)")
    print("my median is " + str(numpy.mean(my_time_small_keys)))
    print("normal median is " + str(numpy.mean(normal_time_small_keys)))
    plt.plot(numpy.array(range(100), int), numpy.array(my_time_small_keys, float), label='оптимизированный подход')
    plt.plot(numpy.array(range(100), int), numpy.array(normal_time_small_keys, float), label='подход rsa')
    plt.legend(prop={"size": 14})
    plt.xlabel('итерация', fontsize=14)
    plt.ylabel('время', fontsize=14)
    plt.grid(True)
    plt.savefig('small_nums.png')
    plt.show()

    print("all data for average numbers(1024bit)")
    print("my median is " + str(numpy.mean(my_time_average_keys)))
    print("normal median is " + str(numpy.mean(normal_time_average_keys)))
    plt.plot(numpy.array(range(100), int), numpy.array(my_time_average_keys, float), label='оптимизированный подход')
    plt.plot(numpy.array(range(100), int), numpy.array(normal_time_average_keys, float), label='подход rsa')
    plt.legend(prop={"size": 14})
    plt.xlabel('итерация', fontsize=14)
    plt.ylabel('время', fontsize=14)
    plt.grid(True)
    plt.savefig('average_nums.png')
    plt.show()

    print("all data for big numbers(4096bit)")
    print("my median is " + str(numpy.mean(my_time_big_keys)))
    print("normal median is" + str(numpy.mean(normal_time_big_keys)))
    plt.plot(numpy.array(range(100), int), numpy.array(my_time_big_keys, float), label = 'оптримизированный подход')
    plt.plot(numpy.array(range(100), int), numpy.array(normal_time_big_keys, float), label = 'проход rsa')
    plt.legend(prop={"size": 14})
    plt.xlabel('итерация', fontsize=14)
    plt.ylabel('время', fontsize=14)
    plt.grid(True)
    plt.savefig('big_nums.png')
    plt.show()


def main():
    test()


if __name__ == '__main__':
    main()


