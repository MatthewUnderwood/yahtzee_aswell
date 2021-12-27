########################################################################
########################################################################
# some functions to define the variables to be used after the roll
########################################################################
########################################################################
import random

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