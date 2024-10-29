import random

def score_card_generate(player_count):
    score_card = {
        'Ones': ['-']*player_count , 'Twos': ['-']*player_count, 'Threes': ['-']*player_count, 'Fours': ['-']*player_count, 'Fives': ['-']*player_count, 'Sixes': ['-']*player_count,
        'One Pair': ['-']*player_count, 'Two Pairs': ['-']*player_count, 'Three of a Kind': ['-']*player_count, 'Four of a Kind': ['-']*player_count, 'Small Straight': ['-']*player_count,
        'Large Straight': ['-']*player_count, 'Full House': ['-']*player_count, 'Chance': ['-']*player_count, 'Yatzy': ['-']*player_count
    }

    return score_card


#this function works flawlessly
def rolling_dice(game_mode_num): #game_mode_num is either 5 or 6 depending on the game mode chosen, ie changing the number of times the dice are rolled
    dice_list = []    # list used to store the values of the rolled dice

    for i in range(0, game_mode_num): # i is the index of the list
        dice_list.append(random.randint(1, 6))
    print_rolls(dice_list, game_mode_num)

    # re-rolling the dice up to 2 re-rolls
    for _ in range(2):
        while True:
            choice_reroll = input("Do you want to re-roll (y - yes, n - no): ").lower().strip()#right i forgot strip the spaces good catch
            if choice_reroll in ('y', 'yes', 'n', 'no'):
                break
            print(f"'{choice_reroll}' is not a valid choice. Please enter 'y' or 'n'.")


        if choice_reroll in ("y", "yes"):
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
            return dice_list
            
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

def single_digits(dice, num):
    score = sum(i for i in dice if i == num)
    return score

def one_pair(dice):
    score = 0
    unique_dice = set(dice)
    sort_dice = sorted(unique_dice, reverse=True)
    for num in sort_dice:
        if dice.count(num) >= 2:
            score = num * 2
            break

    return score

def two_pairs(dice): # this is wrong for maxi yatzi
    score = 0
    unique_dice = set(dice)
    sort_dice = sorted(unique_dice, reverse=True)
    pairs = []

    for num in sort_dice:
        if dice.count(num) >= 2:
            pairs.append(num*2)
        
    if len(pairs) == 2:
        score = sum(pairs)
        return score
    else:
        return score
    

# check if a number appears three (or more) times and update the Three of a Kind value if that's the case
# noinspection DuplicatedCode
def three_of_a_kind(dice):
    score = 0
    for num in dice:
        if dice.count(num) >= 3:
            score = num * 3
            break

    return score


# same as above but for 4 appearances
def four_of_a_kind(dice):
    score = 0
    for num in dice:
        if dice.count(num) >= 4:
            score = num * 4
            break

    return score

#def five_of_a_kind(dice):
def small_straight(dice):
    score = 0 
    required_sequence = {1, 2, 3, 4, 5}

    if required_sequence.issubset(dice):
        score = 15

    return score
             
def large_straight(dice):
    score = 0 
    required_sequence = {2, 3, 4, 5, 6}

    if required_sequence.issubset(dice):
        score = 20

    return score

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

    return score

#any combination of dice
def chance(dice):
    score = 0
    for num in dice:
        score += num

    return score

#yeatzy 5 of a kind
def yatzy(dice, game_mode_number):
    score = 0
    if dice.count(dice[0]) == game_mode_number :
        if game_mode_number == 5:
            score = 50
        elif game_mode_number == 6:
            score = 100
    return score

# sum of scores from the upper section categories + bonus check
upper_keys = ['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']
def upper_count(score_card):
    upper_score = sum(int(score_card[key]) for key in score_card if key in upper_keys and str(score_card[key]).isdigit())

    if upper_score >= 63:
        upper_score += 50

    return upper_score

# sum of scores from the lower section categories
def lower_count(score_card):
    lower_score = sum(int(score_card[key]) for key in score_card if key not in upper_keys and str(score_card[key]).isdigit())

    return lower_score

def possible_categories(dice, which_player, score_card):
    possibilities = []

    # Calculate potential scores for each category
    scoring_dict = {
        'Ones': single_digits(dice, 1),
        'Twos': single_digits(dice, 2),
        'Threes': single_digits(dice, 3),
        'Fours': single_digits(dice, 4),
        'Fives': single_digits(dice, 5),
        'Sixes': single_digits(dice, 6),
        'One Pair': one_pair(dice),
        'Two Pairs': two_pairs(dice),
        'Three of a Kind': three_of_a_kind(dice),
        'Four of a Kind': four_of_a_kind(dice),
        'Small Straight': small_straight(dice),
        'Large Straight': large_straight(dice),
        'Full House': full_house(dice),
        'Chance': chance(dice),
        'Yatzy': yatzy(dice, 5)  # fix this to work with a 6 (maxi) as well
    }

    # Fill in possibilities with categories that have a valid score > 0
    for name, score in scoring_dict.items():
        if score_card[name][which_player] == '-' and score > 0:  # Check score is valid and category isn't used
            possibilities.append((name, score))

    # Early exit if no valid categories
    if not possibilities:
        print("No valid scoring categories available for this roll. You have to cross out a category to continue.")
        print()
        choice = input("Which category would you like to cross out (by name)? ").strip()
        processed_score_card = {key.lower().replace(' ', ''): key for key in score_card}

        processed_choice = choice.lower().replace(' ', '')

        while processed_choice not in processed_score_card:
            print("Invalid input. Please enter a valid number corresponding to a category.")
            choice = input("Enter the name of the category you want to choose: ").strip()
            processed_choice = choice.lower().replace(' ', '')

        category_name = processed_score_card[processed_choice]
        score_card[category_name][which_player] = 'x'

        print()
        print(f"Category '{category_name}' has been crossed out.")

        return None

    # Display possible categories to the user
    print()
    print("Possible categories for this roll:")
    for index, (name, _) in enumerate(possibilities, 1):
        print(f"{index}. {name}")

    # Error handling with user input
    print()
    while True:
        choice = input("Choose a category by number, or type 'x' to cross out a category: ")

        if choice == 'x':
            choice = input("Which category would you like to cross out (by name)? ").strip()

            processed_score_card = {key.lower().replace(' ',''): key for key in score_card}

            processed_choice = choice.lower().replace(' ', '')

            while processed_choice not in processed_score_card:
                print("Invalid input. Please enter a valid number corresponding to a category.")
                choice = input("Enter the name of the category you want to choose: ").strip()
                processed_choice = choice.lower().replace(' ', '')


            category_name = processed_score_card[processed_choice]
            score_card[category_name][which_player] = 'x'

            print(f"Category '{category_name}' has been crossed out.")
            break

        elif choice.isdigit() and 1 <= int(choice) <= len(possibilities):
            choice = int(choice) - 1
            selected_category, selected_score = possibilities[choice]
            score_card[selected_category][which_player] = selected_score

            print(f"You selected '{selected_category}' and scored {selected_score}.")
            break

        else:
            print("Invalid input. Please enter a valid number corresponding to a category or 'x' to cross out a category.")


def show_scoring_sheet(player_count, score_card):
    print()
    print('Current score sheet:')
    header = f"|{'Categories':<16s}|"+"".join(f"P{p+1:^5}|" for p in range(player_count))
    print(header)
    print("-"* (len(header)-1)) 
    for key, value in score_card.items(): #this is most certainly also gonna break #suprisingly did not break
        print(f'|{key:<16}|' +"".join(f"{player_score:^5}|" for player_score in value ))
    print("-"* (len(header)-1))
