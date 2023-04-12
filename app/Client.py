from math import sqrt
from random import randint
from hashlib import md5, sha256
import os


def prime_nums(arr):
    n = len(arr)
    prime_nums = []

    for i in range(1, len(arr)-1):
        j = 0
        if arr[0] < sqrt(n):
            prime = arr[0]
            arr.pop(0)


            while j < len(arr):
                if arr[j] % prime == 0:
                    arr.remove(arr[j])
                    j -= 1
                j += 1
            prime_nums.append(prime)

        else:
            prime = arr[0]
            prime_nums.append(prime)
            arr.pop(0)

            while j < len(arr):
                if arr[j] % prime == 0:
                    arr.remove(arr[j])
                    j -= 1
                j += 1
            prime_nums.extend(arr)

            return prime_nums

def nsd(a, b):
    while a != b:
        if a > b :
            a -= b
        else:
            b -= a
    return a

def choose_e(N):
    while True:
        random_e = randint(N // 3, N // 2)

        if nsd(random_e, N) == 1:
            return random_e

def create_inverse(e, N):
    c1, c2, c3 = N, 0, 0
    v1, v2, v3 = e, 1, N - e * (N // e)

    while c3 != 1:
        q = v3
        v1, v2, v3, c1, c2, c3 = q, c2 + (v2 * -(c1 // v1)), v1 - q * (v1 // q), v1, v2, v3

    while str(v2)[0] == "-":
        v2 += N

    return v2

def encoding(plain_txt, public_key):
    encode = []
    for i in plain_txt:
        encode.append((ord(str(i))**public_key[0]) % public_key[1])

    return encode

def decoding(cipher_txt, private_key):
    decode = ""
    for i in cipher_txt:
        decode += chr((i**private_key[0]) % private_key[1])
    return decode


def new_client(magic_num):
    id = get_id()
    name = md5(b'VekJe' + str(magic_num).encode() + id.encode()).digest().hex()
    amount = 0

    prime_numbers = prime_nums([i for i in range(2, 300)]) # randint(520, 650)

    p = prime_numbers[randint(len(prime_numbers) - 3, len(prime_numbers) - 1)]
    q = prime_numbers[randint(len(prime_numbers) - 6, len(prime_numbers) - 4)]

    n = p * q
    N = (p - 1) * (q - 1)

    public_key = (choose_e(N), n)
    private_key = (create_inverse(public_key[0], N), n)

    working_path = os.getcwd()
    user_path = working_path + "\Pouzivatelia"
    if not os.path.exists(user_path):
        os.mkdir(user_path)

    with open(os.path.join(user_path, str(id) + ".txt"), "w") as file:
        file.write(name + "\n")
        file.write(str(amount) + "\n")
        file.write(str(private_key[0]) + "\n")
        file.write(str(private_key[1]) + "\n")
        file.write(str(public_key[0]) + "\n")
        file.write(str(public_key[1]) + "\n")
        file.write("0\n")

    return id


def get_id():
    lines = []
    with open("wIDs.txt", "r") as file:
        lines = file.readlines()

    new_id = lines[0][:5]

    with open("wIDs.txt", "w") as new_file:
        for i in lines[1:]:
            new_file.write(i)

    return new_id

def make_transaction(sender_id, recipient_id, amount, private_key):
    transaction = str(sender_id)
    while len(transaction + str(amount)) < 9:
        transaction += "0"

    transaction += str(amount) + str(recipient_id)
    original_transaction = transaction


    return original_transaction, encoding(sha256(transaction.encode()).digest().hex(), private_key)

def verification(original_transaction, encoded_transaction, public_key):
    return sha256(original_transaction.encode()).digest().hex() == decoding(encoded_transaction, public_key)


#mess = make_transaction("aaaaa", "aaaab", 9999, (347, 1333))
#print(mess == encoding(sha256(original_transaction.encode()).digest().hex(), private_key))
#new_client(16)



# prime_numbers = prime_nums([i for i in range(2, 600)])
# p = prime_numbers[randint(len(prime_numbers) - 3, len(prime_numbers) - 1)]
# q = prime_numbers[randint(len(prime_numbers) - 6, len(prime_numbers) - 4)]
#
# n = p * q
# N = (p - 1) * (q - 1)
#
# e = choose_e(N)
# d = create_inverse(e, N)


# c = client()
#
# mess = "ad5th6j0005jg4nuj"
# cipher_txt = encoding(mess, c.public_key[0], c.public_key[1])
#
# print(mess == decoding(cipher_txt, c.private_key[0], c.private_key[1]))