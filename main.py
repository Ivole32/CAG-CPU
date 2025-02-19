from gates import *
from register import register

register_1 = register("A_register", 4, True, True) # A register
register_2 = register("B_register", 4, True, True) # B register

register_3 = register("Carry_register", 1, True, True) # Carry register

register_4 = register("Result_register", 4, True, True) # Result register


def ALU(register_1, register_2, register_3, register_4):
    register_1.set("0110")
    register_2.set("0111")
    register_3.set("0")
    register_4.set("0000")
    s = 0
    c = 0

    for  i in range(4):
        print(f"\n\033[32mIteration {i+1}:\033[0m")
        a = int(register_1.get()[3-i])
        b = int(register_2.get()[3-i])

        print(f"\033[36m    a: {a} b: {b}\033[0m")

        s = XOR(XOR(a, b), c)
        c = OR(AND(a, b) , AND(c, XOR(a, b))) 

        register_4.modify(3-i, s)
        register_3.modify(0, c)
    
    return register_3.get(), register_4.get()


if __name__ == "__main__":
    c ,r = ALU(register_1, register_2, register_3, register_4)

    print(f"\n\033[32mCarry: {c} Result: {r}\033[0m")