import copy

number_of_players = 3  # or more
player_info = {
    "name": "",
    "email": "",
    "country": "",
    "rolls": [],
    "wins": 0
}
players = []
# For loop to obtain the player names:
for i in range(number_of_players):

    # Make a deep copy of the template for this player:
    player = player_info.copy()

    player["name"] = input(f"What is the name of Player {i+1}?")
    player["email"] = input(f"What is the e-mail of Player {i+1}?")
    player["country"] = input(f"What is the country of Player {i+1}?")

    players.append(player)