import random

dice = [0,0,0,0,0]
dicecount = [0,0,0,0,0]

def full_house_check(dice):
    if 3 in dicecount and 2 in dicecount:
        return "true"
    else:
        return "false"

def yahtzee_check(dice):
    if 5 in dicecount:
        return "true"
    else:
        return "false"

for idx, val in enumerate(dice):
    dice[idx] = random.randrange(1,6)
    print (dice)

for idx, val in enumerate(dice):
    dicecount[idx] = dice.count(idx + 1)


print (yahtzee_check(dice))