import random

cour = 0
sum = 13
NumC = 4
val = [0, 0, 0, 0]
tries = 0
check = []
num_cz =0
cannot = []




while cour < 100000:
    cour += 1
    for x in range(NumC):
        val[x] = random.randint(0, 9)
        for y in range(len(cannot)):
            if val[x] != cannot[y]:
                val[x].append(cannot)
                break
            else:
                for z in range(len(cannot)):
                    val[x] = random.randint(0, 9)
                    if val[x] != cannot[z]:
                        val[x].append(cannot)
                        break
    val.sort()
    for x in range(len(check)):
        if check[x] == val:
            num_cz += 1
            break
    if val[0] + val[1] + val[2] + val[3] == sum:
        print(val)
        tries += 1
        check.append (val)
print(tries)
print(num_cz)
