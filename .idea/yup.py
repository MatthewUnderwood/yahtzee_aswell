import random

dice = [0,0,0,0,0]
dicecount = [0,0,0,0,0]
scorecare = [0,0,0,0,0,0,35,0,0,0,0,0,0,0,0]


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

def three_of_a_kind_check(dicecount):
    if 3 in dicecount:
        return "true"
    else:
        return "false"

def check_for_large_striaght(dice_rolls):
    if 1 in dice_rolls and 2 in dice_rolls and 3 in dice_rolls and 4 in dice_rolls and 5 in dice_rolls:
        return "true"
    elif 6 in dice_rolls and 2 in dice_rolls and 3 in dice_rolls and 4 in dice_rolls and 5 in dice_rolls:
        return "true"
    else:
        return "false"

def check_for_small_striaght(dice_rolls):
    if 1 in dice_rolls and 2 in dice_rolls and 3 in dice_rolls and 4 in dice_rolls:
        return "true"
    elif 2 in dice_rolls and 3 in dice_rolls and 4 in dice_rolls and 5 in dice_rolls:
        return "true"
    elif 6 in dice_rolls and 3 in dice_rolls and 4 in dice_rolls and 5 in dice_rolls:
        return "true"
    else:
        return "false"

def reroll_dice(num):
    for idx, val in enumerate(dice):
        if idx + 1 == num:
            dice[idx] = random.randrange(1,6)
    return dice


for idx, val in enumerate(dice):
    dice[idx] = random.randrange(1,6)
    print (dice)

for idx, val in enumerate(dice):
    dicecount[idx] = dice.count(idx + 1)


user_amount_of_rerolls = int(input("how many dice would you like to reroll"))

for  i in range(user_amount_of_rerolls):
    user_input = int(input("which dice would you like to reroll"))
    reroll_dice(user_input)

print (dice)
# print (yahtzee_check(dicecount))
# print (four_of_a_kind_check(dicecount))
# print (three_of_a_kind_check(dice))
# print (full_house_check(dicecount))
# print (check_for_large_striaght(dice))
# print (check_for_small_striaght(dice))