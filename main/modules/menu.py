
class Menu:

    def __init__(self, commands_list = {}) -> None:
        self.commands_list = {
            "-help": "Print help",
            "-ti": "Set target info",
            "-vt": "Force Virustotal scan",
            "-exit": "Exit this script"
        }

    def project_menu(self):
        print("Available Commands: \n")
        for i in range(2): print("")
        for i, j in self.commands_list.items(): print("\t\t" + i + "\t\t\t\t" + j)
        print("")
        
    def main_menu():
        pass


