file = "/home/beatrice/AoC_2022/data/1.txt"

with open(file) as f:
    lines = f.readlines()

    elflist = list()

    tempelf = 0
    for line in lines:
        if line in ['\n', '\r']:
            elflist.append(tempelf)
            tempelf = 0
        else:
            tempelf = tempelf + int(line)

    elflist.sort(reverse=True)
    #print(elflist)
    print(elflist[0]+elflist[1]+elflist[2])

