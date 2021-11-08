import random

dice = [0,0,0,0,0]
dicecount = [0,0,0,0,0,0]
yahtzee_count = 0

#           [ 1, 2, 3, 4, 5, 6, 3 of a kind, 4 of a kind, fullhouse, Sstright, Lstright, yahtzee, chance]
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

def hightest_score_algo(dicecount, dice, scorecard, yahtzee_count):
    score = 0

    # check to see if we have a yahtzee
    if  score < yahtzee_check(dicecount, dice):
        yahtzee_count = yahtzee_count + 1
        if scorecard[11] < 0:
            scorecard[11] = yahtzee_check(dicecount, dice)
            return
    #check to see if we have a large straight
    if  score < large_striaght_check(dicecount, dice):
        if scorecard[10] < 0:
            scorecard[10] = large_striaght_check(dicecount, dice)
            return
    # try and save the highest value roll in top
    if 5 in dicecount:
        yahtzee_count = yahtzee_count + 1
        for idx, val in enumerate(dicecount):
            if val == 5 and scorecard[idx] < 0:
                scorecard[idx] = (idx + 1) * 5
                return
    if 4 in dicecount:
        for idx, val in enumerate(dicecount):
            if val == 4 and scorecard[idx] < 0:
                scorecard[idx] = (idx + 1) * 4
                return
    if 3 in dicecount:
        for idx, val in enumerate(dicecount):
            if val == 3 and scorecard[idx] < 0:
                scorecard[idx] = (idx + 1) * 3
                return

    #check to find the remaining highest score possible and save it
    if score < sum(dice):
        score = sum(dice)
    if  score < small_striaght_check(dicecount, dice):
        if scorecard[9] < 0:
            scorecard[9] = small_striaght_check(dicecount, dice)
            return
        score = small_striaght_check(dicecount, dice)
    if  score < full_house_check(dicecount, dice):
        if scorecard[8] < 0:
            scorecard[8] = full_house_check(dicecount, dice)
            return
        score = full_house_check(dicecount, dice)
    if 4 in dicecount:
        for idx, val in enumerate(dicecount):
            if val == 4 and scorecard[7] < 0:
                scorecard[7] = sum(dice)
                return
    if 3 in dicecount:
        for idx, val in enumerate(dicecount):
            if val == 3 and scorecard[6] < 0:
                scorecard[6] = sum(dice)
                return
    elif scorecard[12] < 0:
        scorecard[12] = sum(dice)
    return score

def reroll_dice(num):
    for idx, val in enumerate(dice):
        if idx + 1 == num:
            dice[idx] = random.randrange(1,7)
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
        dice[idx] = random.randrange(1,7)

    print ("this is the inital roll\n", dice)

    for y in range(2):
        user_amount_of_rerolls = int(input("how many dice would you like to reroll"))
        for  i in range(user_amount_of_rerolls):
            user_input = int(input("which dice would you like to reroll"))
            reroll_dice(user_input)
        print (dice)

    count_dice(dicecount, dice)
    print (hightest_score_algo(dicecount, dice, scorecard, yahtzee_count))
    print (scorecard)