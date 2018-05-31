# Score categories
# Change the values as you see fit
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11
YACHT = 12

from collections import defaultdict


def score(dice, category):
    if category == ONES:
        return sum(filter(lambda x: x == 1, dice))
    elif category == TWOS:
        return sum(filter(lambda x: x == 2, dice))
    elif category == THREES:
        return sum(filter(lambda x: x == 3, dice))
    elif category == FOURS:
        return sum(filter(lambda x: x == 4, dice))
    elif category == FIVES:
        return sum(filter(lambda x: x == 5, dice))
    elif category == SIXES:
        return sum(filter(lambda x: x == 6, dice))
    elif category == FULL_HOUSE:
        d = defaultdict(int)
        for x in dice:
            d[x] += 1
        if set(d.values()) == {2, 3}:
            total = 0
            for (k, v) in d.items():
                total += k * v
            return total
        else:
            return 0
    elif category == FOUR_OF_A_KIND:
        d = defaultdict(int)
        for x in dice:
            d[x] += 1
        for (k, v) in d.items():
            if v == 4 or v == 5:
                return k * 4
        return 0
    elif category == LITTLE_STRAIGHT:
        if set(dice) == {2, 1, 3, 4, 5}:
            return 30
        else:
            return 0
    elif category == BIG_STRAIGHT:
        if set(dice) == {2, 3, 4, 5, 6}:
            return 30
        else:
            return 0
    elif category == CHOICE:
        return sum(dice)
    elif category == YACHT:
        if len(set(dice)) == 1:
            return 50
        else:
            return 0
