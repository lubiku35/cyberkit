
class Menu:

    def __init__(self, commands_list = {}) -> None:
        self.commands_list = {
            "-help": "Print help",
            "-ti": "Set target info",
            "-exit": "Exit this script"
        }

    def project_menu(self):
        for i in range(2): print("")
        for i, j in self.commands_list.items(): print("\t" + i + "\t\t\t" + j)
    
    def main_menu():
        pass


