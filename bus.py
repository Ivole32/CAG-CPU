class bus():
    def __init__(self, name="Bus", wires=4):
        self.name = name
        self.wires = wires
        self.value = "0" * self.wires
        print(f"\033[32mBus {self.name} created with {self.wires} wires\033[0m")

    def set(self, value):
        self.value = str(value)
        print(f"\033[32m{self.name} set to {self.value}\033[0m")

    def get(self):
        return "".join(self.value)
    
    def modify(self, index, value):
        self.value = list(self.value)
        if self.value[index] == str(value):
            print(f"\033[96m    {self.name} stayed at {self.value[index]}\033[0m")

        else:
            self.value[index] = str(value)
            self.value = "".join(self.value)
            print(f"\033[96m    {self.name} modified to {self.value}\033[0m")