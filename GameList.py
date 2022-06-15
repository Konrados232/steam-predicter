import pandas as pd
from APIHandler import APIHandler
from Cleaner import Cleaner


class GameList():

    def __init__(self):
        base_dict = {
            "english" : 0,
            "windows" : 0,
            "mac" : 0,
            "linux" : 0,
            "achievements" : 0,
            "average_playtime" : 0,
            "median_playtime" : 0,
            "owners" : 0,
            "price" : 0,
            "Indie" : 0,
            "Action" : 0,
            "Adventure" : 0,
            "Casual" : 0,
            "Strategy" : 0,
            "Simulation" : 0,
            "RPG" : 0,
            "Early Access" : 0,
            "Free to Play" : 0,
            "Puzzle" : 0,
            "Racing" : 0,
            "VR" : 0,
            "Sports" : 0,
            "Anime" : 0,
            "Visual Novel" : 0,
            "Platformer" : 0,
            "Point & Click" : 0,
            "Horror" : 0,
            "Nudity" : 0,
            "FPS" : 0,
            "Multiplayer" : 0,
            "Sexual Content" : 0,
            "Violent" : 0,
            "Gore" : 0,
            "Massively Multiplayer" : 0,
            "Hidden Object" : 0,
            "Open World" : 0,
            "Survival" : 0,
            "Pixel Graphics" : 0,
            "Space" : 0,
            "Female Protagonist" : 0,
            "Shoot 'Em Up" : 0,
            "RTS" : 0,
            "Classic" : 0,
            "Turn-Based" : 0,
            "Arcade" : 0,
            "Sci-fi" : 0,
            "Story Rich" : 0,
            "Tower Defense" : 0,
            "Zombies" : 0,
            "Singleplayer" : 0,
            "World War II" : 0,
            "Card Game" : 0,
            "RPGMaker" : 0,
            "Great Soundtrack" : 0,
            "Management" : 0,
            "Co-op" : 0,
            "Fighting" : 0,
            "2D" : 0,
            "Turn-Based Strategy" : 0,
            "Fantasy" : 0,
            "Utilities" : 0,
            "Rogue-like" : 0,
            "Sandbox" : 0,
            "JRPG" : 0,
            "Board Game" : 0,
            "Retro" : 0,
            "Stealth" : 0,
            "Comedy" : 0,
            "Shooter" : 0,
            "Music" : 0,
            "Hack and Slash" : 0,
            "Bullet Hell" : 0,
            "Atmospheric" : 0,
            "First-Person" : 0,
            "City Builder" : 0,
            "Historical" : 0,
            "Psychological Horror" : 0,
            "Family Friendly" : 0,
            "Memes" : 0,
            "Match 3" : 0,
            "Mystery" : 0,
            "Difficult" : 0,
            "Local Multiplayer" : 0,
            "Driving" : 0,
            "Design & Illustration" : 0,
            "Cyberpunk" : 0,
            "Flight" : 0,
            "Building" : 0,
            "Clicker" : 0,
            "Walking Simulator" : 0,
            "Metroidvania" : 0,
            "Education" : 0,
            "Single-player" : 0,
            "Steam Achievements" : 0,
            "Steam Trading Cards" : 0,
            "Steam Cloud" : 0,
            "Full controller support" : 0,
            "Multi-player" : 0,
            "Partial Controller Support" : 0,
            "Steam Leaderboards" : 0,
            "Online Multi-Player" : 0,
            "Shared/Split Screen" : 0,
            "Stats" : 0,
            "Co-op" : 0,
            "Local Multi-Player" : 0,
            "Cross-Platform Multiplayer" : 0,
            "Online Co-op" : 0,
            "Includes level editor" : 0,
            "Steam Workshop" : 0,
            "Local Co-op" : 0,
            "Captions available" : 0,
            "In-App Purchases" : 0,
            "MMO" : 0,
            "VR Support" : 0,
            "Commentary available" : 0,
            "Valve Anti-Cheat enabled" : 0,
            "Steam Turn Notifications" : 0,
            "SteamVR Collectibles" : 0,
            "Includes Source SDK" : 0,
            "Mods" : 0,
            "desc" : "a",
            "name" : "a",
            "developer" : "a",
            "release_date" : "a",
            "appid" : 0,
            "user_reviews" : 0
        }
        categories_list = ["Single-player", "Steam Achievements", "Steam Trading Cards", "Steam Cloud", "Full controller support", "Multi-player", "Partial Controller Support", "Steam Leaderboards", "Online Multi-Player", "Shared/Split Screen", "Stats", "Co-op", "Local Multi-Player", "Cross-Platform Multiplayer", "Online Co-op", "Includes level editor", "Steam Workshop", "Local Co-op", "Captions available", "In-App Purchases", "MMO", "VR Support", "Commentary available", "Valve Anti-Cheat enabled", "Steam Turn Notifications", "SteamVR Collectibles", "Includes Source SDK", "Mods"]
        tags_list = ["Indie", "Action", "Adventure", "Casual", "Strategy", "Simulation", "RPG", "Early Access", "Free to Play", "Puzzle", "Racing", "VR", "Sports", "Anime", "Visual Novel", "Platformer", "Point & Click", "Horror", "Nudity", "FPS", "Multiplayer", "Sexual Content", "Violent", "Gore", "Massively Multiplayer", "Hidden Object", "Open World", "Survival", "Pixel Graphics", "Space", "Female Protagonist", "Shoot 'Em Up", "RTS", "Classic", "Turn-Based", "Arcade", "Sci-fi", "Story Rich", "Tower Defense", "Zombies", "Singleplayer", "World War II", "Card Game", "RPGMaker", "Great Soundtrack", "Management", "Co-op", "Fighting", "2D", "Turn-Based Strategy", "Fantasy", "Utilities", "Rogue-like", "Sandbox", "JRPG", "Board Game", "Retro", "Stealth", "Comedy", "Shooter", "Music", "Hack and Slash", "Bullet Hell", "Atmospheric", "First-Person", "City Builder", "Historical", "Psychological Horror", "Family Friendly", "Memes", "Match 3", "Mystery", "Difficult", "Local Multiplayer", "Driving", "Design & Illustration", "Cyberpunk", "Flight", "Building", "Clicker", "Walking Simulator", "Metroidvania", "Education"]
        base_url = r"https://store.steampowered.com/api/appdetails?appids="
        flags = [r"l=en"]

        self.data_cleaner = Cleaner(base_dict, categories_list, tags_list)
        self.handler = APIHandler(base_url, flags)

        self.game_list = []
        self.appids = []



    def add_game(self, appid, owners, user_reviews, price):
        self.game_list.append((appid, owners, user_reviews, price))
        self.appids.append([appid, None])

    def clean_data(self):
        for count, appid in enumerate(self.game_list, 0):
            appinfo = self.handler.fetch_steam_info(appid[0])
            cleaned_data = self.data_cleaner.clean_data(appinfo, str(appid[0]))

            cleaned_data["appid"] = appid[0]

            playtime_data = self.handler.fetch_howlongtobeat_info(cleaned_data["name"])

            if playtime_data == None:
                cleaned_data["average_playtime"] = 20
                cleaned_data["median_playtime"] = 20
            else:
                playtime_hours = playtime_data.gameplay_main

                if "½" in playtime_hours:
                    playtime_hours = playtime_hours[:-1]

                playtime_hours = int(playtime_hours)

                cleaned_data["average_playtime"] = playtime_hours
                cleaned_data["median_playtime"] = playtime_hours
            
                cleaned_data["owners"] = self.game_list[count][1]
                cleaned_data["user_reviews"] = self.game_list[count][2]
                cleaned_data["price"] = self.game_list[count][3]


            self.appids[count][1] = cleaned_data

    def convert_to_df(self):
        emp = []
        for i, smh in enumerate(self.appids):
            emp.append(self.appids[i][1])

        print(emp)
        df = pd.DataFrame(emp)

        print(df)

        return df
        