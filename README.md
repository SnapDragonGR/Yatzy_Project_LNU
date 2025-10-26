# Swedish Yatzy Game (Python)

This is a Python-based text user interface (CUI) implementation of **Scandinavian Yatzy**. This project was created as a final project for the "Introduction to Programming" course.

This application fully supports two different game modes, Standard Yatzy (5 dice) and Maxi Yatzy (6 dice), with automated scoring logic for all combinations.

## Table of Contents

- [About the Game](#about-the-game)
- [Features](#features)
- [How to Run](#how-to-run)
- [Game Instructions](#game-instructions)
- [Project Structure](#project-structure)
- [Game Rules](#game-rules)
- [Error Handling](#error-handling)
- [Credits](#credits)

## About the Game

Scandinavian Yatzy is a dice game where players roll dice up to three times per turn, aiming to achieve specific combinations to score points. The game ends after each scoring category is filled, and the player's score is tallied based on these combinations.

This version can be played by 1 to 5 players.

## Features

- **Dual Game Modes:** Choose between Standard Yatzy (5 dice) or Maxi Yatzy (6 dice) at the start of the game
- **Multiplayer Support:** Play solo or with up to 5 players
- **Full Turn Logic:** Roll dice up to three times per turn, with the ability to "keep" specific dice and re-roll the others
- **Automated Score Calculation:** The complex logic for all 20+ scoring categories is handled automatically
  - **Standard (5-Dice) Categories:** Includes all standard rules like Full House, Small Straight, Large Straight, and Yatzy
  - **Maxi (6-Dice) Categories:** Implements all advanced Maxi Yatzy rules, including **Three Pairs**, **Five of a Kind**, **Full Straight**, **Villa** (two triplets), and **Tower** (a pair + four of a kind)
- **Dynamic Score Helper:** After each roll, the game displays a list of all *possible* scoring categories you have achieved, helping you make the best choice
- **"Cross Out" Functionality:** If no valid score can be placed, the game allows you to "cross out" (mark as 'xx') any available category, just like the real game
- **Clean CUI:** Features a formatted, easy-to-read ASCII dice display and a persistent scoreboard that updates after every turn

## How to Run

This project runs in any standard Python 3 environment.

1. Clone or download the repository to your local machine
2. Navigate to the project directory in your terminal:
   ```sh
   cd path/to/Yatzy_Project_LNU
   ```
3. Run the main file:
   ```sh
   python main.py
   ```
4. The game will start, and you will be prompted to choose your game mode and number of players

## Game Instructions

1. Start the game by running `main.py`
2. Choose your game mode: '1' for Standard (5 dice) or '2' for Maxi Yatzy (6 dice)
3. Enter the number of players (1-5)
4. On your turn, the dice will roll automatically. You can re-roll up to two more times
5. To re-roll, you can type 'a' to re-roll all dice, or type the position of the dice you want to re-roll (e.g., `1,3,5`)
6. After your rolls are complete, the game will show you all possible scoring options
7. Select a scoring category by its number, or type 'x' to cross out a category you can't (or don't want to) use
8. The game continues until all players have filled all categories
9. Final scores are tallied (including bonuses) and a winner is announced

## Project Structure

- `main.py`: The main entry point for the game. Contains the top-level game loop, player/mode selection, and turn management
- `under_the_hood.py`: The core logic module. Contains all scoring functions, the dice rolling/printing mechanics, scoreboard generation, and the `possible_categories` helper
- `test_cases.py`: A simple script for testing and verifying the output of the scoring functions

## Game Rules

### 1. Standard Yatzy (5 Dice)

- **Upper section**: Ones, Twos, Threes, Fours, Fives, Sixes
- **Lower section**: One Pair, Two Pairs, Three of a Kind, Four of a Kind, Small Straight (1-5), Large Straight (2-6), Full House (Pair + Triplet), Chance, Yatzy (Five of a Kind)
- **Bonus**: A bonus of 50 points is awarded if you score 63 or more in the upper section

### 2. Maxi Yatzy (6 Dice)

Based on the official rules for 6-dice Maxi Yatzy.

- **Upper section**: Ones, Twos, Threes, Fours, Fives, Sixes
- **Lower section**:
  - **One Pair**: Highest pair
  - **Two Pairs**: Two highest pairs
  - **Three Pairs**: Three distinct pairs
  - **Three of a Kind**: Three dice with the same value
  - **Four of a Kind**: Four dice with the same value
  - **Five of a Kind**: Five dice with the same value
  - **Small Straight**: 1-2-3-4-5
  - **Large Straight**: 2-3-4-5-6
  - **Full Straight**: 1-2-3-4-5-6
  - **Full House**: A set of three combined with a different pair
  - **Villa**: Two sets of three (e.g., 4-4-4 + 2-2-2)
  - **Tower**: A set of four combined with a pair (e.g., 5-5-5-5 + 1-1)
  - **Chance**: Sum of all dice
  - **Yatzy**: Six of a kind. Scores 100 points
- **Bonus**: A bonus of 50 points is awarded if you score 75 or more in the upper section

## Error Handling

- The application includes robust input validation to prevent crashes
- Ensures valid inputs for dice selection (e.g., `1,3,5` or `a`) and scoring choices (a valid index number or 'x')
- Displays an error message and re-prompts the player if an invalid input is detected

## Credits

- Developed by: Abhinav Mugudu (Abhinav5132), Gleb Razumnyi (SnapDragonGR)
- Course: Introduction to Programming
