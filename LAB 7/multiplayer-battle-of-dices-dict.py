import random 

def roll_dice():
    return random.randint(1, 6)

Winning_score = 3
player_names= []
player_wins = []
rounds = 0
game_over = False

# Dictionary template for storing player information
player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []
}

players = []

# Obtain the number of players
num_players = int(input("Enter the number of players: "))

# For loop to gather player names
for i in range(num_players):
    player = player_info.copy()  # Create a copy of the template for each player
    player["name"] = input(f"Enter name for player {i + 1}: ")
    player["email"] = input(f"Enter email for player {i + 1}: ")
    player["country"] = input(f"Enter country for player {i + 1}: ")
    players.append(player)
    
# Repeat rounds until a player wins
while game_over is False:
    print (f"Round {rounds + 1}")
    input("Press Enter to roll the dice...")
    
    current_rolls = []
    
    for each_player in players:
        roll = roll_dice()
        each_player["rolls"].append(roll)
        current_rolls.append((each_player["name"], roll))
        print(f"{each_player['name']} rolled a {roll}")
        
    # oBtain the highest roll
    max_roll = max(current_rolls)
    
    winners =[]
    
    for each_player in players:
        if (each_player["rolls"][-1] == max_roll[1]):
            each_player["wins"] += 1
            print(f"{each_player['name']} wins this round {rounds}!")

            winners.append(each_player["name"])
print (f"Winners of this round: {winners}")

for each_player in player:
    if (each_player["wins"]>= Winning_score):
        print(f"\n {each_player['name']} is tge newest Battle of Dices Champion!!")
        game_over = True

if game_over is False:
    print ("This heated battle of Dices is still going on! who will win in the end")
rounds +=1

# Save results to a file
filename = input("Enter the filename to save the results: ")
with open(filename, "w") as file:  # "w" = write mode
    file.write("Player Information:\n\n")

    # Saves each player information using python automatically concatenation
    # of adjacent strings
    for each_player in players:
        file.write(
            f"Name = {each_player['name']}\n"
            f"Age = {each_player['age']}\n"
            f"Country = {each_player['country']}\n"
            f"Wins = {each_player['wins']}\n\n"
        )

    # ... still in with open
    file.write("\nGame rounds\n")

    # Round history
    for r in range(rounds):
        file.write(f"Round {r+1}:\n")

        # Start with empty text for this round
        rolls_str = ""

        # Go through each player and build the string step by step
        for i, each_player in enumerate(players):
            rolls_str += f"{each_player['name']} rolled {each_player['rolls'][r]}"

            # Add a comma and space unless it's the last player
            if i < (len(players) - 1):
                rolls_str += ", "

        # Save the entire round info to the file
        file.write(rolls_str + "\n\n")

print("\nGame over! Results saved successfully.")
