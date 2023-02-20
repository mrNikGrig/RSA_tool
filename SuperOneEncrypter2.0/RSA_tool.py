import random
import prime_numbers
import encryption


def get_bit_keys(col_bits, e=65577):
    p = prime_numbers.find_prime_number(random.randint(2 ** (col_bits // 2), 2 ** ((col_bits // 2) + 1)))
    q = prime_numbers.find_prime_number(random.randint(2 ** (col_bits // 2) - 1, 2 ** (col_bits // 2)))
    return encryption.gen_keys(p, q, e)


def block_encrypt(m, e, n):
    max_len_block = len(str(n)) - 2
    block = ''
    arr_blocks = []
    for i in m:
        str_i = str(ord(i))
        while len(str_i) < 4:
            str_i = '0' + str_i
        if len(block + str_i) <= max_len_block:
            block += str_i
        else:
            arr_blocks.append('1' + block)
            block = str_i
    arr_blocks.append('1' + block)
    # print(*arr_blocks)
    for i in range(len(arr_blocks)):
        arr_blocks[i] = pow(int(arr_blocks[i]), e, n)
    return arr_blocks


def block_decrypt(c, d, n):
    for i in range(len(c)):
        c[i] = pow(int(c[i]), d, n)
    s = ''
    for i in c:
        tmp = str(i)[1:]
        for i in range(0, len(tmp), 4):
            s += chr(int((tmp[i] + tmp[i + 1] + tmp[i + 2] + tmp[i + 3])))
    return s


