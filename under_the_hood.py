import random

score_card = {
    'ones': 0, 'twos': 0, 'threes': 0, 'fours': 0, 'fives': 0, 'sixes': 0,
    'one_pair': 0, 'two_pairs': 0, 'three_of_a_kind': 0, 'four_of_a_kind': 0, 'small_straight': 0,
    'large_straight': 0, 'full_house': 0, 'chance': 0, 'yatzy': 0, 'bonus': 0
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


# sum of scores from the upper section categories + bonus check
upper_keys = ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes']
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


def main():
    while all(value == 0 for value in score_card.values()):   # correct the conditions
        rolling_dice()

