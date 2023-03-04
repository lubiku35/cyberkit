import os, requests, json
from dotenv import load_dotenv

class Virustotal:

    def __init__(self, target_info = {}, subdomains_count = 0, subdomains_data_list = [], ips_for_subdomains = {}, menu = {}, headers = {}) -> None:
        self.target_info = target_info
        self.subdomains_count = subdomains_count
        self.subdomains_data_list = subdomains_data_list
        self.ips_for_subdomains = ips_for_subdomains
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
        
        def get_subdomains_count():
            with open("./data/vt_subdomains.json", "r") as file: 
                data = json.load(file)
                self.subdomains_count = data["meta"]["count"]
            return self.subdomains_count

        def parse_json_subdomains():
            with open("./data/vt_subdomains.json", "r") as file: data = json.load(file)
            counter = 0
            for i in data["data"]:
                domain_id = data["data"][counter]["id"]
                self.subdomains_data_list.append(domain_id)
                counter += 1
            return self.subdomains_data_list
        
        def parse_json_subdomains_ips():
            with open("./data/vt_subdomains.json", "r") as file: data = json.load(file)
            counter = 0
            for i in data["data"]:
                subdomain_data, domain_ip_dns_record = [], data["data"][counter]["attributes"]["last_dns_records"]
                for j in domain_ip_dns_record:
                    if "A" in j.values(): subdomain_data.append(j["value"])                                          # "A" -> IP
                self.ips_for_subdomains[self.subdomains_data_list[counter]] = subdomain_data
                counter += 1
            return self.ips_for_subdomains

        def check_reachability(subdomains):
            pass
        
        manipulate_response(url=url)
        get_subdomains_count()
        parse_json_subdomains()
        parse_json_subdomains_ips()
        check_reachability(subdomains=self.subdomains_data_list)
    

    def get_menu():
        pass
    
    def test(self):
        print(self.subdomains_data_list)
        print(self.ips_for_subdomains)

