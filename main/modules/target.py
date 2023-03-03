import re

# Structure of target_info:

#   "target_name" = "name of the target" 
#   "target_domain" = "domain of the target" 

class Target:
    
    def __init__(self, target_info = {}) -> None:
        self.target_info = target_info 

    def define_target_info(self):

        def correct_formalization(user_target_input: str) -> str:
            return user_target_input.replace(" ", "").lower()

        def get_info():
            print("The name of the target have to be provided")
            print("You can choose to add domain or ip, but at least one have to be provided for making a research")

        def define_target_name():
            user_target_input_name = input("$ ")
            self.target_info["target_name"] = correct_formalization(user_target_input=user_target_input_name)
            print("'target_name' successfully set")
            return True

        def define_target_domain():
            
            def is_tld_present(user_target_input: str) -> bool:
                tld_regex = re.compile(r'\.[a-z]{2,}$')
                return bool(tld_regex.search(user_target_input))
            
            while True:
                user_target_input_domain = input("$ ")
            
                if is_tld_present(user_target_input=user_target_input_domain):
                    self.target_info["target_domain"] = correct_formalization(user_target_input=user_target_input_domain)
                    print("'target_domain' successfully set")
                    return True
                else: print("Something went wrong creating 'target_domain' info, please provide correct domain with correct tld [top level domain]")

        get_info()

        while True:
            print("Define the target name")
            if define_target_name():
                print("Define the target domain")
                while define_target_domain() != True:
                    define_target_domain()      
                    return
            return

    def return_target_info(self):
        return self.target_info