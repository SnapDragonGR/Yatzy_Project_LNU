import random

""" current error list:
2. full house dosent work properly with maxi-yatzi as it requires 2 unique values in the list, however for maxi yatzi there can be 3 unique values and still be true
3. villa, tower and all other maxi yatzi also needs to be rechecked
4. I will make test cases to debug and verify all of the logic 
5. I also changed main function to not repeat code, however this might fuck with some of the code so more extensive testing is needed 
6. I also might write some automated test to all the logic functions and just write the output to a log file so i can recheck
"""


def score_card_generate(player_count, game_mode_num):
    if game_mode_num == 5:
        score_card = {
        'Ones': ['-']*player_count , 'Twos': ['-']*player_count, 'Threes': ['-']*player_count, 'Fours': ['-']*player_count, 'Fives': ['-']*player_count, 'Sixes': ['-']*player_count,
        'One Pair': ['-']*player_count, 'Two Pairs': ['-']*player_count, 'Three of a Kind': ['-']*player_count, 'Four of a Kind': ['-']*player_count, 'Small Straight': ['-']*player_count,
        'Large Straight': ['-']*player_count, 'Full House': ['-']*player_count, 'Chance': ['-']*player_count, 'Yatzy': ['-']*player_count
        }
        return score_card
    
    elif game_mode_num == 6:
        score_card = {
        'Ones': ['-']*player_count , 'Twos': ['-']*player_count, 'Threes': ['-']*player_count, 'Fours': ['-']*player_count, 'Fives': ['-']*player_count, 'Sixes': ['-']*player_count,
        'One Pair': ['-']*player_count, 'Two Pairs': ['-']*player_count, 'Three Pairs': ['-']*player_count,'Three of a Kind': ['-']*player_count, 'Four of a Kind': ['-']*player_count, 'Five of a kind':['-']*player_count, 
        'Small Straight': ['-']*player_count,'Large Straight': ['-']*player_count, 'Full Straight':['-']*player_count,'Full House': ['-']*player_count,'Villa':['-']*player_count, 'Tower':['-']*player_count ,'Chance': ['-']*player_count, 'Yatzy': ['-']*player_count
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
            choice_reroll = input("\nDo you want to re-roll (y - yes, n - no): ").lower().strip()#right i forgot strip the spaces good catch
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

    dash_length = (9 * game_mode_num) + (game_mode_num - 1)
    print("-" * dash_length)

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


# fixed
def two_pairs(dice):
    score = 0
    sort_dice = sorted(dice, reverse=True)
    pairs = []

    for num in set(sort_dice):
        count = dice.count(num)

        if count >= 4:
            return 0

        elif count >= 2:
            pairs.append(num * 2)

            if len(pairs) == 2:
                score = sum(pairs)
                return score

    return score


def three_pairs(dice): #only for maxi-yatzy
    score = 0 
    unique_dice = set(dice)
    sort_dice = sorted(unique_dice)
    pairs = []

    if len(unique_dice) == 1:
        return score

    else:
        for num in sort_dice:
            if dice.count(num) >= 4: #if there are identical pairs append them to the list two times #also needs to return 0
                pairs.append(num*2)
                pairs.append(num*2)

            elif dice.count(num) >= 2:#schecking if there are pairs
                pairs.append(num*2)

                if len(pairs) == 3: #if the number of pairs is already 3 return the score
                    score = sum(pairs)
                    return score

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


def five_of_a_kind(dice): # for maxi yatzy only
    score = 0
    for num in dice:
        if dice.count(num) >= 5: #if there are 5 or more of the same rolls update the score
            score = num * 5
            break
    return score

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


def full_straight(dice): #for maxi yatzy only
    score = 0
    required_sequence = {1, 2, 3, 4, 5, 6}

    if required_sequence.issubset(dice):
        score = 21

    return score


#combination of 3 of a kind and a pair of two
def full_house(dice): 
    unique_value = set(dice)
    score = 0

    if len(unique_value) == 2:
        first, second = unique_value
        if dice.count(first) == 3 and dice.count(second) == 2:
            score = (first * 3) + (second * 2)
        elif dice.count(second) == 3 and dice.count(first) == 2:
            score = (first * 2) + (second * 3)

    return score


def villa(dice):
    #two there of a kinds
    score = 0
    unique_dice = set(dice)
    triplet= []

    if len(unique_dice) == 1:
        return score
    else:
        for num in unique_dice:
            if dice.count(num) == 3:
                triplet.append(num * 3)
                if len(triplet) == 2:
                    score = sum(triplet)
                    return score
    
    return score


def tower(dice):
    score = 0
    unique_dice = set(dice)
    pairs = []

    if len(unique_dice) == 1:
        return score

    else:
        for num in unique_dice:
            if dice.count(num) == 4 :
                pairs.append(num*4)

            elif dice.count(num) == 2:
                pairs.append(num * 2)

    if len(pairs) == 2:
        score = sum(pairs)
        return score

    else:
        return score


# any combination of dice
def chance(dice):
    score = 0
    for num in dice:
        score += num

    return score


#yatzy 5 of a kind
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


def upper_count(score_card, which_player):
    upper_score = sum(
        int(score_card[key][which_player])
        for key in score_card if key in upper_keys and str(score_card[key][which_player]).isdigit()
    )

    if upper_score >= 63:
        upper_score += 50

    return upper_score


def lower_count(score_card, which_player):
    lower_score = sum(
        int(score_card[key][which_player])
        for key in score_card if key not in upper_keys and str(score_card[key][which_player]).isdigit()
    )

    return lower_score


# final score sum for each player
# check if that works for maxi yatzy
def final_score(score_card, which_player):
    for player_index in range(which_player):
        upper_score = upper_count(score_card, player_index)
        lower_score = lower_count(score_card, player_index)
        final_score = upper_score + lower_score

        print(f"\nFinal score for Player {player_index + 1}: {final_score}")


def cross_out(which_player, score_card):
    available_categories = []

    for category in score_card.keys():
        if score_card[category][which_player] == '-':
            available_categories.append(category)

    for index, category in enumerate(available_categories, start=1):
        print(f"{index}. {category}")

    choice = input("\nWhich one would you like to cross out (index)? ").strip()

    while not choice.isdigit() or int(choice) not in range(1, len(available_categories) + 1):
        print("Invalid input. Please enter an index for an uncrossed category.")
        choice = input("Which category would you like to cross out (index)? ").strip()

    category_name = available_categories[int(choice) - 1]

    score_card[category_name][which_player] = 'x'

    print(f"\nCategory '{category_name}' has been crossed out.")


def possible_categories(dice, which_player, score_card, game_mode_type):
    if all(score != '-' for score in [score_card[key][which_player] for key in score_card]):
        print(f"Player {which_player + 1} has completed all categories and will skip this turn.")
        return None

    possibilities = []

    # Calculate potential scores for each category
    if game_mode_type == 5:
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
            'Yatzy': yatzy(dice, 5)
            }

    elif game_mode_type == 6:
        scoring_dict={
            'Ones': single_digits(dice, 1),
            'Twos': single_digits(dice, 2),
            'Threes': single_digits(dice, 3),
            'Fours': single_digits(dice, 4),
            'Fives': single_digits(dice, 5),
            'Sixes': single_digits(dice, 6),
            'One Pair': one_pair(dice),
            'Two Pairs': two_pairs(dice),
            'Three Pairs': three_pairs(dice),
            'Three of a Kind': three_of_a_kind(dice),
            'Four of a Kind': four_of_a_kind(dice),
            'Five of a kind': five_of_a_kind(dice),
            'Small Straight': small_straight(dice),
            'Large Straight': large_straight(dice),
            'Full Straight': full_straight(dice),
            'Full House': full_house(dice),
            'Villa': villa(dice),
            'Tower': tower(dice),
            'Chance': chance(dice),
            'Yatzy': yatzy(dice, 6)
        }

    # Fill in possibilities with categories that have a valid score > 0
    for name, score in scoring_dict.items():
        if score_card[name][which_player] == '-' and score > 0:  # Check score is valid and category isn't used
            possibilities.append((name, score))

    # Return false for future crossing out if no possibilities found
    if not possibilities:
        print("\nNo valid scoring categories available for this roll. List of categories available to cross out:")
        cross_out(which_player, score_card)
        return None

    # Display possible categories to the user
    print("\nPossible categories for this roll:")
    for index, (name, _) in enumerate(possibilities, 1):
        print(f"{index}. {name}")

    # Error handling with user input
    while True:
        choice = input("\nChoose a category by number, or type 'x' to cross out a category: ")

        if choice == 'x':
            cross_out(which_player, score_card)
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
    print('\nCurrent score sheet:')

    header = f"|{'Categories':<16s}|" + "".join(f"{'P' + str(p + 1):^5}" + "|" for p in range(player_count))
    print(header)

    print("-" * (len(header)))

    for key, value in score_card.items():
        print(f'|{key:<16}|' + "".join(f"{player_score:^5}" + "|" for player_score in value))

    print("-" * len(header))
