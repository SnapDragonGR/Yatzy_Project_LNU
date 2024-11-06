import under_the_hood

player_count = 1

score_card = {
        'Ones': ['-'] * player_count , 'Twos': ['-'] * player_count, 'Threes': ['-'] * player_count, 'Fours': ['-'] * player_count, 'Fives': ['-'] * player_count,
        'Sixes': ['-'] * player_count, 'One Pair': ['-'] * player_count, 'Two Pairs': ['-'] * player_count, 'Three of a Kind': ['-'] * player_count,
        'Four of a Kind': ['-'] * player_count, 'Small Straight': ['-'] * player_count,
        'Large Straight': ['-'] * player_count, 'Full House': ['-'] * player_count, 'Chance': ['-'] * player_count, 'Yatzy': ['-'] * player_count
        }

def norm_yatzi_tests():
    dice_list = [1,2,3,4,5] #should trigger small straight, and ones
    print(dice_list)
    under_the_hood.possible_categories(dice_list, 0, score_card, 5)

    dice_list = [2,3,4,5,6] #should trigger large straight and ones
    print(dice_list)
    under_the_hood.possible_categories(dice_list, 0, score_card, 5)

    dice_list = [2,2,3,4,5] #should trigger one pair and ones 
    print(dice_list)
    under_the_hood.possible_categories(dice_list, 0, score_card, 5)

    dice_list = [2,2,2,3,4] #should trigger theree of a kind, one pair and ones
    print(dice_list)
    under_the_hood.possible_categories(dice_list, 0, score_card, 5)

    dice_list = [2,2,1,1,4] #should trigger two pairs, one pair, ones 
    print(dice_list)
    under_the_hood.possible_categories(dice_list, 0, score_card, 5)

    dice_list = [2,2,2,2,2] #should trigger yatzy, four of a kind, three of a kind, one pair, ones
    print(dice_list)
    under_the_hood.possible_categories(dice_list, 0, score_card, 5)

    dice_list = [2,2,2,1,1] #should be full_house, there of a kind, two pair, one pair 
    print(dice_list)
    under_the_hood.possible_categories(dice_list, 0, score_card, 5)

    dice_list = [2,2,2,2,1] # should trigger four of a kind, two pair and one pair 
    print(dice_list)
    under_the_hood.possible_categories(dice_list, 0, score_card, 5)

"""
Yatzy:
1.Small Straight test passed 
2.Large straight test passed
3.one pair test passed
4.three of a kind test passed 
5.two pairs test passed
6.full house test passed 
7.four of a kind passed
8.yatzy test passed
9.ones test passed 
10.chance passed
"""
norm_yatzi_tests()
