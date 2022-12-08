import random
import time
import math
import matplotlib.pyplot as plt
from tqdm import tqdm
import rsa
import numpy.random
f = open("finalChek.txt", "r")

class RSA_Tool:
    prime_numbers = []

    p = 0
    q = 0
    e = 0
    d = 0
    n = 0
    arr = []
    def __init__(self):
        for i in f:
            self.prime_numbers.append(int(i))

    def get_bit_keys(self, col_bits, e=6557):
        p = self.find_prime_number(random.randint(2 ** (col_bits // 2), 2 ** ((col_bits//2) + 1)))
        #print('get a half')
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


    def rand(self, a, b):  # для теста ферма нужно, что бы числа не повторялись, тут я это проверяю
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
        if n % 10 != 5:  # простые числа оканчиваются только на эти цифры
            if n <= self.prime_numbers[-1]:  # до этого значения числа я высчитал, так что по чему бы просто не проверить их на наличие в файле
                for i in self.prime_numbers:
                    if n < int(i):
                        return False
                    elif n == int(i):
                        return True
            for i in range(50):  # это как раз тест ферма очень хотелось бы увидеть его доказательство. 100 - это константа взятая из статьи в хабре в её правильности я не уверен
                a = self.rand(5, n - 2)
                if (math.gcd(a, n) != 1):  # ну для теста ферма числа должны быть взаимно простые
                    return False  # простые числа должны быть взаимно простыми со всеми
                if (pow(a, n - 1, n) != 1):  # сам тест
                    return False
            #  print("end of ferma test")
            for i in self.prime_numbers[:500]:
                if n % int(i) == 0:  # тут я пытаюсь отсеить числа карлмайка они не простые и удолетворяют тесту ферма. написано про них здесь https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%BE_%D0%9A%D0%B0%D1%80%D0%BC%D0%B0%D0%B9%D0%BA%D0%BB%D0%B0
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
            if self.is_prime_number(i + 1):  # тут я иду по спиралям в которых содержатся простые числа
                return i + 1
            elif self.is_prime_number(i + 5):
                return i + 5
            i += 6

    def factorization(self, n):  # алгоритм для факторизации, это один из способов проверки числа на простоту
        if n % 2 == 0:
            print(2)
        for i in range(3, int(math.sqrt(n)), 2):
            if n % i == 0:
                return i



def main():
    my_RSA = RSA_Tool()
    normal_people_RSA = rsa

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
        my_time_small_keys.append(t2-t1)
    for i in tqdm(range(100)):
        t1 = time.time()
        normal_people_RSA.newkeys(256)
        t2 = time.time()
        normal_time_small_keys.append(t2-t1)


    my_time_average_keys = []
    normal_time_average_keys = []
    for i in tqdm(range(100)):
        t1 = time.time()
        my_RSA.get_bit_keys(1024)
        t2 = time.time()
        my_time_average_keys.append(t2-t1)
    for i in tqdm(range(100)):
        t1 = time.time()
        normal_people_RSA.newkeys(1024)
        t2 = time.time()
        normal_time_average_keys.append(t2-t1)


    my_time_big_keys = []
    normal_time_big_keys = []
    for i in tqdm(range(100)):
        t1 = time.time()
        my_RSA.get_bit_keys(4096)
        t2 = time.time()
        my_time_big_keys.append(t2 - t1)
    for i in tqdm(range(100)):
        t1 = time.time()
        normal_people_RSA.newkeys(4096)
        t2 = time.time()
        normal_time_big_keys.append(t2 - t1)

    print("all data for small numbers(256bit)")
    print("my median is " + str(numpy.mean(my_time_small_keys)))
    print("normal median is " + str(numpy.mean(normal_time_small_keys)))
    plt.plot(numpy.array(range(100), int), numpy.array(my_time_small_keys, float))
    plt.plot(numpy.array(range(100), int), numpy.array(normal_time_small_keys, float))
    plt.grid(True)
    plt.show()
    plt.savefig('small_nums.png')

    print("all data for average numbers(1024bit)")
    print("my median is " + str(numpy.mean(my_time_average_keys)))
    print("normal median is " + str(numpy.mean(normal_time_average_keys)))
    plt.plot(numpy.array(range(100), int), numpy.array(my_time_average_keys, float))
    plt.plot(numpy.array(range(100), int), numpy.array(normal_time_average_keys, float))
    plt.show()
    plt.savefig('average_nums.png')

    print("all data for big numbers(4096bit)")
    print("my median is " + str(numpy.mean(my_time_big_keys)))
    print("normal median is" + str(numpy.mean(normal_time_big_keys)))
    plt.plot(numpy.array(range(100), int), numpy.array(my_time_big_keys, float))
    plt.plot(numpy.array(range(100), int), numpy.array(normal_time_big_keys, float))
    plt.show()
    plt.savefig('big_nums.png')










if __name__ == '__main__':
    main()


