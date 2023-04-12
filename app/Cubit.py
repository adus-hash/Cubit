from Client import *

print("                                           ============================")
print("                                                    Cubit Client")
print("                                           ============================ \n")
print("                                                    1) Log In")
print("                                                  2) New Acount")
print("                                                    3) Exit")

working_path = os.getcwd()
users_path = working_path + "\Pouzivatelia"
transaction_path = working_path + "\Transactions"
blockchain_path = working_path + "\Blockchain"
run = True
menu = True
logged = False

user_id = ""
user_name = ""
user_amount = 0
user_public_key = None
user_private_key = None
is_miner = 0

while run:
    while menu:
        inp = input()
        if inp == "1":
            id = input("\nID: ")

            if os.path.exists(users_path + "\\" + id + ".txt"):
                with open(os.path.join(users_path + "\\" + id + ".txt")) as file:
                    lines = file.readlines()

                    user_id = id
                    user_name = lines[0][:-1]
                    user_amount = int(lines[1])
                    user_private_key = (int(lines[2][:-1]), int(lines[3][:-1]))
                    user_public_key = (int(lines[4][:-1]), int(lines[5][:-1]))
                    is_miner = str(lines[6])
                    try:
                        users_transaction_send = str(lines[7])
                    except:
                        pass

                    print("\n                                           ============================")
                    print("                                                     Loged In")
                    print("                                           ============================ \n")
                    print("                                                1) Make transaction")
                    print("                                                2) Verify to minig")
                    print("                                                3) Info about acount")
                    print("                                                     4) Log out")

                    menu = False
                    logged = True

            else:
                print("\nLoggin failed!")


        elif inp == "2":
            inp = input("\n Enter your age to create new acount: ")
            id = new_client(inp)


            if os.path.exists(users_path + "\\" + id + ".txt"):
                with open(os.path.join(users_path + "\\" + id + ".txt"), "r") as file:
                    lines = file.readlines()

                    user_id = id
                    user_name = lines[0][:-2]
                    user_amount = int(lines[1])
                    user_private_key = (int(lines[2][:-1]), int(lines[3][:-1]))
                    user_public_key = (int(lines[4][:-1]), int(lines[5]))
                    is_miner = str(lines[6])
            print("\n                                           ============================")
            print("                                                  Acount createed")
            print("                                                     Loged In")
            print("                                           ============================ \n")
            print("                                                1) Make transaction")
            print("                                                2) Verify to minig")
            print("                                                3) Info about acount")
            print("                                                     4) Log out")

            menu = False
            logged = True

        elif inp == "3":
            run = False
            menu = False

        else:
            print("Invalid input, try again:\n")

    while logged:
        with open(os.path.join(users_path + "\\" + user_id + ".txt"), "r") as file:
            user_lines = file.readlines()  # z tychto lines potrebujem iba transakcie, tie lines su od prijimatela

            user_name = user_lines[0][:-1]
            user_amount = int(user_lines[1])
            user_private_key = (int(user_lines[2][:-1]), int(user_lines[3][:-1]))
            user_public_key = (int(user_lines[4][:-1]), int(user_lines[5][:-1]))
            is_miner = str(user_lines[6])
            try:
                transaction_check_list = user_lines[7]
            except:
                transaction_check_list = 0

            if transaction_check_list != 0:
                transaction_check_list = transaction_check_list.split(";")
                formed_tr = []

                for i in range(len(transaction_check_list)-1):
                    formed_tr.append(transaction_check_list[i].split(" "))

                while len(formed_tr) > 0:
                    tr = formed_tr[0][0]
                    encoded_tr = [int(i) for i in formed_tr[0][1:]]

                    encoded_tr_str = ""
                    for i in encoded_tr:               # toto mi robi z typu list na typ str, lebo transakcie su v liste a do file nejde pisat listy ale iba str preto sa to tu konvertuje
                        encoded_tr_str += str(i) + " "

                    if user_id == tr[9:]:
                        with open(os.path.join(users_path + "\\" + tr[:5] + ".txt"), "r") as file:
                            lines = file.readlines()  # potrebjem ziskat mnozstvo Cubitov kolko ma odosielatel aby som ich prepisal

                        if verification(tr, encoded_tr, (int(lines[4][:-1]), int(lines[5][:-1]))) == True and int(lines[1]) - int(tr[5:9]) >= 0:
                            lines[1] = str(int(lines[1]) - int(tr[5:9])) + "\n"         # vymena Cubitov
                            user_amount += int(tr[5:9])

                            with open(os.path.join(users_path + "\\" + tr[:5] + ".txt"), "w") as file:
                                for i in lines:     # pises odosielatelovi
                                    file.write(i)

                            if not os.path.exists(transaction_path):
                                os.mkdir(transaction_path)


                            if os.path.exists(transaction_path + "\\" + "transactions" + ".txt"):
                                with open(transaction_path + "\\" + "transactions" + ".txt", "a") as tr_file:
                                    tr_file.write(tr + "\n")        # pises dalsie transakcie ktore uz prebehli

                            else:
                                with open(transaction_path + "\\" + "transactions" + ".txt", "w") as tr_file:
                                    tr_file.write(tr + "\n")

                    formed_tr.pop(0)

# dorobit aby sa akutualizovalo kolko mam love ked stlacim 3, aby som sa za kazdym nemusel odhlasovat a prihlasovat
                with open(os.path.join(users_path + "\\" + user_id + ".txt"), "w") as file:
                    file.write(user_name + "\n")
                    file.write(str(user_amount) + "\n")
                    file.write(str(user_private_key[0]) + "\n")
                    file.write(str(user_private_key[1]) + "\n")
                    file.write(str(user_public_key[0]) + "\n")
                    file.write(str(user_public_key[1]) + "\n")
                    file.write(str(is_miner))

        inp = input()

        with open(os.path.join(users_path + "\\" + user_id + ".txt"), "r") as file:
            user_lines = file.readlines()  # z tychto lines potrebujem iba transakcie, tie lines su od prijimatela

            user_name = user_lines[0][:-1]
            user_amount = int(user_lines[1])
            user_private_key = (int(user_lines[2][:-1]), int(user_lines[3][:-1]))
            user_public_key = (int(user_lines[4][:-1]), int(user_lines[5][:-1]))
            is_miner = str(user_lines[6])
            try:
                transaction_check_list = user_lines[7]
            except:
                transaction_check_list = 0

            if transaction_check_list != 0:
                transaction_check_list = transaction_check_list.split(";")
                formed_tr = []

                for i in range(len(transaction_check_list) - 1):
                    formed_tr.append(transaction_check_list[i].split(" "))

                while len(formed_tr) > 0:
                    tr = formed_tr[0][0]
                    encoded_tr = [int(i) for i in formed_tr[0][1:]]

                    encoded_tr_str = ""
                    for i in encoded_tr:  # toto mi robi z typu list na typ str, lebo transakcie su v liste a do file nejde pisat listy ale iba str preto sa to tu konvertuje
                        encoded_tr_str += str(i) + " "

                    if user_id == tr[9:]:
                        with open(os.path.join(users_path + "\\" + tr[:5] + ".txt"), "r") as file:
                            lines = file.readlines()  # potrebjem ziskat mnozstvo Cubitov kolko ma odosielatel aby som ich prepisal

                        if verification(tr, encoded_tr, (int(lines[4][:-1]), int(lines[5][:-1]))) == True and int(lines[1]) - int(tr[5:9]) >= 0:
                            lines[1] = str(int(lines[1]) - int(tr[5:9])) + "\n"  # vymena Cubitov
                            user_amount += int(tr[5:9])

                            with open(os.path.join(users_path + "\\" + tr[:5] + ".txt"), "w") as file:
                                for i in lines:  # pises odosielatelovi
                                    file.write(i)

                            if not os.path.exists(transaction_path):
                                os.mkdir(transaction_path)


                            if os.path.exists(transaction_path + "\\" + "transactions" + ".txt"):
                                with open(transaction_path + "\\" + "transactions" + ".txt", "a") as tr_file:
                                    tr_file.write(tr + "\n")  # pises dalsie transakcie ktore uz prebehli

                            else:
                                with open(transaction_path + "\\" + "transactions" + ".txt", "w") as tr_file:
                                    tr_file.write(tr + "\n")
                    formed_tr.pop(0)

                with open(os.path.join(users_path + "\\" + user_id + ".txt"), "w") as file:
                    file.write(user_name + "\n")
                    file.write(str(user_amount) + "\n")
                    file.write(str(user_private_key[0]) + "\n")
                    file.write(str(user_private_key[1]) + "\n")
                    file.write(str(user_public_key[0]) + "\n")
                    file.write(str(user_public_key[1]) + "\n")
                    file.write(str(is_miner))

        if inp == "1":
            destination_id = input("Type ID where you wuold like to send yours Cubits: ")

            while not os.path.exists(users_path + "\\" + destination_id + ".txt") or destination_id == user_id:
                destination_id = input("Error occurs, try again: ")

            amount_to_send = input("Type how much Cubits would you like to send: ")

            while int(amount_to_send) > 9999 or user_amount - int(amount_to_send) < 0:
                amount_to_send = input("Error occurs, try again: ")

            with open(os.path.join(users_path + "\\" + destination_id + ".txt"), "r") as file:
                des_lines = file.readlines()        # des_lines stands for destination_lines su to lajni prijimatela

            #print(des_lines)
            #recipient_private_key = (int(des_lines[2][:-1]), int(des_lines[3][:-1]))
            original_transaction, encoded_transaction = make_transaction(user_id, destination_id, amount_to_send, user_private_key)

            encoded_transaction_str = ""
            for i in encoded_transaction:
                encoded_transaction_str += " " + str(i)


            with open(os.path.join(users_path + "\\" + user_id + ".txt"), "w") as file:
                file.write(user_name + "\n")
                file.write(str(user_amount) + "\n")
                file.write(str(user_private_key[0]) + "\n")
                file.write(str(user_private_key[1]) + "\n")
                file.write(str(user_public_key[0]) + "\n")
                file.write(str(user_public_key[1]) + "\n")
                file.write(str(is_miner))
                try:
                    file.write(users_transaction_send)      # zapisuje uz zapisane transakcie
                except:
                    pass

                file.write(original_transaction + encoded_transaction_str + ";")     # zapisuje novu transakciu

                                                                                        # des_file stands for destination_file
            with open(os.path.join(users_path + "\\" + destination_id + ".txt"), "w") as des_file:
                for i in des_lines:
                    des_file.write(i)

                des_file.write(original_transaction + encoded_transaction_str + ";")


        elif inp == "2":
            is_miner = "1\n"
            with open(os.path.join(users_path + "\\" + user_id + ".txt"), "w") as file:
                file.write(user_name + "\n")
                file.write(str(user_amount) + "\n")
                file.write(str(user_private_key[0]) + "\n")
                file.write(str(user_private_key[1]) + "\n")
                file.write(str(user_public_key[0]) + "\n")
                file.write(str(user_public_key[1]) + "\n")
                file.write(str(is_miner))
                try:
                    file.write(users_transaction_send)      # zapisuje uz zapisane transakcie
                except:
                    pass

            print("\n                                           ============================")
            print(f"                                            Now you can mine the Cubit")
            print("                                           ============================ \n")

        elif inp == "3":
            print("\n                                           ============================")
            print(f"                                                You have {user_amount} Cubits")
            print("                                           ============================ \n")


        elif inp == "4":
            menu = True
            logged = False
            print("\n                                           ============================")
            print(f"                                                    Logged out")
            print("                                           ============================ \n")

        else:
            print("Invalid input, try again:\n")
