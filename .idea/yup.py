import random

dice = [0,0,0,0,0]
dicecount = [0,0,0,0,0,0]
scorecare = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
rolls_left = 13


def full_house_check(dicecount):
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
    if 4 in dicecount or yahtzee_check(dicecount) == "true":
        return "true"
    else:
        return "false"

def three_of_a_kind_check(dicecount):
    if 3 in dicecount or four_of_a_kind_check(dicecount) == "true":
        return "true"
    else:
        return "false"

def check_for_large_striaght(dice):
    if 1 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice:
        return "true"
    elif 6 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice:
        return "true"
    else:
        return "false"

def check_for_small_striaght(dice):
    if 1 in dice and 2 in dice and 3 in dice and 4 in dice:
        return "true"
    elif 2 in dice and 3 in dice and 4 in dice and 5 in dice:
        return "true"
    elif 6 in dice and 3 in dice and 4 in dice and 5 in dice:
        return "true"
    else:
        return "false"

def reroll_dice(num):
    for idx, val in enumerate(dice):
        if idx + 1 == num:
            dice[idx] = random.randrange(1,6)
    return dice

def count_dice(dice, dicecount):
    for idx, val in enumerate(dicecount):
        dicecount[idx] = dice.count(idx + 1)

while rolls_left != 0:
    for idx, val in enumerate(dice):
        dice[idx] = random.randrange(1,6)

    print ("this is the inital roll\n", dice)
    user_amount_of_rerolls = int(input("how many dice would you like to reroll"))

    for  i in range(user_amount_of_rerolls):
        user_input = int(input("which dice would you like to reroll"))
        reroll_dice(user_input)

    print (dice)

    user_amount_of_rerolls = int(input("how many dice would you like to reroll"))

    for  i in range(user_amount_of_rerolls):
        user_input = int(input("which dice would you like to reroll"))
        reroll_dice(user_input)

    print (dice)
    print (dicecount)
    count_dice(dice, dicecount)
    print (dicecount)
    rolls_left = rolls_left - 1

    print ("yahtzee_check:           ", yahtzee_check(dicecount))
    print ("four_of_a_kind_check:    ", four_of_a_kind_check(dicecount))
    print ("three_of_a_kind_check:   ", three_of_a_kind_check(dicecount))
    print ("full_house_check:        ", full_house_check(dicecount))
    print ("check_for_large_striaght:", check_for_large_striaght(dice))
    print ("check_for_small_striaght:",  check_for_small_striaght(dice))