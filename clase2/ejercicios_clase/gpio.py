class Gpio:
    """docstring for Gpio."""
    def __init__(self, num=0, state=False):
        self.set_num(num)
        self.set_state(state)
        
    def set_num(self, num):
        if num >= 0 and num < 16:
            self.num = num
            
    def set_state(self, state):
        self.state = state
        with open(f"tmp/gpio_{self.num}.data","w",encoding="utf-8") as f:
            if state:
                f.write("1\n")
            else:
                f.write("0\n")
            
    def print_gpio(self):
        print(f"gpio{self.num} -> state={self.state}")
        
    def get_num(self):
        return self.num
    
    def get_state(self):
        with open(f"tmp/gpio_{self.get_num()}.data","r",encoding="utf-8") as f:
            s = f.readline()
            if s[0] == "0":
                return False
            elif s[0] == "1":
                return True
    