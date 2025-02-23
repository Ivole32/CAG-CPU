from gates import *
from register import register
from bus import bus

bus_1 = bus(name="Bus_1", wires=4) # Bus 1

registers = [
    register("A_register", 4, False, False, bus=bus_1),  # A register
    register("B_register", 4, False, False, bus=bus_1),  # B register
    register("Carry_register", 1, False, False),         # Carry register
    register("Result_register", 4, False, False, bus=bus_1)  # Result register
]

def ALU(register_1, register_2, register_3, register_4):
    s = 0
    c = 0

    for i in range(4):
        print(f"\n\033[32mIteration {i+1}:\033[0m")

        registers[0].enable_wire = True
        for register in range(len(registers)):
            a = int(registers[register].get()[3-i])
        registers[0].enable_wire = False

        registers[1].enable_wire = True
        for register in registers:
            b = int(register.get()[3-i])
        registers[1].enable_wire = False

        print(f"\033[36m    a: {a} b: {b}\033[0m")

        s = XOR(XOR(a, b), c)
        c = OR(AND(a, b) , AND(c, XOR(a, b))) 

        registers[3].modify(3-i, s)
        registers[2].modify(0, c)
    
    return register_3.get(), register_4.get()

if __name__ == "__main__":
    error_counter = 0
    test_counter = 0
    for i in range(16):
        for j in range(16):
            registers[0].set(f"{i:04b}")
            registers[1].set(f"{j:04b}")
            registers[2].set("0")
            registers[3].set("0000")

            result = f"{i+j:04b}"

            c, r = ALU(registers[0], registers[1], registers[2], registers[3])

            print(f"\n\033[32mRight result: {result}\033[0m")
            if len(result) > registers[0].bits or len(result) > register[1].bits and c == "1":
                color_code_1 = "\033[32m"
                color_code_2 = "\033[0m"
            elif result == r and c == "0":
                color_code_1 = "\033[32m"
                color_code_2 = "\033[0m"
            else:
                color_code_1 = "\033[31m"
                color_code_2 = "\033[0m"
                error_counter += 1

            test_counter += 1
            print(f"\n{color_code_1}Carry: {c} Result: {r}{color_code_2}\n\n")

    if error_counter == 0:
        print(f"\033[32mAll \033[36m{test_counter}\033[32m tests passed\033[0m")
    else:
        print(f"\033[31m{error_counter}/{test_counter} tests failed\033[0m")