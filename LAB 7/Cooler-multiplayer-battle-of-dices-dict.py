import random
import copy

# Dice rolling function
def roll_dice():
    return random.randint(1, 6)

# Game setup
WINNING_SCORE = 3
players = []
rounds_played = 0
game_over = False

# Player info template
player_info_template = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []
}

# Get player information
print("🎲 Welcome to Multiplayer Battle of Dices! 🎲")
num_players = int(input("Enter the number of players: "))

for i in range(num_players):
    player = copy.deepcopy(player_info_template)
    player["name"] = input(f"Enter name for player {i + 1}: ")
    player["email"] = input(f"Enter email for player {i + 1}: ")
    player["country"] = input(f"Enter country for player {i + 1}: ")
    players.append(player)

# Main game loop
while not game_over:
    print(f"\nRound {rounds_played + 1}")
    input("Press Enter to roll the dice...")

    current_rolls = []
    for player in players:
        roll = roll_dice()
        player["rolls"].append(roll)
        current_rolls.append(roll)
        print(f"{player['name']} rolled a {roll}")

    # Determine round winners
    max_roll = max(current_rolls)
    winners = []
    for i, player in enumerate(players):
        if player["rolls"][-1] == max_roll:
            player["wins"] += 1
            winners.append(player["name"])

    print(f"Winners of this round: {', '.join(winners)}")

    # Check for overall winner
    for player in players:
        if player["wins"] >= WINNING_SCORE:
            print(f"\n {player['name']} is the Battle of Dices Champion! 🎉")
            game_over = True
            break

    rounds_played += 1

# Save results to a file
filename = input("\nEnter the filename to save the results: ")
with open(filename, "w") as file:
    file.write("Player Information:\n")
    for player in players:
        file.write(
            f"Name = {player['name']}\n"
            f"Email = {player['email']}\n"
            f"Country = {player['country']}\n"
            f"Wins = {player['wins']}\n"
        )

    file.write("Game Results:\n\n")
    for r in range(rounds_played):
        round_summary = ", ".join(
            f"{player['name']} rolled {player['rolls'][r]}"
            for player in players
        )
        file.write(f"Round {r + 1}: {round_summary}\n\n")

print("\nGame over! Results saved successfully.")
