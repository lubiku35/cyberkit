import requests

class Virustotal:

    def __init__(self, target_info, api_key, headers = {}) -> None:
        self.target_info = target_info
        self.api_key = api_key
        self.headers = headers

    def create_headers(self):
        self.headers["x-apikey"] = self.api_key
        return self.headers
    
    def process_virustotal_lookup(self):

        URL = f"https://www.virustotal.com/api/v3/domains/{self.target_info.get('target_domain')}/subdomains?limit=1000"
        
        def manipulate_response(url: str):
            try:
                virustotal_server_respose = requests.get(url, headers=self.headers)
                if virustotal_server_respose.status_code == 200: print("Website is up and running...")
                else: print(f"Error accessing website. Status code: {virustotal_server_respose.status_code}")
                with open("./data/vt_subdomains.json", "w") as file: 
                    print("Data successfully accessed and created\n")
                    return file.write(virustotal_server_respose.text)
            except Exception as e:
                print("Error requesting virustotal server\n")
                return

        def collect_subdomains_data():
            pass

        def create_excel_output():
            pass


        self.create_headers()
        manipulate_response(url = URL)
    
    def process_subdomains_reachability():
        pass

    def create_subdomains_screenshots():

        def create_screenshots_folder():
            pass
        
        
    

    def check(self):
        self.create_headers()
        print(self.target_info)
        print(self.api_key)
        print(self.headers)