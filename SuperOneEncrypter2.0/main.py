import time
import matplotlib.pyplot as plt
from tqdm import tqdm
import rsa
import numpy.random
import RSA_tool as my_RSA


def test():
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
    plt.plot(numpy.array(range(100)), numpy.array(my_time_small_keys, float), label='предложенный подход')
    plt.plot(numpy.array(range(100)), numpy.array(normal_time_small_keys, float), label='стандартный подход')
    plt.legend(prop={"size": 14})
    plt.xlabel('итерация', fontsize=14)
    plt.ylabel('время, с', fontsize=14)
    plt.grid(True)
    plt.savefig('small_nums.png')
    plt.show()

    print("all data for average numbers(1024bit)")
    print("my median is " + str(numpy.mean(my_time_average_keys)))
    print("normal median is " + str(numpy.mean(normal_time_average_keys)))
    plt.plot(numpy.array(range(100), int), numpy.array(my_time_average_keys, float), label='предложенный подход')
    plt.plot(numpy.array(range(100), int), numpy.array(normal_time_average_keys, float), label='стандартный подход')
    plt.legend(prop={"size": 14})
    plt.xlabel('итерация', fontsize=14)
    plt.ylabel('время, с', fontsize=14)
    plt.grid(True)
    plt.savefig('average_nums.png')
    plt.show()

    print("all data for big numbers(4096bit)")
    print("my median is " + str(numpy.mean(my_time_big_keys)))
    print("normal median is" + str(numpy.mean(normal_time_big_keys)))
    plt.plot(numpy.array(range(100), int), numpy.array(my_time_big_keys, float), label='предложенный подход')
    plt.plot(numpy.array(range(100), int), numpy.array(normal_time_big_keys, float), label='стандартный подход')
    plt.legend(prop={"size": 14})
    plt.xlabel('итерация', fontsize=14)
    plt.ylabel('время, с', fontsize=14)
    plt.grid(True)
    plt.savefig('big_nums.png')
    plt.show()


def main():
    test()
    # e, d, n = my_RSA.get_bit_keys(256)
    # m = 'я люблю вкусный чай'
    # c = my_RSA.block_encrypt(m, e, n)
    # m = my_RSA.block_decrypt(c, d, n)
    # print(m)


if __name__ == '__main__':
    main()