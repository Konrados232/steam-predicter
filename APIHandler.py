import json
import requests

class APIHandler():
    def __init__(self, url, flags):
        self.base_ulr = url
        self.additional_flags = flags
    

    def _make_url_with_id(self, id):
        flags_combined = "&".join(self.additional_flags)
        return f"{self.base_ulr}{id}&{flags_combined}"


    def fetch_info(self, appid):
        f = requests.get(self._make_url_with_id(appid))
        return json.loads(f.text)

