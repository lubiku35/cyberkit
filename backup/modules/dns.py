

class DNS:

    def __init__(self, target_info) -> None:
        self.target_info = target_info

    def check(self):
        print(self.target_info)