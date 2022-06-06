

class Cleaner():
    def __init__(self, categories_list):
        self.categories_list = categories_list


    def _extract_data(self, data, appid):
        return data[appid]["data"]


    def _get_name(self, game_data):
        return game_data["name"]

    
    def _get_required_age(self, game_data):
        return int(game_data["required_age"])


    def _get_description(self, game_data):
        return game_data["short_description"]


    def _is_english(self, game_data):
        return 1 if "English" in game_data["supported_languages"] else 0


    def _is_windows(self, game_data):
        return 1 if game_data["platforms"]["windows"] else 0


    def _is_mac(self, game_data):
        return 1 if game_data["platforms"]["mac"] else 0


    def _is_linux(self, game_data):
        return 1 if game_data["platforms"]["linux"] else 0


    def _get_achievements(self, game_data):
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



    def clean_data(self, data, appid):
        game_data = self._extract_data(data, appid)

        name = self._get_name(game_data)
        print(name)

        age = self._get_required_age(game_data)
        print(age)

        desc = self._get_description(game_data)
        print(desc)

        eng = self._is_english(game_data)
        print(eng)

        win = self._is_windows(game_data)
        print(win)

        mac = self._is_mac(game_data)
        print(mac)

        lin = self._is_linux(game_data)
        print(lin)

        ach = self._get_achievements(game_data)
        print(ach)

        rd = self._get_release_date(game_data)
        print(rd)

        catt = self._get_categories(game_data)
        print(catt)

        genn = self._get_genres(game_data)
        print(genn)

        dev = self._get_developer(game_data)
        print(dev)

        pub = self._get_publisher(game_data)
        print(pub)


