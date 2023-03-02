import random

# Define the game options
options = ['rock', 'paper', 'scissors']

# Ask the player to make a move
player_move = input("Enter your move (rock/paper/scissors): ").lower()

# Check if the player's move is valid
if player_move not in options:
    print("Invalid move!")
else:
    # Generate a random move for the computer
    computer_move = random.choice(options)

    # Print the computer's move
    print(f"The computer chose {computer_move}.")

    # Determine the winner of the game
    if player_move == computer_move:
        print("It's a tie!")
    elif player_move == 'rock' and computer_move == 'scissors':
        print("You win!")
    elif player_move == 'paper' and computer_move == 'rock':
        print("You win!")
    elif player_move == 'scissors' and computer_move == 'paper':
        print("You win!")
    else:
        print("You lose!")
