import os, requests
from dotenv import load_dotenv

class Virustotal:

    def __init__(self, target_info = {}, menu = {}, headers = {}) -> None:
        self.target_info = target_info
        self.menu = {
            "menu_item": "command"
        }

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
    
    def force_virustotal_subdomain_scan(self):
        self.read_env()

        if self.target_info != {}:
            target_domain = self.target_info.get("target_domain") 
            url = f"https://www.virustotal.com/api/v3/domains/{target_domain}/subdomains?limit=100"
        else: print("Something went wrong while initializing target domain")

        def manipulate_response(url: str):
            try:
                virustotal_server_respose = requests.get(url, headers=self.headers)
                if virustotal_server_respose.status_code == 200: print("Website is up and running")
                else: print(f"Error accessing website. Status code: {virustotal_server_respose.status_code}")
                with open("./data/vt_subdomains.json", "w") as file: 
                    print("Subdomains JSON file successfully loaded")
                    return file.write(virustotal_server_respose.text)
            except Exception as e:
                print("Error requesting virustotal server")
                return

        manipulate_response(url=url)
    
    

    def get_menu():
        pass
    
    def test(self):
        print(self.target_info)

