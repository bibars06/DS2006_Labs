# Battle of Dices (cooler) is going to be an amazing 2 player game, 

# where two players face each other using only their sheer luck! 

# The rules are:
# Each player throws D4 and D6.
# The player with the highest roll wins the round.  
# The first player to win 10 times is the winner.


import random

def rollD4():
    return random.randint(1, 4)

def rollD6():
    return random.randint(1, 6)


print("Welcome to the battle of dices (better)")

# Initialize variables to track wins
player1_wins = 0
player2_wins = 0
Rounds_played = 0

while player1_wins <10 and player2_wins < 10:
    input("Press ENTER to roll the dice...")

    player1_roll = rollD6() + rollD4()
    print("Player 1 rolled:", player1_roll)

    player2_roll = rollD6() + rollD4() 
    print("Player 2 rolled:", player2_roll)

    input("\nPress ENTER to continue...")

    # Decide winner for the round
    if player1_roll > player2_roll:
        player1_wins += 1
        print("Player 1 wins this round!\n")
    elif player2_roll > player1_roll:
        player2_wins += 1
        print("Player 2 wins this round!\n")
    else:
        print("It's a tie!\n")

    # Increment rounds inside the loop
    Rounds_played += 1

# Final result
print("=== Final Result ===")
if player1_wins == 10:
    print(f"Player 1 is the overall winner! ({player1_wins} - {player2_wins})")
    print(f"It took {Rounds_played} rounds for Player 1 to win the game!")
elif player2_wins == 10:
    print(f"Player 2 is the overall winner! ({player2_wins} - {player1_wins})")
    print(f"It took {Rounds_played} rounds for Player 2 to win the game!")
else:
    print(f"The game is a tie! ({player1_wins} - {player2_wins})")