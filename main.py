import re

class Main:
    
    def __init__(self, taget_info = {}, ) -> None:
        self.taget_info = taget_info

    def menu(self):
        print("\n\n\t\t-h \t\t\t\t\tPrint help message")
        print("\t\t-ti \t\t\t\t\tCheck actual target information")
        print("\t\t-dt \t\t\t\t\tDefine target")
        print("\t\t-v \t\t\t\t\tCall virustotal script")
        print("\t\t-s \t\t\t\t\tCall shodan script")
        print("\t\t-w \t\t\t\t\tCall whois script")
        print("\t\t-d \t\t\t\t\tCall DNS script")
        print("\t\t-e \t\t\t\t\tExit\n")


    def main_menu(self):

        def chcek_target_info() -> bool:
            return True if self.taget_info == {} else False

        def check_correct_input() -> bool:
            return True if USER_CHOICE == "-h" or USER_CHOICE == "-ti" or USER_CHOICE == "-dt" or USER_CHOICE == "-v" or USER_CHOICE == "-s" or USER_CHOICE == "-d" or USER_CHOICE == "-e" or USER_CHOICE == "-w" else False
        
        self.menu()
        while True:
            USER_CHOICE = input("$ ").lower()
            if check_correct_input() == False:
                print("Not available option, check the help by using -h\n")
                continue
            if USER_CHOICE == "-h": 
                self.menu()
                continue
            if USER_CHOICE == "-ti" and chcek_target_info():
                print("Target info not defined please define the target\n")
                continue
            elif USER_CHOICE == "-ti" and chcek_target_info() == False: self.chceck_target()
            if USER_CHOICE == "-dt" and chcek_target_info():
                self.define_target_info()
                continue
            if USER_CHOICE == "-dt" and chcek_target_info() == False:
                redefine = input("Target info already defined do you want to redefine it ['-y', '-n'] ? \n$ ").lower()
                if redefine == "-y": self.define_target_info()
                else: continue
            if chcek_target_info() == False:
                if USER_CHOICE == "-v":
                    print("Calling virustotal script\n")
                    break  
                elif USER_CHOICE == "-s":
                    print("Calling shodan script\n")
                    break  
                elif USER_CHOICE == "-w":
                    print("Calling whois script\n")
                    break   
                elif USER_CHOICE == "-d":
                    print("Calling dns script\n")
                    break  
            else:
                print("Target info not defined can't call the script\n")
                continue


    def chceck_target(self):
        for i in self.taget_info:
            print(f"{i}\t -> {self.taget_info.get(i)}")
        return

    def define_target_info(self):

        def correct_formalization(USER_INPUT) -> str:
            return USER_INPUT.replace(" ", "").lower()

        def get_target_name() -> bool:
            try:
                USER_INPUT = input("Define target name: ")
                self.taget_info["target_name"] = correct_formalization(USER_INPUT = USER_INPUT) 
                print("Target name succesfully set\n")
                return True
            except Exception as e:
                print("Something went wrong creating target name\n")
                return False
            
        def get_target_domain() -> bool:
            
            def is_tld_present(USER_INPUT: str) -> bool:
                tld_regex = re.compile(r'\.[a-z]{2,}$')
                return bool(tld_regex.search(USER_INPUT))
            
            while True:
                USER_INPUT = input("Define target domain: ")
                USER_INPUT = correct_formalization(USER_INPUT=USER_INPUT)
                if is_tld_present(USER_INPUT=USER_INPUT):
                    self.taget_info["target_domain"] = USER_INPUT 
                    print("Target domain succesfully set\n")
                    return True
                else: print("Something went wrong creating target domain, please check if tld 'top level domain' is correct or present\n")

        # main function
        while True:
            if get_target_name() and get_target_domain(): 
                print("Target info successfully set\n") 
                return self.taget_info


if __name__ == "__main__":
    main = Main()
    main.main_menu()