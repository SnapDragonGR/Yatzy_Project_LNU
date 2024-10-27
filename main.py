import under_the_hood


#debugging code
game_mode_num = 5
under_the_hood.rolling_dice(game_mode_num)

def main():
    while any(isinstance(value, str) for value in under_the_hood.score_card.values()):
        print('Rolling dice...')
        under_the_hood.rolling_dice(game_mode_num) #5 need to be a variable so we can easily integrate multiplayer