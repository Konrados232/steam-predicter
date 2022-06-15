import json
import os
import pandas as pd
from GameList import GameList

# # https://store.steampowered.com/api/appdetails?appids=578080&l=en

game_list = GameList()

game_list.add_game(1150690, 100_000, 1, 19.99)
game_list.add_game(274520, 50_000, 1, 14.99)
game_list.add_game(374320, 2_000_000, 1, 59.99)
game_list.add_game(1142710, 50_000, 1, 53.99)
game_list.add_game(445870, 10_000, 0, 14.99)
game_list.add_game(1171120, 10_000, 0, 9.99)
game_list.add_game(1245620, 3_000_000, 1, 59.99) # Elden Ring
game_list.add_game(413150, 500_000, 1, 14.99) # Stardew Valley
game_list.add_game(201790, 40_000, 1, 14.99) # Orcs Must Die 2
game_list.add_game(49520, 1_000_000, 1, 29.99) # Borderlands 2
game_list.add_game(620, 1_000_000, 1, 9.99) # Portal 2
game_list.add_game(892970, 500_000, 1, 19.99) # Valheim
game_list.add_game(294100, 500_000, 1, 29.99) # Rimworld
game_list.add_game(239160, 1_000_000, 0, 24.99) # Thief
game_list.add_game(236850, 1_000_000, 0, 299.99) # eu

game_list.clean_data()

df = game_list.convert_to_df()
test_path = os.path.join("test.csv")
df.to_csv(test_path)

