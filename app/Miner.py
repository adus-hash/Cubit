import hashlib
import random
import os
import time

print("                                           ============================")
print("                                                     Cubit Miner")
print("                                           ============================ \n")
print("                                                    1) Log In")
print("                                                     2) Exit")

working_path = os.getcwd()
users_path = working_path + "\Pouzivatelia"
transaction_path = working_path + "\Transactions"
blockchain_path = working_path + "\Blockchain"

if not os.path.exists(blockchain_path):
    os.mkdir(blockchain_path)

run = True
menu = True
logged = False

pocet_tr = 0
transactions = []
nonce = 0
previous_hash = 0

while run:
    while menu:
        inp = input()
        if inp == "1":
            id = input("\nID: ")

            if os.path.exists(users_path + "\\" + id + ".txt"):
                with open(users_path + "\\" + id + ".txt", "r") as user_file:
                    is_miner = user_file.readlines()[6][:-1]
                    if is_miner == "1":

                        print("\n                                           ============================")
                        print("                                                     Loged In")
                        print("                                                 Mining started")
                        print("                                           ============================ \n")

                        menu = False
                        logged = True
                    else:
                        print("\n                                           ============================")
                        print("                                                You are not a miner")
                        print("                                           ============================ \n")

            else:
                print("\nLoggin failed!")

    while logged:
        str_tr = ""
        transactions = []

        if len(os.listdir(os.path.join(blockchain_path))) != 0:
            with open(blockchain_path + "\\" + "block_" + str(len(os.listdir(os.path.join(blockchain_path))) - 1) + ".txt", "r") as previous_block:
                previous_hash = previous_block.readlines()[1]

        while len(transactions) < 10:
            time.sleep(4)
            with open(os.path.join(transaction_path, "transactions.txt"), "r") as transaction_file:
                transactions = transaction_file.readlines()


                if len(transactions) >= 10:
                    with open(transaction_path + "\\" + "transactions.txt", "w") as new_transaction_file:
                        new_transaction_file.writelines(transactions[10:])
                        for i in transactions[:10]:
                            str_tr += str(i[:-1]) + " "


        while len(transactions) >= 10:
            finding_letters = hashlib.sha256(random.randint(90000000000, 9000000000000).to_bytes(16, 'little', signed=False) + str_tr.encode()).hexdigest()[0:6]

                                    # nonce                                  # transakcie       # hash z predchadzajuceho bloku
            while hashlib.sha256(nonce.to_bytes(16, 'little', signed=False) + str_tr.encode() + str(previous_hash).encode()).hexdigest()[0:6] != finding_letters:
                nonce += 1

            with open(users_path + "\\" + id + ".txt", "r") as user_file:
                user_lines = user_file.readlines()

            with open(users_path + "\\" + id + ".txt", "w") as user_file:
                user_lines[1] = str(int(user_lines[1]) + 3) + "\n"
                user_file.writelines(user_lines)


            if len(os.listdir(os.path.join(blockchain_path))) == 0:
                with open(blockchain_path + "\\" + "block_0.txt", "w") as first_block:
                    first_block.write("0\n")
                    first_block.write(hashlib.sha256(nonce.to_bytes(16, 'little', signed=False) + str_tr.encode() + str(previous_hash).encode()).hexdigest() + "\n")
                    first_block.write(str(nonce) + "\n")
                    first_block.writelines(transactions[:10])

            else:
                with open(blockchain_path + "\\" + "block_" + str(len(os.listdir(os.path.join(blockchain_path)))) +".txt", "w") as block:
                    block.write(previous_hash)
                    block.write(hashlib.sha256(nonce.to_bytes(16, 'little', signed=False) + str_tr.encode() + str(previous_hash).encode()).hexdigest() + "\n")
                    block.write(str(nonce) + "\n")
                    block.writelines(transactions[:10])

            print("New block were created []")
            print(nonce, str_tr, hashlib.sha256(nonce.to_bytes(16, 'little', signed=False) + str_tr.encode() + str(previous_hash).encode()).hexdigest(), finding_letters)
            transactions = []
            nonce = 0

