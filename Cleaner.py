

class Cleaner():
    def __init__(self, base_dict, categories_list, tags_list):
        self.base_dict = base_dict
        self.categories_list = categories_list
        self.tags_list = tags_list


    def _extract_data(self, data, appid):
        return data[appid]["data"]


    def _get_name(self, game_data):
        return game_data["name"]

    
    def _get_required_age(self, game_data):
        return int(game_data["required_age"])


    def _get_short_description(self, game_data):
        return game_data["short_description"]
    
    
    def _get_detailed_description(self, game_data):
        return game_data["detailed_description"]


    def _is_english(self, game_data):
        return 1 if "English" in game_data["supported_languages"] else 0


    def _is_windows(self, game_data):
        return 1 if game_data["platforms"]["windows"] else 0


    def _is_mac(self, game_data):
        return 1 if game_data["platforms"]["mac"] else 0


    def _is_linux(self, game_data):
        return 1 if game_data["platforms"]["linux"] else 0


    def _get_achievements(self, game_data):
        if "achievements" not in game_data:
            return int(0)
        else:
            return int(game_data["achievements"]["total"])


    def _get_release_date(self, game_data):
        return game_data["release_date"]["date"]

    
    def _get_categories(self, game_data):
        cat_list = [x["description"] for x in game_data["categories"]]
        return cat_list
    

    def _get_genres(self, game_data):
        genre_list = [x["description"] for x in game_data["genres"]]
        return genre_list


    def _get_developer(self, game_data):
        return game_data["developers"][0]
    

    def _get_publisher(self, game_data):
        return game_data["publishers"][0]


    def _assign_categories(self, cat_data, new_dict):
        for i in self.categories_list:
            if i in cat_data:
                new_dict[i] = 1


    def _assign_tags(self, tags_data, new_dict):
        for i in self.tags_list:
            if i in tags_data:
                new_dict[i] = 1


    def clean_data(self, data, appid):
        new_dict = dict(self.base_dict)
        game_data = self._extract_data(data, appid)

        new_dict["name"]  = self._get_name(game_data)
        new_dict["required_age"]  = self._get_required_age(game_data)
        new_dict["desc"] = self._get_short_description(game_data)
        new_dict["english"] = self._is_english(game_data)
        new_dict["windows"] = self._is_windows(game_data)
        new_dict["mac"] = self._is_mac(game_data)
        new_dict["linux"] = self._is_linux(game_data)
        new_dict["achievements"] = self._get_achievements(game_data)
        new_dict["release_date"] = self._get_release_date(game_data)
        new_dict["developer"] = self._get_developer(game_data)

        self._assign_categories(self._get_categories(game_data), new_dict)
        self._assign_tags(self._get_genres(game_data), new_dict)

        return new_dict
        