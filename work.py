q_list = [
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
]

g_list = [
    2,
    5,
    2,
    6,
    3,
    3,
    2,
    3,
    2,
    2,
    6,
    5,
    2,
    5,
    2,
    2,
    2,
    19,
    5,
    2,
    3,
    2,
    3,
    2,
    6,
    3,
    7,
    7,
    6,
]

import random


def random_int(num):
    return random.randint(1, num - 1)


def calculate(g, Xa, q):
    """
    计算公钥
    输入: g: q的本原根 ,Xa:私钥,q:素数,具体公式：(g^Xa) mod q
    输出:公钥Ya
    """
    result = 1
    while Xa > 0:
        if Xa & 1 == 1:
            result = (result * g) % q
        g = (g * g) % q
        Xa >>= 1
    return result


for q, g in zip(q_list, g_list):
    X_A = random.randint(1, q - 1)
    X_B = random.randint(1, q - 1)

    print("素数 q= ", q)
    print("本原根 g= ", g)
    print("A获取的私钥 Xa=", X_A)
    print("B获取的私钥 Xb=", X_B)

    Y_A = calculate(g, X_A, q)
    Y_B = calculate(g, X_B, q)
    print("A计算得到的公钥 Ya为：", Y_A)
    print("B计算得到的公钥 Yb为：", Y_B)

    print("------X_A与B交换公钥------")
    key_A = calculate(Y_B, X_A, q)
    key_B = calculate(Y_A, X_B, q)
    print("A计算得到的key为：", key_A)
    print("B计算得到的key为：", key_B)

    print("\n**************************")
