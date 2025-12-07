"""Solution module for Day 17, 2024"""
import copy
from itertools import count
import time
from sys import maxsize

from advent_of_code.utils.fetch import fetch


def test_1A():
    input = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""
    answer = "4,6,3,5,6,3,5,2,1,0"
    assert(solution_1(input) == answer)
    

def test_1B():
    registers = {"A": 0, "B": 0, "C": 9}
    program = [2, 6]
    _, registers = run_program(registers, program)
    assert(registers["B"]==1)


def test_1C():
    registers = {"A": 10, "B": 0, "C": 0}
    program = [5,0,5,1,5,4]
    output, _ = run_program(registers, program)
    assert(output=="0,1,2")


def test_1D():
    registers = {"A": 2024, "B": 0, "C": 0}
    program = [0,1,5,4,3,0]
    output, registers = run_program(registers, program)
    assert(output=="4,2,5,6,7,7,7,7,3,1,0" and registers["A"]==0)


def test_1E():
    registers = {"A": 0, "B": 29, "C": 0}
    program = [1,7]
    output, registers = run_program(registers, program)
    assert(registers["B"]==26)


def test_1F():
    registers = {"A": 0, "B": 2024, "C": 43690}
    program = [4,0]
    output, registers = run_program(registers, program)
    assert(registers["B"]==44354)


def test_2():
    input = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""
    answer = 117440
    assert(solution_2(input) == answer)


def parse(input):
    regs, prog = input.strip().split("\n\n")

    registers = {}
    for reg in regs.split("\n"):
        letter = reg.strip().split()[1][0]
        number = int(reg.strip().split()[-1])
        registers[letter] = number
    
    prog = prog.split()[-1]
    program = list(map(int, prog.split(",")))

    return registers, program


def adv(operand, registers):
    num = registers["A"]

    if operand in range(4):
        den = operand
    elif operand == 4:
        den = registers["A"]
    elif operand == 5:
        den = registers["B"]
    elif operand == 6:
        den = registers["C"]
    else:
        raise ValueError(f"Invalid operand: {operand}")
    
    registers["A"] = int(num/(2**den))

    return registers


def bxl(operand, registers):
    registers["B"] = registers["B"] ^ operand
    return registers


def bst(operand, registers):

    if operand in range(4):
        val = operand
    elif operand == 4:
        val = registers["A"]
    elif operand == 5:
        val = registers["B"]
    elif operand == 6:
        val = registers["C"]
    else:
        raise ValueError(f"Invalid operand: {operand}")

    registers["B"] = val%8

    return registers


def bxc(operand, registers):
    registers["B"] = registers["B"] ^ registers["C"]
    return registers


def out(operand, registers):

    if operand in range(4):
        val = operand
    elif operand == 4:
        val = registers["A"]
    elif operand == 5:
        val = registers["B"]
    elif operand == 6:
        val = registers["C"]
    else:
        raise ValueError(f"Invalid operand: {operand}")

    return val%8


def bdv(operand, registers):
    num = registers["A"]

    if operand in range(4):
        den = operand
    elif operand == 4:
        den = registers["A"]
    elif operand == 5:
        den = registers["B"]
    elif operand == 6:
        den = registers["C"]
    else:
        raise ValueError(f"Invalid operand: {operand}")
    
    registers["B"] = int(num/(2**den))

    return registers


def cdv(operand, registers):
    num = registers["A"]

    if operand in range(4):
        den = operand
    elif operand == 4:
        den = registers["A"]
    elif operand == 5:
        den = registers["B"]
    elif operand == 6:
        den = registers["C"]
    else:
        raise ValueError(f"Invalid operand: {operand}")
    
    registers["C"] = int(num/(2**den))

    return registers


def run_program(registers, program):

    output = []
    ip = 0
    while True:

        try:
            opcode, operand = program[ip], program[ip+1]
        except IndexError:
            return ",".join(output), registers

        match opcode:
            case 0:
                registers = adv(operand, registers)
            case 1:
                registers = bxl(operand, registers)
            case 2:
                registers = bst(operand, registers)
            case 3:
                if registers["A"] != 0:
                    ip = operand - 2  # -2 to take height for the increment further down
            case 4:
                registers = bxc(operand, registers)
            case 5:
                output.append(str(out(operand, registers)))
            case 6:
                registers = bdv(operand, registers)
            case 7:
                registers = cdv(operand, registers)

        ip += 2


def solution_1(in_data):
    registers, program = parse(in_data)
    output, registers = run_program(registers, program)
    return output


def solution_2(input):
    _, program = parse(input)

    queue = [(program, len(program) - 1, 0)]
    while queue:

        program, off, a = queue.pop(0)

        # Treat A like a number in base 8 (octal).
        # Shifting a left by 3 bits (a << 3) is equivalent to multiplying a by
        # 8, and then adding cur (which is between 0 and 7) appends a new
        # "digit" in base 8.
        for cur in range(8):
            new_a = (a << 3) + cur
            registers = {"A": new_a, "B": 0, "C": 0}

            output, _ = run_program(registers, program)

            # Check if the last off+1 digits of the output matches.
            # If they do, increment the size of the suffix and add
            # the new_a that yielded the good output to the queue.
            # When off == 0 the whole program matches.
            if list(map(int, output.split(","))) == program[off:]:
                if off == 0:
                    return new_a
                queue.append((program, off - 1, new_a))


def run(year: int, day: int):
    print(f"\n🌟 Fetching input for {year}/{day} 🌟")

    input = fetch(year, day)

    test_1A()
    print("Test 1A was successful!")
    test_1B()
    print("Test 1B was successful!")
    test_1C()
    print("Test 1C was successful!")
    test_1D()
    print("Test 1D was successful!")
    test_1E()
    print("Test 1E was successful!")
    test_1F()
    print("Test 1F was successful!")

    test_2()
    print("Test 2 was successful!")

    tic = time.perf_counter()
    s1 = solution_1(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 1: {s1} acquired in: {toc-tic:0.4f} seconds")

    tic = time.perf_counter()
    s2 = solution_2(copy.deepcopy(input))
    toc = time.perf_counter()
    print(f"Solution for problem 2: {s2} acquired in: {toc-tic:0.4f} seconds")
