import random
from math import pi, gcd


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


GOAL_SCORE = 100
FIRST_100_DIGITS_OF_PI_AFTER_DECIMAL = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679 "
MAX_ROLLS = 10
SIDES_OF_DIE = 6


def toss():
    toss = random.randint(0, 1)
    print("Time for the random toss: ", end="")
    print(f"{'You go first' if toss == 0 else 'Computer goes first'}")
    return 0 if toss == 0 else 1


def number_of_rolls():
    nod = -1
    while nod < 0:
        nod = int(input(f"\n{color.PURPLE}(Your Turn){color.END} Enter number of dice to roll (0 - {MAX_ROLLS}): "))
        if nod < 0:
            print("Can't roll negative times man!")
    if nod > MAX_ROLLS:
        print(f"Max number of rolls is {MAX_ROLLS}. Taking number of rolls to be {MAX_ROLLS}...")
    return nod if nod < MAX_ROLLS else MAX_ROLLS


def computer_rolls():
    nod = random.randint(0, MAX_ROLLS)
    print(f"\n{color.RED}(Computer's Turn){color.END} Dice to roll (0 - {MAX_ROLLS}): {nod}")
    return nod


def dice_roll(nod, ops, cp):
    rolls = []
    sum = 0
    if nod != 0:
        for i in range(nod):
            roll = random.randint(1, SIDES_OF_DIE)
            rolls.append(roll)
            if roll == 1:
                break
            sum += roll
        # pig out
        if 1 in rolls:
            print(f"{'You pigged out! :(' if cp == 0 else 'The computer pigged out!'}")
            sum = 1
    # free bacon
    elif nod == 0:
        k = 3 if ops == 0 else int(FIRST_100_DIGITS_OF_PI_AFTER_DECIMAL[ops])
        print(f"Free bacon! Lucky points for {'you!' if cp == 0 else 'the computer'}: {k}")
        sum = k + 3 if ops != 0 else k
    return sum


def print_scores(scores):
    print(f"Your score: {scores[0]}")
    print(f"Computer's Score: {scores[1]}")


def swine_align(cps, ops):
    my_gcd = gcd(cps, ops)
    return True if cps > 0 and ops > 0 and my_gcd > 10 else False


def pig_pass(cps, ops):
    return True if cps < ops and (ops - cps) < 3 else False


def game(scores, currPlayer):
    while scores[0] < GOAL_SCORE and scores[1] < GOAL_SCORE:
        nod = number_of_rolls() if currPlayer == 0 else computer_rolls()
        # basic variable init
        oppPlayer = 1 if currPlayer == 0 else 0
        oppScore = scores[oppPlayer]
        # roll the dice
        sum = dice_roll(nod, oppScore, currPlayer)
        # update score for current player
        scores[currPlayer] += sum
        # print scores per round
        print_scores(scores)
        # swine align and pig pass (if gcd > 10 or diff < 3, don't flip current player)
        if swine_align(scores[currPlayer], oppScore) or pig_pass(scores[currPlayer], oppScore):
            print(
                f"{'Lucky you! Here, have another another chance!' if currPlayer == 0 else 'Computer gets another chance!'}")
        else:
            currPlayer = oppPlayer
    return scores


def main():
    print("Welcome to HOG game ^_^ ")
    scores = [0, 0]
    currPlayer = toss()

    scores = game(scores, currPlayer)
    print(f"\nFinal scores: ")
    print_scores(scores)
    print(
        f"\n{color.CYAN}{color.BOLD}{'You are the winner! :)' if scores[0] > GOAL_SCORE else 'Computer is the winner! :('}{color.END}")


if __name__ == "__main__":
    main()
