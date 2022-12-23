def game_v1(one, two):
    if one not in ["A", "B", "C"] or two not in ["X", "Y", "Z"]:
        print("Error: ill-formed input.")
        return -1
    else:
        #player one plays "rock" 
        if one == "A" and two == "X":
            return 4, 4
        if one == "A" and two == "Y":
            return 1, 8
        if one == "A" and two == "Z":
            return 7, 3

        #player one plays "paper"
        if one == "B" and two == "X":
            return 8, 1
        if one == "B" and two == "Y":
            return 5, 5
        if one == "B" and two == "Z":
            return 2, 9


        #player one plays "scissors" 
        if one == "C" and two == "X":
            return 3, 7
        if one == "C" and two == "Y":
            return 9, 2
        if one == "C" and two == "Z":
            return 6, 6

def game_v2(one, two):
    if one not in ["A", "B", "C"] or two not in ["X", "Y", "Z"]:
        print("Error: ill-formed input.")
        return -1
    else:
        #player one plays "rock" 
        if one == "A" and two == "X":
            return 7, 3
        if one == "A" and two == "Y":
            return 4, 4
        if one == "A" and two == "Z":
            return 1, 8

        #player one plays "paper"
        if one == "B" and two == "X":
            return 8, 1
        if one == "B" and two == "Y":
            return 5, 5
        if one == "B" and two == "Z":
            return 2, 9


        #player one plays "scissors" 
        if one == "C" and two == "X":
            return 9, 2
        if one == "C" and two == "Y":
            return 6, 6
        if one == "C" and two == "Z":
            return 3, 7

file = "/home/beatrice/AoC_2022/data/2.txt"

with open(file) as f:
    lines = f.readlines()
    one_score = 0
    two_score = 0
    for line in lines:
        one, two = line[0], line[2]
        two_score += game_v2(one, two)[1]
    print(two_score)


        
