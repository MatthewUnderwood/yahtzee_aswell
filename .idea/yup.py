import random

dice = [1,2,1,1,1]
dicecount = [0,0,0,0,0]

def full_house_check(dice):
    if 3 in dicecount and 2 in dicecount:
        return "true"
    else:
        return "false"

def yahtzee_check(dicecount):
    if 5 in dicecount:
        return "true"
    else:
        return "false"

def four_of_a_kind_check(dicecount):
    if 4 in dicecount:
        return "true"
    else:
        return "false"


# for idx, val in enumerate(dice):
#     dice[idx] = random.randrange(1,6)
#     print (dice)

for idx, val in enumerate(dice):
    dicecount[idx] = dice.count(idx + 1)


print (four_of_a_kind_check(dicecount))