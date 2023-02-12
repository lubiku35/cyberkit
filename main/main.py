import requests, json, os
from bs4 import BeautifulSoup
from selenium import webdriver

class Liberty:

    def __init__(self, target_domain = "", headers = {}, driver = "") -> None:
        self.target_domain = target_domain                                                          # USER INPUT
        self.headers = {
            "accept": "application/json",                                                           # APP -> JSON
            "x-apikey": "81dab74fef4524e13c1c17bfe5d33b7a63005282840bf4dbcc080d8ff164290f"          # API KEY -> VIRUS TOTAL
        }
        self.driver = ""                                                                            # INITIALIZE DEFAULT WEBDRIVER
        self.virustotal_subdomains = []
        self.cwd = os.getcwd()                                                                      # CURRENT WORKING DIRECTORY
    
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

            self.virustotal_subdomains = []
            counter = 0

            for i in data["data"]:
                subdomain_data = []
                domain_id = data["data"][counter]["id"]                                             # Domain Name
                last_dns_record_ip = data["data"][counter]["attributes"]["last_dns_records"]        # subdomain IP

                # Finding Ips 
                for j in last_dns_record_ip:
                    if "A" in j.values():
                        subdomain_data.append(j["value"])

                subdomain_data.append(domain_id)
                self.virustotal_subdomains.append(subdomain_data)

                counter += 1

            return self.virustotal_subdomains

        url = f"https://www.virustotal.com/api/v3/domains/{self.target_domain}/subdomains?limit=1000"

        # Virustotal response
        response = requests.get(url, headers=self.headers)

        with open("../data_collect/subdomains.json", "w") as file:
            file.write(response.text)

        return virustotal_subdomains_parser()

    def whois_lookup(self):
        response = requests.get(f"https://who.is/whois/{self.target_domain}")

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            pre_tag = soup.pre
            pre_tag = pre_tag.get_text
            x = pre_tag.__str__().split('\n')
            out = ""

            # deleting bad formats
            for i in x:
                if i.startswith("<") or i.startswith("%"):
                    continue
                else:
                    out += i + "\n"
            return out
        else:
            return "Error: WHOIS lookup failed."

    def create_output(self):
        output_domain = self.target_domain[:self.target_domain.index(".")]

        def get_correct_path(output_domain):
            directory = f"outputs//{output_domain}"
            correct_path = ""
            for i in self.cwd:
                if i == '\\':
                    i = "/"
                    correct_path += i
                correct_path += i
            return correct_path + "//" + directory

        def create_target_directory():
            return os.mkdir(get_correct_path(output_domain=output_domain))

        
        create_target_directory()
        self.cwd = get_correct_path(output_domain=output_domain)

        with open(f"{self.cwd}//{output_domain}.txt", "w") as file:
            file.write(f"Data Collected for domain {self.target_domain}\n\n")
            file.write("Who Is LookUp: \n")
            file.write(self.whois_lookup())
            file.write("\nVirustotal Subdomains Found: \n\n")
            for i in self.virustotal_subdomains:
                for j in i:
                    file.write(j + "   ")
                file.write("\n")

    def is_reachable_subdomain(self):

        def add_reachability(x):
            counter = 0
            for i in x:
                self.virustotal_subdomains[counter].append(i)
                counter += 1
            return

        def find_alphanumerics(x):
            alphanumerics = []
            for i in x:
                for j in i:
                    if j[0].isalpha() or j[1].isalpha() or j[2].isalpha():
                        alphanumerics.append(j)
            return alphanumerics
        
        alphanumerics = find_alphanumerics(self.virustotal_subdomains) 
        self.driver = webdriver.Firefox()
        results = []
        for i in alphanumerics:
            url = f"https://{i}"
            try:
                self.driver.set_page_load_timeout(12)
                self.driver.get(url)
                results.append("True")
            except:
                results.append("False")
        self.driver.close()

        add_reachability(results)

        return self.virustotal_subdomains

    def print_subdomains(self):
        for i in self.virustotal_subdomains:
            print(i)
        return

# # Load the URL
# url = "https://www.jhv.cz"
# driver.get(url)

if __name__ == "__main__":
    liberty = Liberty()
    liberty.display_visual_menu()
    liberty.get_target_domain()
    print(liberty.get_virustotal_subdomains())
    # print(liberty.whois_lookup())
    # liberty.create_txt_output()
    liberty.is_reachable_subdomain()
    liberty.print_subdomains()
    liberty.create_output()





