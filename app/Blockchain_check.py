import hashlib
import os

working_path = os.getcwd()
blockchain_path = working_path + "\Blockchain"

while True:
    if len(os.listdir(os.path.join(blockchain_path))) != 1:
        with open(blockchain_path + "\\" + "block_" + str(len(os.listdir(os.path.join(blockchain_path))) - 2) + ".txt", "r") as previous_block:
            previous_hash = " " + previous_block.readlines()[1]


        with open(blockchain_path + "\\" + "block_" + str(len(os.listdir(os.path.join(blockchain_path))) - 1) +".txt", "r") as block:
            block_lines = block.readlines()
            nonce = int(block_lines[2])               # program pre kontrolu ci svsetko pasuje v blockchain
            current_hash = block_lines[1][:-1]

            tr = [i for i in block_lines[3:]]

            str_tr = ""
            for i in tr:
                str_tr += str(i[:-1]) + " "

# takto by to malo vyzerat
#         str_tr = "aaaab0010aaaaa aaaaa0011aaaab aaaaa0012aaaab aaaab0013aaaaa aaaaa0014aaaab aaaab0015aaaaa aaaab0016aaaaa aaaab0017aaaaa aaaaa0018aaaab aaaaa0019aaaab"
#         previous_hash = " d370a3b8b0a9c96268f5235fcb13c659c02b80b4c5b51c1f9b0a3c638b902632\n"


        if hashlib.sha256(nonce.to_bytes(16, 'little', signed=False) + str_tr[:-1].encode() + previous_hash.encode()).hexdigest() != current_hash:
            os.remove(blockchain_path + "\\" + "block_" + str(len(os.listdir(os.path.join(blockchain_path))) - 1) +".txt")
