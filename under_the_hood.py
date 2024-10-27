import random

class Dumb_Ass_Error:
    """You forgot to error check or something dumbass, fix it"""
    pass

#for it to work with maxi yatzi we would need a seperate score card
# therefore logic needs to be added to check which kind of game is being played
score_card = {
    'Ones': '-', 'Twos': '-', 'Threes': '-', 'Fours': '-', 'Fives': '-', 'Sixes': '-',
    'One Pair': '-', 'Two Pairs': '-', 'Three of a Kind': '-', 'Four of a Kind': '-', 'Small Straight': '-',
    'Large Straight': '-', 'Full House': '-', 'Chance': '-', 'Yatzy': '-'
}

#this function works flawlessly
def rolling_dice(game_mode_num): #game_mode_num is either 5 or 6 depending on the game mode chosen, ie changing the number of times the dice are rolled
    dice_list = []    # list used to store the values of the rolled dice

    for i in range(0, game_mode_num): # i is the index of the list
        dice_list.append(random.randint(1, 6))
    print_rolls(dice_list, game_mode_num)

    # re-rolling the dice up to 2 re-rolls
    for _ in range(2):
        while True:
            choice_reroll = input("Do you want to re-roll (y - yes, n - no): ").lower().strip()
            if choice_reroll in ('y', 'yes', 'n', 'no'):
                break
            print(f"'{choice_reroll}' is not a valid choice. Please enter 'y' or 'n'.")


        if choice_reroll == "y":
            while True:
                choice_all = input("To re-roll all dice enter 'a', or specify dice positions separated by commas (e.g. 1,3,5): ").lower().strip()

                # Re-roll all dice
                if choice_all in ("a", "all"):
                    for j in range(game_mode_num):
                        dice_list[j] = random.randint(1, 6)
                    print_rolls(dice_list, game_mode_num)
                    break

                else:
                    # Process the input for specific dice to re-roll
                    choice_dicekey = choice_all.split(",")

                    # Validate that all entries are valid numbers in the range
                    if all(key.strip().isdigit() and 1 <= int(key.strip()) <= game_mode_num for key in choice_dicekey):
                        choice_dicekey = [int(key.strip()) for key in choice_dicekey]

                        # Re-roll the chosen dice
                        for key in choice_dicekey:
                            dice_list[key - 1] = random.randint(1, 6)
                        print_rolls(dice_list, game_mode_num)
                        break

                    else:
                        print(f"Please enter positions between 1 and {game_mode_num} only, separated by commas (e.g. 1,3,5).")
        else:
            break # fix this part, do smth when user presses 'n'


    return dice_list


def print_rolls(roll_list, game_mode_num):
    dice_faces = {
        1: ["[       ]", "[   ○   ]", "[       ]"],
        2: ["[ ○     ]", "[       ]", "[     ○ ]"],
        3: ["[ ○     ]", "[   ○   ]", "[     ○ ]"],
        4: ["[ ○   ○ ]", "[       ]", "[ ○   ○ ]"],
        5: ["[ ○   ○ ]", "[   ○   ]", "[ ○   ○ ]"],
        6: ["[ ○   ○ ]", "[ ○   ○ ]", "[ ○   ○ ]"]
    }

    for row in range(3):
        for i in range(1, game_mode_num + 1):
            print(dice_faces[roll_list[i - 1]][row], end=" ")
        print()
    print('-------------------------------------------------')
    for a in range(1, game_mode_num + 1):
        print(f"{a:^10}", end="")
    print()


# Give user possible categories based on what they have in their roll (if elifing at its max)
def possible_categories(dice):
    for num in dice:
        pass


# Start of counting functions (gon count the scores and update them in the score card)

# count single digit score if a player decides to go for this option (make em choose the num to go for). Also, gotta have a global variable "dice" to have access to
# the values of a roll and to be able to work with it

#the rolling dice function returns dice_list a list of all the values of the dice, so in the main file we need to make a global value that takes its output
def single_digits(dice, num):
    score = 0
    for i in dice:
        if i == num:
            score += num

    key_mapping = {
        1: 'Ones',
        2: 'Twos',
        3: 'Threes',
        4: 'Fours',
        5: 'Fives',
        6: 'Sixes'
    }

    if num in key_mapping:
        key = key_mapping[num]
        score_card[key] = score

def two_of_a_kind(dice):
    score = 0
    for num in dice:
        if dice.count(num) >= 2:
            score = num *2
            break

        score_card["Two Pairs"] = score

    return score


# check if a number appears three (or more) times and update the Three of a Kind value if that's the case
def three_of_a_kind(dice):
    score = 0
    for num in dice:
        if dice.count(num) >= 3:
            score = num * 3
            break

    score_card['Three of a Kind'] = score


# same as above but for 4 appearances
def four_of_a_kind(dice):
    score = 0
    for num in dice:
        if dice.count(num) >= 4:
            score = num * 4
            break

    score_card['Four of a Kind'] = score

#def five_of_a_kind(dice):
def small_straight(dice):
    score = 0 
    required_sequence = {1, 2, 3, 4, 5}

    if required_sequence.issubset(dice):
        score = 15
    
    score_card["Small Straight"] = score
             

def large_straight(dice):
    score = 0 
    required_sequence = {2, 3, 4, 5, 6}

    if required_sequence.issubset(dice):
        score = 20
    
    score_card["Small Straight"] = score

#combination of 3 of a kind and a pair of two
def full_house(dice): 
    unique_value = set(dice)
    score = 0

    if len(unique_value) == 2: # underlying logic works for maxi yazi however this if statement does not
        first, second = unique_value
        if dice.count(first) == 3 and dice.count(second) == 2:
            score = (first * 3) + (second * 2)
        elif dice.count(second) == 3 and dice.count(first) == 2:
            score = (first * 2) + (second * 3)
    
    score_card['Full House'] = score

#any combination of dice
def chance(dice):
    score = 0
    for num in dice:
        score += num
    score_card['Chance'] = score

#yeatzy 5 of a kind
def yatzy(dice, game_mode_number):
    score = 0
    if dice.count(dice[0]) == game_mode_number :
        if game_mode_number == 5:
            score = 50
        elif game_mode_number == 6:
            score = 100
        else: 
            raise Dumb_Ass_Error

    return score

# sum of scores from the upper section categories + bonus check
upper_keys = ['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']
def upper_count():
    upper_score = sum(score_card[key] for key in score_card if key in upper_keys)

    if upper_score >= 63:
        upper_score += 50

    return upper_score

# sum of scores from the lower section categories
def lower_count():
    lower_score = sum(score_card[key] for key in score_card if key not in upper_keys)

    return lower_score


def show_scoring_sheet():
    print('Current score sheet:')
    for key, value in score_card.items():
        print(f'{key}: {value}')


def main():
    while any(isinstance(value, str) for value in score_card.values()): #also this function i think needs to be in main.py so this main is limited to only the back end functions
        print('Rolling dice...')
        rolling_dice(5) #5 need to be a variable so we can easily integrate multiplayer



