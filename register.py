class register():
    def __init__(self, name, bits, set_wire, enable_wire, bus=None):
        self.name = name
        self.bus = bus
        self.bits = bits
        self.set_wire = set_wire
        self.enable_wire = enable_wire
        self.value = "0" * self.bits
        print(f"\033[32mRegister {self.name} created with {self.bits} bits\033[0m")

    def set(self, value="0000", set_wire=False):
        if set_wire:
            if self.bus:
                self.value = str(self.bus.get())
                print(f"\033[32m{self.name} set to {self.value} by {self.bus.name}\033[0m")
        else:
            self.value = str(value)
            print(f"\033[32m{self.name} set to {self.value} by value parameter\033[0m")

    def get(self, enable_wire=False):
        if enable_wire:
            self.bus.set(self.value)
    
    def modify(self, index, value, set_wire=False):
        if set_wire:
            self.value = list(self.value)
            if self.value[index] == str(value):
                print(f"\033[96m    {self.name} stayed at {self.value[index]}\033[0m")

            else:
                self.value[index] = str(value)
                self.value = "".join(self.value)
                print(f"\033[96m    {self.name} modified to {self.value}\033[0m")