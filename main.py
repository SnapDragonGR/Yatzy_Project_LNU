import under_the_hood
import time

# proper main function with error handling and possibilities for further maxi yatzy development
def main():
    while True:
        mode = input(
            "Welcome to the Scandinavian Yatzy game. Choose your game mode to start playing ('1' for standard, '2' for Maxi Yatzy, '3' to exit): ")

        if mode == '1':
            dice_num = 5
            while '-' in under_the_hood.score_card.values():
                print("Rolling dice...")
                print()
                dice_list = under_the_hood.rolling_dice(dice_num)
                #time.sleep(2) #makes it easier to read what the final dice roll is without the program moving forward, should be removed for production
                under_the_hood.show_scoring_sheet()
                under_the_hood.possible_categories(dice_list)

            under_the_hood.show_scoring_sheet()
            print("All categories are filled. Game over!")
            final_score = under_the_hood.lower_count() + under_the_hood.upper_count()
            print(f"The final score is: {final_score}")
            print()

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
