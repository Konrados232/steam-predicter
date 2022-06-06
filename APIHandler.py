import json
import requests
from howlongtobeatpy import HowLongToBeat


class APIHandler():
    def __init__(self, url, flags):
        self.base_ulr = url
        self.additional_flags = flags
    

    def _make_url_with_id(self, appid):
        flags_combined = "&".join(self.additional_flags)
        return f"{self.base_ulr}{appid}&{flags_combined}"


    def fetch_steam_info(self, appid):
        f = requests.get(self._make_url_with_id(appid))
        return json.loads(f.text)


    def fetch_howlongtobeat_info(self, app_name):
        results = HowLongToBeat().search(app_name)
        if results is not None and len(results) > 0:
            best_element = max(results, key=lambda element: element.similarity)
            return best_element
        else:
            return None
            