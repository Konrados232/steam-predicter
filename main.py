import json
import os
from APIHandler import APIHandler

def beautify_json(data):
    print(json.dumps(data, indent=4))

appid_list = []

# https://store.steampowered.com/api/appdetails?appids=578080&l=en

base_url = r"https://store.steampowered.com/api/appdetails?appids="
flags = [r"l=en"]

handler = APIHandler(base_url, flags)

appinfo = handler.fetch_info(578080)

beautify_json(appinfo)

