from under_the_hood import score_card_generate, rolling_dice, show_scoring_sheet, possible_categories, final_score

# Rule set used for maxi-yatzy can be found at https://www.blankettbanken.se/wp-content/uploads/2018/03/maxiyatzy.pdf

# Main function to start the game with a game mode selection and error handling
# Provides options for standard Yatzy, Maxi Yatzy, and exiting the game
def main():
    while True:
        # Ask the user to select a game mode or exit
        mode = input(
            "Welcome to the Scandinavian Yatzy game. Choose your game mode to start playing ('1' for standard, '2' for Maxi Yatzy, '3' to exit): ")

        # Starts standard Yatzy game (5 dice)
        if mode == '1':
            dice_num = 5
            game_logic(dice_num)

        # Starts Maxi Yatzy (6 dice)
        elif mode == '2':
            dice_num = 6
            game_logic(dice_num)

        # Exit option to end the program
        elif mode == '3':
            print("Goodbye!")
            break

        # Invalid input handling in the while True loop
        else:
            print("Invalid input. Please type 1, 2, or 3.")

# The main game logic function that handles player setup, turns, and score tracking
# Takes "dice_num" as a parameter to determine if it's standard or Maxi Yatzy (5 or 6 dice)
def game_logic(dice_num):
    while True:

            # Ask the user to enter the number of players (multiplayer integration) or go back to game mode selection
            # The 5 player limits is artificial, since we based it on the actual game we played in which on one scorecard
            # there was space for 5 players max
            player_count_choice = input(
                "\nPlease enter the number of players (max 5; type 'back' to return to game select): ")
            player_count_choice = player_count_choice.strip().lower()

            # Check if the input is a valid number within the player limit range (1 - 5)
            if player_count_choice.isdigit() and 1 <= int(player_count_choice) <= 5:
                player_count = int(player_count_choice)
                # Generate a new scorecard based on player count and game mode
                score_card = score_card_generate(player_count, dice_num)
                # Track each player's game status (whether they've filled all categories)
                finished_players = [False] * player_count  # Track finished players

                # Main game loop that runs until all players have completed their score sheets
                while any(not finished for finished in finished_players):
                    for player in range(player_count):
                        # Skip the player's turn if they've completed all categories
                        if finished_players[player]:
                            continue  # Skip the player's turn if they are finished

                        # Announce the current player's turn and ROLL the dice
                        print(f"\nPlayer {player + 1}'s turn:")
                        print("Rolling dice...")
                        print()
                        dice_list = rolling_dice(dice_num)

                        # Display the current scoring sheet for all players
                        show_scoring_sheet(player_count, score_card)
                        # Display available scoring categories based on the dice roll
                        possible_categories(dice_list, player, score_card, dice_num)

                        # Check if the player has filled all categories to mark them as finished
                        if all(score_card[cat][player] != '-' for cat in score_card):
                            finished_players[player] = True  # Mark player as finished
                            print(f"Player {player + 1} has finished the game!")

                # Once all players have finished, display the final scoring sheet
                show_scoring_sheet(player_count, score_card)
                print("\nAll categories are filled. Game over!")

                # Calculate and display the final scores for each player
                final_score(score_card, player_count, dice_num)

            # Return to the game mode selection if the user types "back"
            elif player_count_choice == 'back':
                break

            # Handle invalid inputs for player count selection
            else:
                print("Invalid input. Please enter the number of players or 'back' to return to game select.")


# Entry point of the program, starts the main function
if __name__ == '__main__':
    main()
