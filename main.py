import under_the_hood

def main():
    while True:
        mode = int(input(
            "Welcome to the Scandinavian Yatzy game. Choose your game mode to start playing (1 for standard, 2 for Maxi Yatzy): "))
        if mode == 1:
            dice_num = 5
            while any(isinstance(value, str) for value in under_the_hood.score_card.values()):
                print('Rolling dice...')
                roll = under_the_hood.rolling_dice(dice_num)  # 5 need to be a variable so we can easily integrate multiplayer
                under_the_hood.possible_categories(roll)

        elif mode == 2:
            pass

        else:
            print('Invalid mode! Please enter 1 or 2.')

if __name__ == '__main__':
    main()
