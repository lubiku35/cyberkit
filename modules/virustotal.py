

class Virustotal:

    def __init__(self, target_info, api_key, headers = {}) -> None:
        self.target_info = target_info
        self.api_key = api_key
        self.headers = headers

    def create_headers(self):
        self.headers["x-apikey"] = self.api_key
        return self.headers
    
    def check(self):
        self.create_headers()
        print(self.target_info)
        print(self.api_key)
        print(self.headers)