import os

class Output:
    
    def __init__(self) -> None:
        self.message = "hello output"

    def test(self):
        return "".join([i if i != "\\" else "/" for i in os.getcwd()]) + f"/out/xd"
    

if __name__ == "__main__":
    out = Output()
    print(out.test())