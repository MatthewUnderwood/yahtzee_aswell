import random
import yahtzee_checks
import position_functions
import matthews_algo
from contextlib import redirect_stdout


########################################################################
########################################################################
# just declaring the variables and setting up and easy readible scorecard
########################################################################
########################################################################
dice = [0,0,0,0,0]
dicecount = [0,0,0,0,0,0]
extra_yahtzees = [0]
#           [ 0, 1, 2, 3, 4, 5, 6----------, 7----------, 8--------, 9-------, 10------, 11-----, 12----]
#           [ 1, 2, 3, 4, 5, 6, 3 of a kind, 4 of a kind, fullhouse, Sstright, Lstright, yahtzee, chance]
scorecard = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
rolls_left = 13
pos_of_ones = []
pos_of_twos = []


########################################################################
########################################################################
# main program starts
########################################################################
########################################################################
for onethou_rolls in range(500):
    scorecard = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    extra_yahtzees = [0]
    for thirteen_rolls in range(13):
        for idx, val in enumerate(dice):
            dice[idx] = random.randrange(1,7)
        dice.sort()
        print ("this is the inital roll")
        print (dice)
        position_functions.count_dice(dicecount, dice)
        for i in range(2):
            ########################################################################
            ########################################################################
            # this commented out part lets the user acctually pick the dice to roll
            # instead of letting the algo reroll for you
            ########################################################################
            ########################################################################
            # user_amount_of_rerolls = int(input("how many dice would you like to reroll"))
            # for  i in range(user_amount_of_rerolls):
            #     user_input = int(input("which dice would you like to reroll"))
            #     reroll_dice(user_input - 1, dice)
            # print (dice)
            ########################################################################
            ########################################################################
            matthews_algo.matthews_rolling_algo(dicecount, dice, scorecard, extra_yahtzees, pos_of_ones, pos_of_twos)
            dice.sort()
            print(dice)
            position_functions.count_dice(dicecount, dice)
        print (matthews_algo.matthews_score_algo(dicecount, dice, scorecard, extra_yahtzees, pos_of_ones, pos_of_twos))
        print (scorecard)

    score_total = 0
    short_sum = 0
    for i in range(6):
        short_sum = short_sum + scorecard[i]
    if short_sum > 62:
        score_total = score_total + 35
    if scorecard[11] != 0:
        score_total = score_total + sum(scorecard) + (extra_yahtzees[0] * 100)
    else:
        score_total = score_total + sum(scorecard)
    print("your total score is " + str(score_total))
    print(extra_yahtzees[0])

    # this saves the score to an out txt file
    with open('out.txt', 'a') as f:
        with redirect_stdout(f):
            print(str(score_total))