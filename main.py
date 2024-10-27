import under_the_hood

# proper main function with error handling and possibilites for further maxi yatzy development
def main():
    while True:
        mode = input(
            "Welcome to the Scandinavian Yatzy game. Choose your game mode to start playing ('1' for standard, '2' for Maxi Yatzy, '3' to exit): ")

        if mode == '1':
            dice_num = 5
            while not all(isinstance(value, int) for value in under_the_hood.score_card.values()):
                print("Rolling dice...")
                print()
                under_the_hood.rolling_dice(dice_num)  # 5 need to be a variable so we can easily integrate multiplayer
            print("All categories are filled. Game over!")

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
