from modules import dns, shodan, virustotal, whois

import re, os
from dotenv import load_dotenv

class Main:
    
    def __init__(self, target_info = {}, API_keys = {}, SUBDOMAINS_DATA= {}) -> None:
        self.target_info = target_info                # "target_name", "target_domain"
        self.API_keys = API_keys                      # "VIRUSTOTAL_API_KEY", "SHODAN_API_KEY"

        self.SUBDOMAINS_DATA = SUBDOMAINS_DATA
    def menu(self):
        print("\n\n\t\t-h \t\t\t\t\tPrint help message")
        print("\t\t-ti \t\t\t\t\tCheck actual target information")
        print("\t\t-dt \t\t\t\t\tDefine target")
        print("\t\t-all \t\t\t\t\tCall all scripts")
        print("\t\t-v \t\t\t\t\tCall virustotal script")
        print("\t\t-s \t\t\t\t\tCall shodan script")
        print("\t\t-w \t\t\t\t\tCall whois script")
        print("\t\t-d \t\t\t\t\tCall DNS script")
        print("\t\t-e \t\t\t\t\tExit\n")

    def main_menu(self):

        def chcek_target_info() -> bool:
            return True if self.target_info == {} else False

        def check_correct_input() -> bool:
            return True if USER_CHOICE == "-h" or USER_CHOICE == "-ti" or USER_CHOICE == "-dt" or USER_CHOICE == "-v" or USER_CHOICE == "-s" or USER_CHOICE == "-d" or USER_CHOICE == "-e" or USER_CHOICE == "-w" or USER_CHOICE == "-all" else False
        
        self.menu()
        while True:
            USER_CHOICE = input("$ ").lower()
            if check_correct_input() == False: print("Not available option, check the help by using -h\n"); continue
            if USER_CHOICE == "-h": self.menu(); continue
            if USER_CHOICE == "-ti" and chcek_target_info(): print("Target info not defined please define the target\n"); continue
            elif USER_CHOICE == "-ti" and chcek_target_info() == False: self.chceck_target()
            if USER_CHOICE == "-dt" and chcek_target_info(): self.define_target_info(); continue
            if USER_CHOICE == "-dt" and chcek_target_info() == False:
                redefine = input("Target info already defined do you want to redefine it ['-y', '-n'] ? \n$ ").lower()
                if redefine == "-y": self.define_target_info()
                else: continue
            if chcek_target_info() == False:
                if USER_CHOICE == "-all":
                    print("OSINT Analyzation in progress")
                    self.generate_output_folder()
                    self.load_env_file()
                    CALLBACK_VIRUSTOTAL, CALLBACK_WHOIS = virustotal.Virustotal(self.target_info, self.API_keys.get("VIRUSTOTAL_API_KEY")), whois.Whois(self.target_info)                                        
                    CALLBACK_WHOIS.process_whois_lookup()
                    CALLBACK_VIRUSTOTAL.process_virustotal_lookup()
                    CALLBACK_VIRUSTOTAL.process_subdomains_reachability()
                    self.SUBDOMAINS_DATA = CALLBACK_VIRUSTOTAL.return_subdomains_data()
                    CALLBACK_SHODAN = shodan.ShodanLookup(self.target_info, api_key=self.API_keys.get("SHODAN_API_KEY"), SUBDOMAINS_DATA=self.SUBDOMAINS_DATA)
                    x = CALLBACK_SHODAN.collect_shodan_data()
                    print(x)
                    break
                if USER_CHOICE == "-v":
                    print("Calling virustotal script\n")
                    self.generate_output_folder()
                    self.load_env_file()
                    CALLBACK_VIRUSTOTAL = virustotal.Virustotal(self.target_info, self.API_keys.get("VIRUSTOTAL_API_KEY"))
                    CALLBACK_VIRUSTOTAL.process_virustotal_lookup()
                    CALLBACK_VIRUSTOTAL.process_subdomains_reachability()
                    self.SUBDOMAINS_DATA = CALLBACK_VIRUSTOTAL.return_subdomains_data()
                    break  
                elif USER_CHOICE == "-s":
                    print("Calling shodan script\n")
                    self.generate_output_folder()
                    self.load_env_file()
                    CALLBACK_SHODAN = shodan.Shodan(self.target_info, self.API_keys.get("SHODAN_API_KEY"), self.SUBDOMAINS_DATA)
                    CALLBACK_SHODAN.check()
                    break  
                elif USER_CHOICE == "-w":
                    print("Calling whois script\n")
                    self.generate_output_folder()
                    CALLBACK_WHOIS = whois.Whois(self.target_info)
                    CALLBACK_WHOIS.process_whois_lookup()
                    break   
                elif USER_CHOICE == "-d":
                    print("Calling dns script\n")
                    self.generate_output_folder()
                    CALLBACK_DNS = dns.DNS(self.target_info)
                    CALLBACK_DNS.check()
                    break  
            else: print("Target info not defined can't call the script\n"); continue

    def chceck_target(self):
        for i in self.target_info: print(f"{i}\t -> {self.target_info.get(i)}")
        return

    def define_target_info(self):

        def correct_formalization(USER_INPUT) -> str:
            return USER_INPUT.replace(" ", "").lower()

        def get_target_name() -> bool:
            try:
                USER_INPUT = input("Define target name: ")
                USER_INPUT.replace(" ", "_")
                self.target_info["target_name"] = correct_formalization(USER_INPUT = USER_INPUT) 
                print("Target name succesfully set\n")
                return True
            except Exception as e: print("Something went wrong creating target name\n"); return False
            
        def get_target_domain() -> bool:
            # function to check top level domain 
            def is_tld_present(USER_INPUT: str) -> bool:
                tld_regex = re.compile(r'\.[a-z]{2,}$')
                return bool(tld_regex.search(USER_INPUT))
            
            while True:
                USER_INPUT = input("Define target domain: ")
                USER_INPUT = correct_formalization(USER_INPUT=USER_INPUT)
                if is_tld_present(USER_INPUT=USER_INPUT):
                    self.target_info["target_domain"] = USER_INPUT 
                    print("Target domain succesfully set\n")
                    return True
                else: print("Something went wrong creating target domain, please check if tld 'top level domain' is correct or present\n")

        # main target info function
        while True:
            if get_target_name() and get_target_domain(): print("Target info successfully set\n"); return self.target_info

    def generate_output_folder(self):
        
        def get_correct_path() -> str:
            return "".join([i if i != "\\" else "/" for i in os.getcwd()]) + f"/out/{self.target_info.get('target_name')}"
        
        try:
            os.mkdir(get_correct_path())
            print(f"Successfully created output folder {self.target_info.get('target_name')}")
            return 
        except: print(f"Something went wrong creating a folder, maybe {self.target_info.get('target_name')} folder already exists"); return 
    
    # create .env file where main function is and pass the values in this format: 
    # VIRUSTOTAL_API_KEY = yourVirustotalApiKey
    # SHODAN_API_KEY = yourShodanApiKey
    def load_env_file(self):
        load_dotenv()
        self.API_keys["VIRUSTOTAL_API_KEY"], self.API_keys["SHODAN_API_KEY"] = os.getenv("VIRUSTOTAL_API_KEY"), os.getenv("SHODAN_API_KEY")
        return self.API_keys

if __name__ == "__main__":
    main = Main()
    main.main_menu()