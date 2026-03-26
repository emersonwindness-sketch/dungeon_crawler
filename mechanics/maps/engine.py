def display_room(player_choice, world):
    player_choice = world[player_choice]
    print (player_choice["description"])
    choices = ", " .join(player_choice["choice"])
    print (f"Exits: {choices}")

