import random

""" current error list:
1. I also might write some automated test to all the logic functions and just write the output to a log file so i can recheck
"""

# The function generates a scorecard dictionary for Yatzy / Maxi Yatzy depending on the number of players and game mode (5 or 6 dice).
# Each category has a list with placeholders '-' for each player, indicating that no score has been recorded yet.
# Different categories are generated depending on the selected game mode.
def score_card_generate(player_count, game_mode_num):
    if game_mode_num == 5:
        score_card = {
        'Ones': ['-'] * player_count , 'Twos': ['-'] * player_count, 'Threes': ['-'] * player_count, 'Fours': ['-'] * player_count, 'Fives': ['-'] * player_count,
        'Sixes': ['-'] * player_count, 'One Pair': ['-'] * player_count, 'Two Pairs': ['-'] * player_count, 'Three of a Kind': ['-'] * player_count,
        'Four of a Kind': ['-'] * player_count, 'Small Straight': ['-'] * player_count,
        'Large Straight': ['-'] * player_count, 'Full House': ['-'] * player_count, 'Chance': ['-'] * player_count, 'Yatzy': ['-'] * player_count
        }
        return score_card
    
    elif game_mode_num == 6:
        score_card = {
        'Ones': ['-'] * player_count , 'Twos': ['-'] * player_count, 'Threes': ['-'] * player_count, 'Fours': ['-'] * player_count, 'Fives': ['-'] * player_count,
        'Sixes': ['-'] * player_count, 'One Pair': ['-'] * player_count, 'Two Pairs': ['-'] * player_count, 'Three Pairs': ['-'] * player_count,
        'Three of a Kind': ['-'] * player_count, 'Four of a Kind': ['-'] * player_count, 'Five of a kind':['-'] * player_count, 'Small Straight': ['-'] * player_count,
        'Large Straight': ['-'] * player_count, 'Full Straight':['-'] * player_count,'Full House': ['-'] * player_count,'Villa':['-'] * player_count,
        'Tower':['-'] * player_count , 'Chance': ['-'] * player_count, 'Yatzy': ['-'] * player_count
        }
        return score_card

# Main game mechanics function.
# Rolls a specified number of dice (based on game mode) and allows 2 re-rolls. The user can choose to re-roll all dice or select specific
# dice to re-roll by providing their positions. Validations ensure inputs are within the allowed range and format, which prevents the program from
# crashing and improving usability.
def rolling_dice(game_mode_num): # game_mode_num is either 5 or 6, defining the number of dice to roll
    dice_list = []    # List used to store the values of the rolled dice

    # Initial roll for the specified number of dice
    for i in range(0, game_mode_num): # i is the index of the list
        dice_list.append(random.randint(1, 6))
    print_rolls(dice_list, game_mode_num)

    # Re-rolling the dice up to 2 re-rolls
    for _ in range(2):
        while True:
            # Ask if the player wants to re-roll
            choice_reroll = input("\nDo you want to re-roll (y - yes, n - no): ").lower().strip()
            if choice_reroll in ('y', 'yes', 'n', 'no'):
                break

            print(f"'{choice_reroll}' is not a valid choice. Please enter 'y' or 'n'.")


        if choice_reroll in ("y", "yes"):
            while True:
                choice_all = input("To re-roll all dice enter 'a', or specify dice positions separated by commas (e.g. 1,3,5): ").lower().strip()
                print()

                # Re-roll all dice if 'a' is chosen
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


# This function prints the rolled dice in an aesthetically pleasing visual format, showing dice faces.
# Each die face is represented by a pattern of tods (○) for numbers 1 to 6.
# The function formats the output for each row and adds numbered labels for dice positions.
def print_rolls(roll_list, game_mode_num):
    dice_faces = {
        1: ["[       ]", "[   ○   ]", "[       ]"],
        2: ["[ ○     ]", "[       ]", "[     ○ ]"],
        3: ["[ ○     ]", "[   ○   ]", "[     ○ ]"],
        4: ["[ ○   ○ ]", "[       ]", "[ ○   ○ ]"],
        5: ["[ ○   ○ ]", "[   ○   ]", "[ ○   ○ ]"],
        6: ["[ ○   ○ ]", "[ ○   ○ ]", "[ ○   ○ ]"]
    }

    # Print each row of dice faces for the current roll
    for row in range(3):
        for i in range(1, game_mode_num + 1):
            print(dice_faces[roll_list[i - 1]][row], end=" ")
        print()

    # Print a separator line under the dice faces
    dash_length = (9 * game_mode_num) + (game_mode_num - 1)
    print("-" * dash_length)

    # Print dice position numbers centered below each die
    for a in range(1, game_mode_num + 1):
        print(f"{a:^10}", end="")
    print()


# Function calculates the score for the "Single Digits" category.
# Sums the values in the roll that match "num" and returns the total score.
def single_digits(dice, num):
    score = sum(i for i in dice if i == num)
    return score


# Calculate the score for the "One Pair" category.
# The function finds the highest number that appears at least twice in the roll.
# If such a number exists, it returns the doubled number. Otherwise, returns 0.
def one_pair(dice):
    score = 0
    unique_dice = set(dice) # Get unique roll values to simplify checking for pairs
    sort_dice = sorted(unique_dice, reverse=True) # Sort descending to find largest pairs first

    for num in sort_dice:
        if dice.count(num) >= 2:  # Check if there is a pair
            score = num * 2
            break

    return score


# Calculate the score for the "Two Pairs" category.
# The function searches for the two largest pairs in the roll
# If two pairs are found, it returns their combined score (the pairs should contain different numbers).
# Otherwise, it returns 0.
def two_pairs(dice):
    score = 0
    sort_dice = sorted(dice, reverse=True) # Sort descending to find highest pairs first
    pairs = [] # List to hold pairs' scores

    for num in set(sort_dice): # Check unique values in the roll
        count = dice.count(num)

        # Check if they are four of the same number, which does not work for "Two Pairs"
        if count >= 4:
            return 0

        elif count >= 2:
            pairs.append(num * 2)

            # If two pairs are found, calculate the score
            if len(pairs) == 2:
                score = sum(pairs)
                break

    return score


# Calculates the score for Three Pairs (Maxi-Yatzy only).
# It finds up to 3 distinct pairs and adds their values together.
# Similar logic to the function defined above.
def three_pairs(dice):
    score = 0
    sort_dice = sorted(dice, reverse=True) # Sort dice in descending order to find largest pairs
    pairs = [] # List to store the scores of the pairs found

    for num in set(sort_dice):
        count = dice.count(num)

        if count >= 4:
            return 0

        # If there are at least 2 of the same die - a valid pair
        elif count >= 2:
            pairs.append(num * 2) # Add the score of the pair to the list (value * 2)

            # If 3 pairs are found, return total score
            if len(pairs) == 3:
                score = sum(pairs) # Sum up the scores of the three pairs
                break

    return score # returns 0 if no three pairs were found


# Calculates the score for "Three of a Kind".
# If at least three of the same die are found, their value is multiplied by 3.
def three_of_a_kind(dice):
    score = 0

    # Iterate over each die in the dice list
    for num in dice:
        # If the current die appears 3 or more times, calculate the score
        if dice.count(num) >= 3:
            score = num * 3 # Value of the die * 3
            break

    return score


# Same as above but for 4 appearances ("Four of a kind")
def four_of_a_kind(dice):
    score = 0
    for num in dice:
        if dice.count(num) >= 4:
            score = num * 4
            break

    return score


# Same as above but for five of the same die (Maxi-Yatzy only)
def five_of_a_kind(dice):
    score = 0
    for num in dice:
        if dice.count(num) >= 5: # if there are 5 or more of the same rolls update the score
            score = num * 5
            break

    return score


# Checks if the rolled dice contain the required numbers for "Small Straight".
# Small straight = 1, 2, 3, 4, 5
def small_straight(dice):
    score = 0 
    required_sequence = {1, 2, 3, 4, 5} # Define the required sequence for Small Straight

    # Check if the required sequence is a subset of the rolled dice
    if required_sequence.issubset(dice):
        score = 15 # Sum of the set is 15

    return score


# Same logic as above but for "Large Straight" (2, 3, 4, 5, 6)
def large_straight(dice):
    score = 0 
    required_sequence = {2, 3, 4, 5, 6}

    if required_sequence.issubset(dice):
        score = 20

    return score



# Calculates the score for "Full Straight" (Maxi-Yatzy only).
# Full straight = 1, 2, 3, 4, 5, 6
def full_straight(dice): #for maxi yatzy only
    score = 0
    required_sequence = {1, 2, 3, 4, 5, 6} # Define the required sequence

    if required_sequence.issubset(dice):
        score = 21 # Sum of the numbers in the sequence is 21

    return score


# Calculates the score for "Full House"
# which is a combination of "Three of a Kind" and a "Pair".
def full_house(dice):
    score = 0
    temp = sorted(dice) # Makes pattern matching easier

    # Check for a 5-dice pattern (manually for any possible combination)
    if len(temp) == 5 and len(set(temp)) != 1: # The set should have more than one unique value
        if temp[0] == temp[1] and temp[2] == temp[3] == temp[4]:
            score = temp[0] * 2 + temp[2] * 3
        elif temp[0] == temp[1] == temp[2] and temp[3] == temp[4] and len(set(temp)) != 1:
            score = temp[0] * 3 + temp[3] * 2

        return score

    # Check for a 6-dice pattern (manually for any possible combination)
    elif len(temp) == 6 and len(set(temp)) != 1:
        if temp[0] == temp[1] == temp[2] and temp[3] == temp[4]:
            score = temp[0] * 3 + temp[3] * 2

        elif temp[1] == temp[2] == temp[3] and temp[4] == temp[5]:
            score = temp[1] * 3 + temp[4] * 2

        elif temp[1] == temp[2] and temp[3] == temp[4] == temp[5]:
            score = temp[1] * 2 + temp[3] * 3

        elif temp[0] == temp[1] and temp[3] == temp[4] == temp[5]:
            score = temp[0] * 2 + temp[3] * 3

        elif temp[0] == temp[1] and temp[2] == temp[3] == temp[4]:
            score = temp[0] * 2 + temp[2] * 3

        return score

    return score


# Checks if the dice has two "Three of a Kind" (Maxi-Yatzy)
def villa(dice):
    score = 0
    unique_dice = set(dice)
    triplet = [] # Holds values for any triplets found

    if len(unique_dice) == 1: # If all dice are the same return 0
        return score

    else:
        for num in unique_dice:
            if dice.count(num) == 3: # Check if a number appears exactly 3 times
                triplet.append(num * 3) # Add its "three of a kind" score to the triplet
                if len(triplet) == 2: # If two "three of a kind" patterns are found, calculate the score
                    score = sum(triplet) # Sum of the two triplets
                    return score
    
    return score


# Checks for "Tower" (Maxi-Yatzy).
# A "four of a kind" and a "pair" in the roll.
# If both are found, returns sum of their scores.
def tower(dice):
    score = 0
    unique_dice = set(dice)
    four_numbers = []
    pair = []

    if len(unique_dice) == 1:
        return score

    else:
        for num in unique_dice:
            if dice.count(num) == 4: # If a num appears 4 times it's a "four of a kind"
                four_numbers.append(num * 4)

            if dice.count(num) == 2: # If appears exactly twice, it's a "pair"
                pair.append(num * 2)

    if len(four_numbers) == 1 and len(pair) == 1: # If exactly one "four of a kind" and one "pair" are found
        score = sum(four_numbers) + sum(pair) # Add the scores

    return score


# Calculates "Chance" which is a combination of random numbers (kind of like last resort before crossing out).
def chance(dice):
    score = 0
    for num in dice:
        score += num # Simply the sum of all numbers in the roll

    return score


# Checks if all dice are the same, meaning it's a "YATZY".
# In standard Yatzy this gives 50 points.
# In Maxi-Yatzy - 100 points.
def yatzy(dice, game_mode_number):
    score = 0
    if dice.count(dice[0]) == game_mode_number :
        if game_mode_number == 5:
            score = 50
        elif game_mode_number == 6:
            score = 100

    return score

# Upper keys for upper count
upper_keys = ['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']

# Sum of scores from the upper section categories + bonus check
# Minimal threshold depends on if it's yatzy or maxi yatzy
# 63 for standard and 75 for maxi
def upper_count(score_card, which_player, game_mode_number):
    # Calculate the sum of scores in the upper section for the specified player
    upper_score = sum(
        int(score_card[key][which_player])
        for key in score_card if key in upper_keys and str(score_card[key][which_player]).isdigit()
    )

    if game_mode_number == 5:
        if upper_score >= 63:
            upper_score += 50

    elif game_mode_number == 6:
        if upper_score >= 75:
            upper_score += 50

    return upper_score


# Function calculates the score from the "Lower Section" (simply not "Upper Section")
def lower_count(score_card, which_player):
    lower_score = sum(
        int(score_card[key][which_player])
        for key in score_card if key not in upper_keys and str(score_card[key][which_player]).isdigit()
    )

    return lower_score


# Final score sum for each player depending on if it's maxi yatzy or normal yatzy
def final_score(score_card, which_player, game_mode_number):
    for player_index in range(which_player):
        if game_mode_number == 5:
            upper_score = upper_count(score_card, player_index, 5)
            lower_score = lower_count(score_card, player_index)
            final_score = upper_score + lower_score

        elif game_mode_number == 6:
            upper_score = upper_count(score_card, player_index, 6)
            lower_score = lower_count(score_card, player_index)
            final_score = upper_score + lower_score

        print(f"\nFinal score for Player {player_index + 1}: {final_score}")


# This function allows players to cross out an unused category in the scorecard
# Identifies available (uncrossed) categories, present them to the player, takes their cross out choice
# and updates the scorecard to mark the selected category as crossed out
def cross_out(which_player, score_card):
    available_categories = []

    # Loop through each category and check if it's available to cross out (has '-' in it)
    # then add it to the available categories
    for category in score_card.keys():
        if score_card[category][which_player] == '-':
            available_categories.append(category)

    # Display the available categories with index numbers
    for index, category in enumerate(available_categories, start=1):
        print(f"{index}. {category}")

    # Get the user's choice of a category to cross out by entering its index
    choice = input("\nWhich one would you like to cross out (index)? ").strip()

    # Error handling - check if input is a digit, corresponds to a valid index
    while not choice.isdigit() or int(choice) not in range(1, len(available_categories) + 1):
        print("Invalid input. Please enter an index for an uncrossed category.")
        choice = input("Which category would you like to cross out (index)? ").strip()

    # Convert the valid input to the category name selected by the player
    category_name = available_categories[int(choice) - 1]

    # Update the scorecard by marking the selected category with 'xx' to indicate it is crossed out
    score_card[category_name][which_player] = 'xx'

    # Print confirmation message for the player
    print(f"\nCategory '{category_name}' has been crossed out.")


# Another main game mechanics function
# Gives the user all possible scoring options for the current roll
# Does it by calling each scoring function (defined above) and checking if the output is 0 or not
# If it is not 0 then it is a possible category and the user will be able to choose it
# If no such categories found (all of them either give out 0 or already have a score)
# the user has to cross out a category to keep playing (just like in the actual board game)
# Also lets the user cross out a category whenever they want to
def possible_categories(dice, which_player, score_card, game_mode_type):
    possibilities = [] # Initializing the possibility list

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

        # If the input is a valid number within range, mark the chosen category with the calculated score
        elif choice.isdigit() and 1 <= int(choice) <= len(possibilities):
            choice = int(choice) - 1
            selected_category, selected_score = possibilities[choice]
            score_card[selected_category][which_player] = selected_score

            print(f"You selected '{selected_category}' and scored {selected_score}.")
            break

        else:
            print("Invalid input. Please enter a valid number corresponding to a category or 'x' to cross out a category.")


# Function displays the current scoring sheet for each player with good formatting
# Generates a header with player labels and prints each category's score, adjusting formatting for different score types
def show_scoring_sheet(player_count, score_card):
    print('\nCurrent score sheet:')

    # Create the header row with "Categories" column and a column for each player (P1, P2, ...)
    header = f"|{'Categories':<16s}|" + "".join(f"{'P' + str(p + 1):^6}" + "|" for p in range(player_count))
    print(header)

    # Separator line that matches the header length
    print("-" * (len(header)))

    # Loop through each category in the scorecard to print each row with category name and scores for each player
    for key, value in score_card.items():

        # Build the score line for each player in category
        # Format each player's score:
        # " -- " if the score is still pending ('-')
        # Display a two-digit number if the score is numeric
        # Center the scores
        score_line = "".join(
            f"{'  --  ' if player_score == '-' else f'{int(player_score):02}' 
            if str(player_score).isdigit() else str(player_score).center(6)}".center(6) + "|"
            for player_score in value
        )

        # Print the category name followed by the formatted scores for each player
        print(f'|{key:<16}|' + score_line)

    # Print a final separator line to close the table
    print("-" * len(header))
