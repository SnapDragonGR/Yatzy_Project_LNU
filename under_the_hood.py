import random

score_card = {
    'Ones': '-', 'Twos': '-', 'Threes': '-', 'Fours': '-', 'Fives': '-', 'Sixes': '-',
    'One Pair': '-', 'Two Pairs': '-', 'Three of a Kind': '-', 'Four of a Kind': '-', 'Small Straight': '-',
    'Large Straight': '-', 'Full House': '-', 'Chance': '-', 'Yatzy': '-'
}


def rolling_dice(game_mode_num): #game_mode_num is either 5 or 6 depending on the game mode chosen, ie chaging the number of times the dice are rolled
    #rolling hte dice
    dice_list = [] # list used to store the values of the rolled dice
    for i in range(0, game_mode_num): # i is the index of the list
        dice_list.append(random.randint(1, 6))
    print_rolls(dice_list, game_mode_num)
    #re-rolling the dice
    for i in range(0, 2):
        choice_reroll = input("Do you want to reroll(y - yes, n - no):")

        if choice_reroll.lower() != "y" or "n": 
            print(choice_reroll, "is not a valid choice") #needs to be in a loop to error check
            choice_reroll = input("Do you want to reroll(y - yes, n - no)")

        elif choice_reroll.lower() == "y": 
            choice_all = input("To reroll all dice enter 'a', enter anyother key to reroll a subset of dice :")

            if (choice_all.lower() == "a"):
                for j in range(0, game_mode_num):
                    dice_list.append(random.randint(1, 6))
                print_rolls(dice_list, game_mode_num)
            
            else:
                choice_dicenum = input("How many dice do you want to reroll:")
                choice_dicekey = []
                print("Which dice do you want to reroll(enter n - where n is the key of the dice displayed below the dice)", end = " ") #error handling for this needs to be one 
                for k in range(0,choice_dicenum):
                    choice_dicekey.append(int(input()))
                
                for key in choice_dicekey: 
                    dice_list[key-1] = random.randint(1, 6)
                print_rolls(dice_list, game_mode_num)


def print_rolls(roll_list, game_mode_num):  
    for row in range(3):            
        for i in range(1, game_mode_num): 
            print("gbiyasmlkb")


# Give user possible categories based on what they have in their roll (if elifing at its max)
def possible_categories(dice):
    for num in dice:
        pass


# Start of counting functions (gon count the scores and update them in the score card)

# count single digit score if a player decides to go for this option (make em choose the num to go for). Also, gotta have a global variable "dice" to have access to
# the values of a roll and to be able to work with it
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


def small_straight(dice):
    pass

def large_straight(dice):
    pass


def full_house(dice):
    pass


def chance(dice):
    pass


def yatzy(dice):
    pass


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


def show_scoring_sheet():
    print('Current score sheet:')
    for key, value in score_card.items():
        print(f'{key}: {value}')


def main():
    while any(isinstance(value, str) for value in score_card.values()):
        print('Rolling dice...')
        rolling_dice(5)

