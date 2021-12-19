import random

dice = [3,3,3,4,3]
dicecount = [0,0,0,0,0,0]
extra_yahtzees = [0]
#           [ 0, 1, 2, 3, 4, 5, 6----------, 7----------, 8--------, 9-------, 10------, 11-----, 12----]
#           [ 1, 2, 3, 4, 5, 6, 3 of a kind, 4 of a kind, fullhouse, Sstright, Lstright, yahtzee, chance]
scorecard = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
rolls_left = 13
pos_of_ones = []
pos_of_twos = []


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

def sub_optimal_score(dicecount, dice, scorecard):
    short_sum = 0;
    for i in range(6):
        if scorecard[i] >= 0:
            short_sum = short_sum + scorecard[i]
            if short_sum > 53:
                for idx, val in enumerate(dicecount):
                    if val == 2 and scorecard[idx] < 0:
                        scorecard[idx] = (idx + 1) * 2
                        return
                    if val == 1 and scorecard[idx] < 0:
                        scorecard[idx] = (idx + 1)
                        return
    if scorecard[7] < 0:
        scorecard[7] = 0
        return
    elif scorecard[0] < 0:
        scorecard[0] = dicecount[0]
        return
    elif scorecard[1] < 0 and dicecount[1] != 0:
        scorecard[1] = dicecount[1] * 2
        return
    elif scorecard[11] < 0:
        scorecard[11] = 0
        return
    elif scorecard[10] < 0:
        scorecard[10] = 0
        return
    elif scorecard[1] < 0:
        scorecard[1] = dicecount[1] * 2
        return
    elif scorecard[8] < 0:
        scorecard[8] = 0
        return
    elif scorecard[6] < 0:
        scorecard[6] = 0
        return
    elif scorecard[9] < 0:
        scorecard[9] = 0
        return
    elif scorecard[7] < 0:
        scorecard[7] = 0
        return
    for i in range(13):
        if scorecard[i] < 0 and i <= 5:
            scorecard[i] = (i + 1) * dicecount[i]
        elif scorecard[i] < 0 and i > 5:
            scorecard[i] = 0
    else:
        print("this should not have happened")
        return


def hightest_score_algo(dicecount, dice, scorecard, extra_yahtzees):
    # check to see if we have a yahtzee
    if  yahtzee_check(dicecount, dice) > 0 and scorecard[11] < 0:
        scorecard[11] = yahtzee_check(dicecount, dice)
        return
    #check to see if we have a large straight
    elif  large_striaght_check(dicecount, dice) > 0 and scorecard[10] < 0:
        scorecard[10] = large_striaght_check(dicecount, dice)
        return
    # try and save the highest value roll in top that is above 3
    ############################################################
    ############################################################
    elif 5 in dicecount:
        for idx, val in enumerate(dicecount):
            if val == 5 and scorecard[idx] < 0:
                scorecard[idx] = (idx + 1) * 5
                extra_yahtzees[0] = extra_yahtzees[0] + 1
                return
        if scorecard[7] < 0:
            scorecard[7] = sum(dice)
            extra_yahtzees[0] = extra_yahtzees[0] + 1
            return
        elif scorecard[6] < 0:
             scorecard[6] = sum(dice)
             extra_yahtzees[0] = extra_yahtzees[0] + 1
             return
        elif scorecard[12] < 0:
            scorecard[12] = sum(dice)
            extra_yahtzees[0] = extra_yahtzees[0] + 1
            return
        elif scorecard[11] > 0:
            extra_yahtzees[0] = extra_yahtzees[0] + 1
            for i in range(13):
                if scorecard[i] < 0:
                    scorecard[i] = 0
                    return
        else:
            print("something bad happened 5")
            sub_optimal_score(dicecount, dice, scorecard)
            return
    elif 4 in dicecount:
        for idx, val in enumerate(dicecount):
            if val == 4 and scorecard[idx] < 0:
                scorecard[idx] = (idx + 1) * 4
                return
        if scorecard[7] < 0:
            scorecard[7] = sum(dice)
            return
        elif scorecard[6] < 0:
            scorecard[6] = sum(dice)
            return
        elif scorecard[12] < 0:
            scorecard[12] = sum(dice)
            return
        else:
            print("something bad happened 4")
            sub_optimal_score(dicecount, dice, scorecard)
            return
    elif 3 in dicecount:
        for idx, val in enumerate(dicecount):
            if val == 3 and scorecard[idx] < 0:
                scorecard[idx] = (idx + 1) * 3
                return
        if (scorecard[8] < 0 and sum(dice) < 25) or (scorecard[8] < 0 and scorecard[12] >= 0):
            scorecard[8] = 25
            return
        elif scorecard[6] < 0:
            scorecard[6] = sum(dice)
            return
        elif scorecard[12] < 0:
            scorecard[12] = sum(dice)
            return
        else:
            print("something bad happened 3")
            sub_optimal_score(dicecount, dice, scorecard)
            return
    elif  small_striaght_check(dicecount, dice) > 0 and scorecard[9] < 0:
        scorecard[9] = small_striaght_check(dicecount, dice)
        return
    elif scorecard[12] < 0:
        scorecard[12] = sum(dice)
        return
    ############################################################
    ############################################################
    #if it gets here it will add a zero or sub optimal top to the score
    else:
        print("how did I get here")
        sub_optimal_score(dicecount, dice, scorecard)
    ############################################################
    ############################################################
    ############################################################

def reroll_dice(num, dice):
    if num >= 0 and num <=6:
        dice[num] = random.randrange(1,7)

def count_dice(dicecount, dice):
    for idx, val in enumerate(dicecount):
        dicecount[idx] = dice.count(idx + 1)

def define_position_of_ones(pos_of_ones, dicecount, dice):
    for i in range(len(dicecount)):
        for j in range(len(dice)):
            if dicecount[i] == 1 and i + 1 == dice[j]:
                pos_of_ones.append(j)

def define_position_of_twos(pos_of_twos, dicecount, dice):
    for i in range(len(dicecount)):
        for j in range(len(dice)):
            if dicecount[i] == 2 and i + 1 == dice[j]:
                pos_of_twos.append(j)

def reset_position_of_ones(pos_of_ones):
    pos_of_ones.clear()

def reset_position_of_twos(pos_of_twos):
    pos_of_twos.clear()

def rolling_algo(dicecount, dice, scorecard, extra_yahtzees):

    reset_position_of_ones(pos_of_ones)
    define_position_of_ones(pos_of_ones, dicecount, dice)
    reset_position_of_twos(pos_of_twos)
    define_position_of_twos(pos_of_twos, dicecount, dice)

    if 5 in dicecount and (scorecard[11] != 0 or scorecard[7] < 0 or scorecard[6] < 0 or scorecard[dicecount.index(5)] < 0):
        return
    elif large_striaght_check(dicecount, dice) > 0 and scorecard[10] < 0:
        return
    elif small_striaght_check(dicecount, dice) > 0 and scorecard[10] < 0:
        if 2 in dicecount:
            reroll_dice(pos_of_twos[0], dice)
            return
        elif dice == [1,2,3,4,6]:
            reroll_dice(4, dice)
            return
        elif dice == [1,3,4,5,6]:
            reroll_dice(1, dice)
            return
        else:
            print("the rolling algo at the small sraight part has an error")
    elif 4 in dicecount and (scorecard[11] != 0 or scorecard[7] < 0 or scorecard[6] < 0 or scorecard[dicecount.index(4)] < 0):
        reroll_dice(pos_of_ones[0], dice)
    elif small_striaght_check(dicecount, dice) > 0 and scorecard[9] < 0:
        return
    elif 3 in dicecount and (scorecard[11] != 0 or scorecard[8] < 0 or scorecard[7] < 0 or scorecard[6] < 0 or scorecard[dicecount.index(3)] < 0):
        #take the full house since nothing else is avaiable
        if 2 in dicecount and scorecard[8] < 0 and scorecard[7] >= 0 and scorecard[6] >= 0 and scorecard[dicecount.index(3)] >= 0:
            return
        elif (2 in dicecount) and (scorecard[11] < 0 or scorecard[7] < 0 or scorecard[6] < 0 or scorecard[dicecount.index(3)] < 0):
            for i in range(len(pos_of_twos)):
                reroll_dice(pos_of_twos[i], dice)
            return
        elif 1 in dicecount:
            for i in range(len(pos_of_ones)):
                reroll_dice(pos_of_ones[i], dice)
            return
    elif (2 in dicecount and len(pos_of_twos) > 2) and (scorecard[dicecount.index(2)] < 0 or scorecard[dicecount.index(2, pos_of_twos[1])] < 0 or scorecard[7] < 0 or scorecard[6] < 0):
        for i in range(5,0,-1):
            if scorecard[i] < 0 and dicecount[i] == 2:
                reroll_dice(pos_of_ones[0], dice)
                if dice[dicecount.index(2)] == ((dicecount[i] / 2) * i):
                    reroll_dice(pos_of_twos[2], dice)
                    reroll_dice(pos_of_twos[3], dice)
                    return
                else:
                    reroll_dice(pos_of_twos[0], dice)
                    reroll_dice(pos_of_twos[1], dice)
                    return
            else:
                reroll_dice(pos_of_ones[0], dice)
                reroll_dice(pos_of_twos[0], dice)
                reroll_dice(pos_of_twos[1], dice)
                return
    elif (2 in dicecount and len(pos_of_twos) > 2) and (scorecard[dicecount.index(2)] >= 0 or scorecard[dicecount.index(2, pos_of_twos[1])] >= 0) and (scorecard[8] < 0):
        reroll_dice(pos_of_ones[0], dice)
        return
    elif (2 in dicecount and len(pos_of_twos) == 2) and (scorecard[dicecount.index(2)] < 0 or scorecard[6] < 0 or scorecard[7] < 0):
        for i in range(len(pos_of_ones)):
            reroll_dice(pos_of_ones[i], dice)
        return

    elif scorecard[5] < 0 and dicecount[5] == 1:
        for i in range(5):
            if dice[i] != 6:
                reroll_dice(i, dice)
        return
    elif scorecard[4] < 0 and dicecount[4] == 1:
        for i in range(5):
            if dice[i] != 5:
                reroll_dice(i, dice)
        return
    elif scorecard[3] < 0 and dicecount[3] == 1:
        for i in range(5):
            if dice[i] != 4:
                reroll_dice(i, dice)
        return
    elif scorecard[2] < 0 and dicecount[2] == 1:
        for i in range(5):
            if dice[i] != 3:
                reroll_dice(i, dice)
        return
    elif scorecard[1] < 0 and dicecount[1] == 1:
        for i in range(5):
            if dice[i] != 2:
                reroll_dice(i, dice)
        return
    elif scorecard[0] < 0 and dicecount[0] == 1:
        for i in range(5):
            if dice[i] != 1:
                reroll_dice(i, dice)
        return
    else:
        for i in range(5):
            reroll_dice(i, dice)
            print("ahhhh")
        return



# program starts
########################################################################
########################################################################
########################################################################

for thirteen_rolls in range(13):
    for idx, val in enumerate(dice):
        dice[idx] = random.randrange(1,7)
    dice.sort()
    print ("this is the inital roll")
    print (dice)
    count_dice(dicecount, dice)
    for i in range(2):
        # user_amount_of_rerolls = int(input("how many dice would you like to reroll"))
        # for  i in range(user_amount_of_rerolls):
        #     user_input = int(input("which dice would you like to reroll"))
        #     reroll_dice(user_input - 1, dice)
        # print (dice)
        rolling_algo(dicecount, dice, scorecard, extra_yahtzees)
        dice.sort()
        print(dice)
        count_dice(dicecount, dice)
    print (hightest_score_algo(dicecount, dice, scorecard, extra_yahtzees))
    print (scorecard)

score_total = 0
short_sum = 0
for i in range(6):
    short_sum = short_sum + scorecard[i]
if short_sum > 61:
    score_total = score_total + 35
if scorecard[11] != 0:
    score_total = score_total + sum(scorecard) + (extra_yahtzees[0] * 100)
else:
    score_total = score_total + sum(scorecard)
print("your total score is " + str(score_total))
print(extra_yahtzees[0])
