# battle-of-dices-bad-not-rigged

import random

player1_wins = 0
player2_wins = 0
player1_rolls = []
player2_rolls = []
Rounds=10

#Track wins
for round_num in range(1, Rounds + 1):
    input(f"\nPress ENTER to roll the dice for Round {round_num}...")

    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)

    
    player1_rolls.append(roll1)
    player2_rolls.append(roll2)


    print(f"Player 1 rolled: {roll1}")
    print(f"Player 2 rolled: {roll2}")

    input("\nPress ENTER to continue...")

# Decide winner for the round

    if roll1 > roll2:
        player1_wins += 1
        print(f"Player 1 wins Round {round_num}\n")
    elif roll2 > roll1:
        player2_wins += 1
        print(f"Player 2 wins Round {round_num}\n")
    else:
        print("It's a tie!\n")

#Game over
print("\nGAME OVER")
for i in range(Rounds):
    print(f"Round {i+1}: Player 1 rolled {player1_rolls[i]}, Player 2 rolled {player2_rolls[i]}")


# Final result
print("\nFinal result:")
print("Player 1 wins:", player1_wins)
print("Player 2 wins:", player2_wins)

if player1_wins > player2_wins:
    print(" Player 1 is the winner!")
elif player2_wins > player1_wins:
    print(" Player 2 is the winner!")
else:
    print("It's a tie overall!")

#Name the file
filename=input("Enter the filename to save the results:")
with open(filename, "w") as file:
    for i in range (len(player1_rolls)):
        file.write(f"round{i+1}:player 1 rolled{player1_rolls[i]}, player 2 rolled {player2_rolls[i]}\n")