import under_the_hood

# proper main function with error handling and possibilities for further maxi yatzy development
def main():
    while True:
        mode = input(
            "Welcome to the Scandinavian Yatzy game. Choose your game mode to start playing ('1' for standard, '2' for Maxi Yatzy, '3' to exit): ")

        if mode == '1':
            
            while True:
                player_count_choice = input("Please enter the number of players (max 5, back - to return to game select):") #there is technically nothing restricting how many players play the game, 5 just makes it match with the physical game
                player_count_choice = player_count_choice.strip().lower()
                if player_count_choice.isdigit() and int(0 < int(player_count_choice) <= 5): 
                    
                    player_count = int(player_count_choice)
                    score_card = under_the_hood.score_card_generate(player_count)
                    
                    dice_num = 5
                    while any("-" in score for score in score_card.values()): #even if player one has won the game will continue cuz player 2 might not have finished
                        #this completely breaks the game because player 1 has no possibilites, which triggers the the cross out, so player 1 is forcd to cross out a colum
                        for player in range(int(player_count)):
                            print(f"Player {player+1}'s turn:")
                            print("Rolling dice...")
                            print()
                            dice_list = under_the_hood.rolling_dice(dice_num)
                            
                            under_the_hood.show_scoring_sheet(player_count, score_card)
                            under_the_hood.possible_categories(dice_list, player, score_card)

                    under_the_hood.show_scoring_sheet(player_count, score_card)
                    print("All categories are filled. Game over!")
                    final_score = under_the_hood.lower_count(score_card) + under_the_hood.upper_count(score_card)
                    print(f"The final score is: {final_score}")
                    print()
                elif player_count_choice == "back":
                    break 
                    
                else:
                    print("Invalid input, please enter a number between 1 and 5")

        elif mode == '2':
            # further development for Maxi Yatzy
            pass

        elif mode == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid input. Please type 1, 2, or 3.")


if __name__ == '__main__':
    main()
