########################################################################
########################################################################
# this looks to find the best scoring option of a bad roll ussually taking
# a zero somewhere on scorecard
########################################################################
########################################################################
import random
import position_functions
import yahtzee_checks

def matthews_sub_optimal_score(dicecount, dice, scorecard):
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

########################################################################
########################################################################
# main scoring algo that looks to find a optimal score
########################################################################
########################################################################

def matthews_score_algo(dicecount, dice, scorecard, extra_yahtzees, pos_of_ones, pos_of_twos):
    # check to see if we have a yahtzee
    if  yahtzee_checks.yahtzee_check(dicecount, dice) > 0 and scorecard[11] < 0:
        scorecard[11] = yahtzee_checks.yahtzee_check(dicecount, dice)
        return
    #check to see if we have a large straight
    elif  yahtzee_checks.large_striaght_check(dicecount, dice) > 0 and scorecard[10] < 0:
        scorecard[10] = yahtzee_checks.large_striaght_check(dicecount, dice)
        return
    # check to see if we have a yahtzee that can't be put in the yahtzee scorecard slot
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
            matthews_sub_optimal_score(dicecount, dice, scorecard)
            return
    # checks to see if we have a 4 and saves it in the best space available
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
            matthews_sub_optimal_score(dicecount, dice, scorecard)
            return
    #checks to see if we have a 3 of a kind and saves it in the best slot if available
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
            matthews_sub_optimal_score(dicecount, dice, scorecard)
            return
    elif  yahtzee_checks.small_striaght_check(dicecount, dice) > 0 and scorecard[9] < 0:
        scorecard[9] = yahtzee_checks.small_striaght_check(dicecount, dice)
        return
    elif scorecard[12] < 0:
        scorecard[12] = sum(dice)
        return
    ############################################################
    ############################################################
    #if it gets here it will add a zero or sub optimal top to the score
    else:
        print("how did I get here")
        matthews_sub_optimal_score(dicecount, dice, scorecard)
    ############################################################
    ############################################################


########################################################################
########################################################################
# my rolling algo it looks for dice that are alike (pairs or triples)
# and rerolls the other dice if a slot in scorecard is open for that roll
# if it doesn't find any pattern that open it rerolls all the dice
########################################################################
########################################################################

def matthews_rolling_algo(dicecount, dice, scorecard, extra_yahtzees, pos_of_ones, pos_of_twos):
    position_functions.reset_position_of_ones(pos_of_ones)
    position_functions.define_position_of_ones(pos_of_ones, dicecount, dice)
    position_functions.reset_position_of_twos(pos_of_twos)
    position_functions.define_position_of_twos(pos_of_twos, dicecount, dice)

    if 5 in dicecount and (scorecard[11] != 0 or scorecard[7] < 0 or scorecard[6] < 0 or scorecard[dicecount.index(5)] < 0):
        return
    elif yahtzee_checks.large_striaght_check(dicecount, dice) > 0 and scorecard[10] < 0:
        return
    elif yahtzee_checks.small_striaght_check(dicecount, dice) > 0 and scorecard[10] < 0:
        if 2 in dicecount:
            position_functions.reroll_dice(pos_of_twos[0], dice)
            return
        elif dice == [1,2,3,4,6]:
            position_functions.reroll_dice(4, dice)
            return
        elif dice == [1,3,4,5,6]:
            position_functions.reroll_dice(1, dice)
            return
        else:
            print("the rolling algo at the small sraight part has an error")
    elif 4 in dicecount and (scorecard[11] != 0 or scorecard[7] < 0 or scorecard[6] < 0 or scorecard[dicecount.index(4)] < 0):
        position_functions.reroll_dice(pos_of_ones[0], dice)
    elif yahtzee_checks.small_striaght_check(dicecount, dice) > 0 and scorecard[9] < 0:
        return
    elif 3 in dicecount and (scorecard[11] != 0 or scorecard[8] < 0 or scorecard[7] < 0 or scorecard[6] < 0 or scorecard[dicecount.index(3)] < 0):
        #take the full house since nothing else is avaiable
        if 2 in dicecount and scorecard[8] < 0 and scorecard[7] >= 0 and scorecard[6] >= 0 and scorecard[dicecount.index(3)] >= 0:
            return
        elif (2 in dicecount) and (scorecard[11] < 0 or scorecard[7] < 0 or scorecard[6] < 0 or scorecard[dicecount.index(3)] < 0):
            for i in range(len(pos_of_twos)):
                position_functions.reroll_dice(pos_of_twos[i], dice)
            return
        elif 1 in dicecount:
            for i in range(len(pos_of_ones)):
                position_functions.reroll_dice(pos_of_ones[i], dice)
            return
    elif (2 in dicecount and len(pos_of_twos) > 2) and (scorecard[dicecount.index(2)] < 0 or scorecard[dicecount.index(2, pos_of_twos[1])] < 0 or scorecard[7] < 0 or scorecard[6] < 0):
        for i in range(5,0,-1):
            if scorecard[i] < 0 and dicecount[i] == 2:
                position_functions.reroll_dice(pos_of_ones[0], dice)
                if dice[dicecount.index(2)] == ((dicecount[i] / 2) * i):
                    position_functions.reroll_dice(pos_of_twos[2], dice)
                    position_functions.reroll_dice(pos_of_twos[3], dice)
                    return
                else:
                    position_functions.reroll_dice(pos_of_twos[0], dice)
                    position_functions.reroll_dice(pos_of_twos[1], dice)
                    return
            else:
                position_functions.reroll_dice(pos_of_ones[0], dice)
                position_functions.reroll_dice(pos_of_twos[0], dice)
                position_functions.reroll_dice(pos_of_twos[1], dice)
                return
    elif (2 in dicecount and len(pos_of_twos) > 2) and (scorecard[dicecount.index(2)] >= 0 or scorecard[dicecount.index(2, pos_of_twos[1])] >= 0) and (scorecard[8] < 0):
        position_functions.reroll_dice(pos_of_ones[0], dice)
        return
    elif (2 in dicecount and len(pos_of_twos) == 2) and (scorecard[dicecount.index(2)] < 0 or scorecard[6] < 0 or scorecard[7] < 0):
        for i in range(len(pos_of_ones)):
            position_functions.reroll_dice(pos_of_ones[i], dice)
        return

    elif scorecard[5] < 0 and dicecount[5] == 1:
        for i in range(5):
            if dice[i] != 6:
                position_functions.reroll_dice(i, dice)
        return
    elif scorecard[4] < 0 and dicecount[4] == 1:
        for i in range(5):
            if dice[i] != 5:
                position_functions.reroll_dice(i, dice)
        return
    elif scorecard[3] < 0 and dicecount[3] == 1:
        for i in range(5):
            if dice[i] != 4:
                position_functions.reroll_dice(i, dice)
        return
    elif scorecard[2] < 0 and dicecount[2] == 1:
        for i in range(5):
            if dice[i] != 3:
                position_functions.reroll_dice(i, dice)
        return
    elif scorecard[1] < 0 and dicecount[1] == 1:
        for i in range(5):
            if dice[i] != 2:
                position_functions.reroll_dice(i, dice)
        return
    elif scorecard[0] < 0 and dicecount[0] == 1:
        for i in range(5):
            if dice[i] != 1:
                position_functions.reroll_dice(i, dice)
        return
    else:
        for i in range(5):
            position_functions.reroll_dice(i, dice)
            print("ahhhh")
        return
