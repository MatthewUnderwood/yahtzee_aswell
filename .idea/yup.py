import random

dice = [0,0,0,0,0]
dicecount = [0,0,0,0,0,0]
scorecard = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
rolls_left = 13


def full_house_check(dicecount, dice):
    if 3 in dicecount and 2 in dicecount:
        return 25
    else:
        return 0

def yahtzee_check(dicecount, dice):
    if 5 in dicecount:
        return 50
    else:
        return 0

def four_of_a_kind_check(dicecount, dice):
    if 4 in dicecount or yahtzee_check(dicecount, dice) > 0:
        return sum(dice)
    else:
        return 0

def three_of_a_kind_check(dicecount, dice):
    if 3 in dicecount or four_of_a_kind_check(dicecount, dice) > 0:
        return sum(dice)
    else:
        return 0

def large_striaght_check(dicecount, dice):
    if 1 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice:
        return 40
    elif 6 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice:
        return 40
    else:
        return 0

def small_striaght_check(dicecount, dice):
    if 1 in dice and 2 in dice and 3 in dice and 4 in dice:
        return 30
    elif 2 in dice and 3 in dice and 4 in dice and 5 in dice:
        return 30
    elif 6 in dice and 3 in dice and 4 in dice and 5 in dice:
        return 30
    else:
        return 0

# end of scoring functions
########################################################################
########################################################################
########################################################################

def hightest_score_algo(dicecount, dice, scorecard):
    score = 0
    if  score < yahtzee_check(dicecount, dice):
        score = yahtzee_check(dicecount, dice)
        if scorecard[6] < 0:
            scorecard[6] = yahtzee_check(dicecount, dice)
    if  score < four_of_a_kind_check(dicecount, dice):
        score = four_of_a_kind_check(dicecount, dice)
        if scorecard[7] < 0:
            scorecard[7] = four_of_a_kind_check(dicecount, dice)
    if  score < three_of_a_kind_check(dicecount, dice):
        if scorecard[8] < 0:
            scorecard[8] = three_of_a_kind_check(dicecount, dice)
        score = three_of_a_kind_check(dicecount, dice)
    if  score < large_striaght_check(dicecount, dice):
        if scorecard[9] < 0:
            scorecard[9] = large_striaght_check(dicecount, dice)
        score = large_striaght_check(dicecount, dice)
    if  score < small_striaght_check(dicecount, dice):
        if scorecard[10] < 0:
            scorecard[10] = small_striaght_check(dicecount, dice)
        score = small_striaght_check(dicecount, dice)
    if  score < full_house_check(dicecount, dice):
        if scorecard[11] < 0:
            scorecard[11] = full_house_check(dicecount, dice)
        score = full_house_check(dicecount, dice)
    else:
        score = sum(dice)
    return score

def reroll_dice(num):
    for idx, val in enumerate(dice):
        if idx + 1 == num:
            dice[idx] = random.randrange(1,6)
    return dice

def count_dice(dicecount, dice):
    for idx, val in enumerate(dicecount):
        dicecount[idx] = dice.count(idx + 1)

# program starts
########################################################################
########################################################################
########################################################################


while rolls_left != 0:
    for idx, val in enumerate(dice):
        dice[idx] = random.randrange(1,6)

    print ("this is the inital roll\n", dice)

    for y in range(2):
        user_amount_of_rerolls = int(input("how many dice would you like to reroll"))
        for  i in range(user_amount_of_rerolls):
            user_input = int(input("which dice would you like to reroll"))
            reroll_dice(user_input)
        print (dice)

    count_dice(dicecount, dice)
    print (hightest_score_algo(dicecount, dice, scorecard))
    print (scorecard)