import requests, json, xlsxwriter
import pandas as pd

class Virustotal:

    def __init__(self, target_info, api_key, headers = {}, SUBDOMAINS_DATA = {}, SUBDOMAINS_COUNT = 0) -> None:
        self.target_info = target_info
        self.api_key = api_key
        self.headers = headers

        self.SUBDOMAINS_DATA = SUBDOMAINS_DATA
        self.SUBDOMAINS_COUNT = SUBDOMAINS_COUNT

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
        self.create_headers()
        manipulate_response(url=URL)
        self.collect_subdomains_data()
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
            return 
        
        with open("./data/vt_subdomains.json", "r") as file: DATA = json.load(file)
        self.SUBDOMAINS_COUNT = DATA.get("meta").get("count")

        for i in DATA.get("data"):
            SUBDOMAIN_NAME = i.get("id")        
            LAST_DNS_RECORDS_DATA = i.get("attributes").get("last_dns_records")
            SUBDOMAIN_IPS = []
            for i in LAST_DNS_RECORDS_DATA:
                if i["type"] == "A": SUBDOMAIN_IPS.append(i.get("value"))
                self.SUBDOMAINS_DATA[SUBDOMAIN_NAME] = SUBDOMAIN_IPS
        
        create_subdomains_count_as_txt(DATA=self.SUBDOMAINS_COUNT)
        create_subdomains_excel_output(DATA=self.SUBDOMAINS_DATA)
        return 
    
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