import requests, json
import pandas as pd

class Virustotal:

    def __init__(self, target_info, api_key, headers = {}, SUBDOMAINS_DATA = {}, SUBDOMAINS_COUNT = 0, HTTP_SUBDOMAINS_REACHABILITY = [], HTTPS_SUBDOMAINS_REACHABILITY = []) -> None:
        # Neccessary data to start this script 
        self.target_info = target_info
        self.api_key = api_key
        self.headers = headers

        # Master Subdomains Data
        self.SUBDOMAINS_DATA = SUBDOMAINS_DATA
        self.SUBDOMAINS_COUNT = SUBDOMAINS_COUNT

        # Reachability data 
        self.HTTP_SUBDOMAINS_REACHABILITY = HTTP_SUBDOMAINS_REACHABILITY
        self.HTTPS_SUBDOMAINS_REACHABILITY = HTTPS_SUBDOMAINS_REACHABILITY


    def create_headers(self):
        # headers for virustotal api 
        self.headers["x-apikey"] = self.api_key
        return self.headers
    
    def process_virustotal_lookup(self):

        URL = f"https://www.virustotal.com/api/v3/domains/{self.target_info.get('target_domain')}/subdomains?limit=1000"
        def manipulate_response(url: str):
            try:
                virustotal_server_respose = requests.get(url, headers=self.headers)
                if virustotal_server_respose.status_code == 200: print("Website is up and running")
                else: print(f"Error accessing website. Status code: {virustotal_server_respose.status_code}")
                with open("./data/vt_subdomains.json", "w") as file: print("Data successfully accessed and created in vt_subdomains.json file"); return file.write(virustotal_server_respose.text)
            except Exception as e: print("Error requesting virustotal server\n"); return
        self.create_headers()
        manipulate_response(url=URL)
        self.collect_subdomains_data()
        print("Data from Virustotal about subdomains collected successfully!")
        return
    
    def collect_subdomains_data(self):

        def create_subdomains_count_as_txt(DATA):
            with open(f'./out/{self.target_info.get("target_name")}/subdomains_count.txt', "w") as file: return file.write("Subdomains count: " + str(DATA))
        
        def create_subdomains_excel_output(DATA):
            data = []
            for subdomain, ips in DATA.items(): data.append({'SUBDOMAIN NAME': subdomain, 'SUBDOMAIN IPS': ', '.join(ips)})
            df = pd.DataFrame(data=data)

            # Write the dataframe to an Excel file
            writer = pd.ExcelWriter(f'./out/{self.target_info.get("target_name")}/subdomains.xlsx', engine='xlsxwriter')
            df.to_excel(writer, index=False)
            writer.close()
            print("Virustotal data proccessed successfully!")
            return 
        
        with open("./data/vt_subdomains.json", "r") as file: DATA = json.load(file)
        self.SUBDOMAINS_COUNT = DATA.get("meta").get("count")

        for i in DATA.get("data"):
            SUBDOMAIN_NAME = i.get("id")        
            LAST_DNS_RECORDS_DATA = i.get("attributes").get("last_dns_records")
            SUBDOMAIN_IPS = []
            for i in LAST_DNS_RECORDS_DATA: 
                if i["type"] == "A": SUBDOMAIN_IPS.append(i.get("value")); self.SUBDOMAINS_DATA[SUBDOMAIN_NAME] = SUBDOMAIN_IPS
        
        create_subdomains_count_as_txt(DATA=self.SUBDOMAINS_COUNT)
        create_subdomains_excel_output(DATA=self.SUBDOMAINS_DATA)
        return 
        
    def process_subdomains_reachability(self):
        
        def check_https_subdomains_reachability(SUBDOMAINS):
            
            def create_https_reachability_txt_output(data):
                with open(f"./out/{self.target_info.get('target_name')}/virustotal_https_reachability.txt", "w") as file:
                    file.write("HTTPS SUBDOMAINS REACHABILITY\n\n")
                    data.insert(0, ("Subomain", "Is reachable", "Status\n"))
                    for i in data:
                        for j in i:
                            j = str(j)
                            while len(j) <= 32: j += " "
                            file.write(str(j))
                        file.write("\n")

            self.HTTPS_SUBDOMAINS_REACHABILITY = []
            for subdomain in SUBDOMAINS.keys():
                try:
                    RESPONSE = requests.get(url=f"https://{subdomain}", timeout=10, allow_redirects=False)
                    if RESPONSE.status_code == 200: self.HTTPS_SUBDOMAINS_REACHABILITY.append((subdomain, True, "200"))
                    elif RESPONSE.status_code == 301 or RESPONSE.status_code == 302: self.HTTPS_SUBDOMAINS_REACHABILITY.append((subdomain, "Redirect", "301/302"))
                except requests.exceptions.RequestException as e: self.HTTPS_SUBDOMAINS_REACHABILITY.append((subdomain, False, "500")) if "[Errno 11001]" or "getaddrinfo failed" in str(e) else self.HTTPS_SUBDOMAINS_REACHABILITY.append((subdomain, False, "Check by User"))
                
            return create_https_reachability_txt_output(data=self.HTTPS_SUBDOMAINS_REACHABILITY)

        def check_http_subdomains_reachability(SUBDOMAINS):

            def create_http_reachability_txt_output(data):
                with open(f"./out/{self.target_info.get('target_name')}/virustotal_http_reachability.txt", "w") as file:
                    file.write("HTTP SUBDOMAINS REACHABILITY\n\n")
                    data.insert(0, ("Subomain", "Is reachable", "Status\n"))
                    for i in data:
                        for j in i:
                            j = str(j)
                            while len(j) <= 32: j += " "
                            file.write(str(j))
                        file.write("\n")

            self.HTTP_SUBDOMAINS_REACHABILITY = []
            for subdomain in SUBDOMAINS.keys():
                try:
                    RESPONSE = requests.get(url=f"http://{subdomain}", timeout=10, allow_redirects=False)
                    if RESPONSE.status_code == 200: self.HTTP_SUBDOMAINS_REACHABILITY.append((subdomain, True, "200"))
                    elif RESPONSE.status_code == 301 or RESPONSE.status_code == 302: self.HTTP_SUBDOMAINS_REACHABILITY.append((subdomain, "Redirect", "301/302"))
                except requests.exceptions.RequestException as e: self.HTTP_SUBDOMAINS_REACHABILITY.append((subdomain, False, "500")) if "[Errno 11001]" or "getaddrinfo failed" in str(e) else self.HTTP_SUBDOMAINS_REACHABILITY.append((subdomain, False, "Check by User"))
            
            return create_http_reachability_txt_output(data=self.HTTP_SUBDOMAINS_REACHABILITY) 
        
        check_https_subdomains_reachability(SUBDOMAINS=self.SUBDOMAINS_DATA)
        check_http_subdomains_reachability(SUBDOMAINS=self.SUBDOMAINS_DATA)
    
    def return_subdomains_data(self):
        return self.SUBDOMAINS_DATA

    def return_reachability_data(self):
        return self.HTTP_SUBDOMAINS_REACHABILITY, self.HTTPS_SUBDOMAINS_REACHABILITY
        
    def check(self):
        self.create_headers()
        print(self.target_info)
        print(self.api_key)
        print(self.headers)