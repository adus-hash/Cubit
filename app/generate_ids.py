id = ["0", "0", "0", "0", "0"]
with open("wIDs.txt", "w") as file:
    for i in range(97, 123):
        id[0] = chr(i)
        for j in range(97, 123):
            id[1] = chr(j)
            for k in range(97, 123):
                id[2] = chr(k)
                for l in range(97, 123):
                    id[3] = chr(l)
                    for n in range(97, 123):
                        id[4] = chr(n)
                        file.write("".join(id) + "\n")