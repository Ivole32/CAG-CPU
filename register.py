class register():
    def __init__(self, name, bits, set_wire, enable_wire):
        self.name = name
        self.bits = bits
        self.set_wire = set_wire
        self.enable_wire = enable_wire
        self.value = "0" * self.bits
        print(f"\033[32mRegister {self.name} created with {self.bits} bits\033[0m")

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