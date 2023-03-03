import os
from dotenv import load_dotenv

class Virustotal:

    def __init__(self, message = "", headers = {}) -> None:
        self.message = "hello virustotal"
        self.headers = headers
    
    def read_env(self):
        # headers consist of - Virustotal API Key and Application Type
        # reading this values form .env file
        def define_headers():       
            self.headers["accept"], self.headers["x-apikey"] = "application/json", os.getenv("VIRUSTOTAL_API_KEY")
            return self.headers
        
        if load_dotenv(".env") != True: print("Loading dotenvfile fialed")
        else:
            define_headers()
            print("Headers for Virustoal API created succesfully")
            return

    
    def test(self):
        return self.message

