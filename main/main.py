import requests, json


class Liberty:

    def __init__(self, target_domain = "", headers = {}):
        self.target_domain = target_domain                                                          # USER INPUT
        self.headers = {
            "accept": "application/json",                                                           # APP -> JSON 
            "x-apikey": "81dab74fef4524e13c1c17bfe5d33b7a63005282840bf4dbcc080d8ff164290f"          # API KEY -> VIRUS TOTAL
        }

    # VISUAL MENU
    def display_visual_menu(self):
        print("")
        print("")
        print("     _/\/\________/\/\/\/\__/\/\/\/\/\____/\/\/\/\/\/\__/\/\/\/\/\____/\/\/\/\/\/\__/\/\____/\/\_")
        print("    _/\/\__________/\/\____/\/\____/\/\__/\____________/\/\____/\/\______/\/\______/\/\____/\/\_ ")
        print("   _/\/\__________/\/\____/\/\/\/\/\____/\/\/\/\/\____/\/\/\/\/\________/\/\________/\/\/\/\___  ")
        print("  _/\/\__________/\/\____/\/\____/\/\__/\/\__________/\/\__/\/\________/\/\__________/\/\_____   ")
        print(" _/\/\/\/\/\__/\/\/\/\__/\/\/\/\/\____/\/\/\/\/\/\__/\/\____/\/\______/\/\__________/\/\_____    ")
        print("____________________________________________________________________________________________     ")
        print("by: Lubiku")
    
    # USER MENU
    def display_menu(self):
        pass

    # TARGET INPUT
    def get_target_domain(self):
        self.target_domain = input("enter domain in format [xxxxxxx.xxx]: ")
        return self.target_domain

    # SUBDOMAINS FROM VIRUSTOTAL
    def get_virustotal_subdomains(self):

        def virustotal_subdomains_parser():
            with open("../data_collect/subdomains.json", "r") as file:
                data = json.load(file)

            subdomains = []
            counter = 0

            for i in data["data"]:
                subdomain_data = []
                domain_id = data["data"][counter]["id"]                                             # Domain Name
                last_dns_record_ip = data["data"][counter]["attributes"]["last_dns_records"]        # subdomain IP
                
                for j in last_dns_record_ip:
                    if "A" in j.values():
                        subdomain_data.append(j["value"])

                subdomain_data.append(domain_id)
                subdomains.append(subdomain_data)

                counter += 1
            
            return subdomains

        url = f"https://www.virustotal.com/api/v3/domains/{self.target_domain}/subdomains?limit=1000"
        
        response = requests.get(url, headers=self.headers)
        
        with open("../data_collect/subdomains.json", "w") as file:
            file.write(response.text)

        return virustotal_subdomains_parser()
    

    
if __name__ == "__main__":
    liberty = Liberty()
    liberty.display_visual_menu()
    liberty.get_target_domain()
    print(liberty.get_virustotal_subdomains())






