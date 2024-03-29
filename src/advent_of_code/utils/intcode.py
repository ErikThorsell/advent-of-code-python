"""An OP Code Module"""
from collections import defaultdict

import numpy as np


class Intcode:
    def __init__(self, program, init=None):

        # initialize memory as a dictionary instead of array
        # this allows for arbitrary memory access, defaulting to 0
        self.memory = defaultdict(int)
        for idx, value in enumerate(program):
            self.memory[idx] = value

        self.init = init
        self.output = None
        self.pos = 0
        self.relative_base = 0
        self.modes = []
        self.first_run = True
        self.done = False

    def modify(self, modifications):
        for (address, value) in modifications.items():
            self.memory[address] = value

    def value(self, mode):
        if mode == 0:
            return self.memory[self.memory[self.pos]]
        elif mode == 1:
            return self.memory[self.pos]
        elif mode == 2:
            return self.memory[self.memory[self.pos + self.relative_base]]
        else:
            raise ValueError(f"Unknown mode: {mode}")

    def add_mul(self, opcode):  # [1/2, a, b, c]
        """Addition and multiplication only differ by the np.sum() and np.prod()."""
        self.modes += [0] * (
            3 - len(self.modes)
        )  # pad to handle leading 0 in instruction
        self.pos += 1  # increment to get to parameters

        params = []
        for _ in range(2):  # we only want the modes for a and b
            m = self.modes.pop(0)
            params.append(self.value(m))
            self.pos += 1

        # We must pop or the mode list will grow and become wrong
        m = self.modes.pop(0)
        assert m == 0  # x will always be a position in memory (mode 0)

        if opcode == 1:
            self.memory[self.memory[self.pos]] = np.sum(params)
        elif opcode == 2:
            self.memory[self.memory[self.pos]] = np.prod(params)

        self.pos += 1

    def save(self, signal=None):  # [3, a]
        self.modes += [0] * (
            1 - len(self.modes)
        )  # pad to handle leading 0 in instruction
        assert all(self.modes) == 0

        _ = self.modes.pop(0)  # not used, but we add and pop for consistency
        v = self.memory[self.pos + 1]

        if self.first_run:
            if self.init is not None:
                self.memory[v] = int(self.init)
            else:
                self.memory[v] = int(input(f"Insert number to store at position {v}: "))
            self.first_run = False
        else:
            self.memory[v] = signal

        self.pos += 2

    def load(self):  # [4, a]
        self.pos += 2
        self.modes += [0] * (
            1 - len(self.modes)
        )  # pad to handle leading 0 in instruction
        _ = self.modes.pop(0)
        self.output = self.memory[self.memory[self.pos - 1]]

    def jump_t(self):  # [5, a, b]
        self.modes += [0] * (
            2 - len(self.modes)
        )  # pad to handle leading 0 in instruction
        m = self.modes.pop(0)

        self.pos += 1
        if self.value(m) != 0:
            m = self.modes.pop(0)
            self.pos += 1
            self.pos = self.value(m)
        else:
            self.pos += 2
            _ = self.modes.pop(0)

    def jump_f(self):  # [6, a, b]
        self.modes += [0] * (
            2 - len(self.modes)
        )  # pad to handle leading 0 in instruction
        m = self.modes.pop(0)

        self.pos += 1
        if self.value(m) == 0:
            m = self.modes.pop(0)
            self.pos += 1
            self.pos = self.value(m)
        else:
            self.pos += 2
            _ = self.modes.pop(0)

    def less(self):  # [7, a, b, c]
        self.pos += 1  # increment to get to parameters
        self.modes += [0] * (
            3 - len(self.modes)
        )  # pad to handle leading 0 in instruction

        params = []
        for _ in range(2):  # we want the modes for a, b
            m = self.modes.pop(0)
            v = self.memory[self.pos]
            if m == 0:
                params.append(self.memory[v])
            if m == 1:
                params.append(v)
            self.pos += 1

        m = self.modes.pop(0)
        assert m == 0

        if params[0] < params[1]:
            self.memory[self.memory[self.pos]] = 1
        else:
            self.memory[self.memory[self.pos]] = 0

        self.pos += 1

    def eq(self):  # [8, a, b, c]
        self.pos += 1  # increment to get to parameters
        self.modes += [0] * (
            3 - len(self.modes)
        )  # pad to handle leading 0 in instruction

        params = []
        for _ in range(2):  # we want the modes for a, b
            m = self.modes.pop(0)
            v = self.memory[self.pos]
            if m == 0:
                params.append(self.memory[v])
            if m == 1:
                params.append(v)
            self.pos += 1

        m = self.modes.pop(0)
        assert m == 0

        if params[0] == params[1]:
            self.memory[self.memory[self.pos]] = 1
        else:
            self.memory[self.memory[self.pos]] = 0

        self.pos += 1

    def adj_base(self):  # [9, a]
        self.pos += 1
        self.modes += [0] * (
            1 - len(self.modes)
        )  # pad to handle leading 0 in instruction
        m = self.modes.pop(0)
        self.relative_base += self.value(m)
        self.pos += 1

    def run(self, signal=None):
        """Run the program in memory."""

        counter = 0
        try:
            while True:

                instr = self.memory[self.pos]
                opcode = int(str(instr)[-2:])
                self.modes = [int(p) for p in str(instr)[:-2][::-1]]

                match opcode:
                    case 99:
                        self.done = True
                        return (None, opcode)
                    case 1:
                        self.add_mul(1)
                    case 2:
                        self.add_mul(2)
                    case 3:
                        self.save(signal)
                    case 4:
                        self.load()
                        return (self.output, opcode)
                    case 5:
                        self.jump_t()
                    case 6:
                        self.jump_f()
                    case 7:
                        self.less()
                    case 8:
                        self.eq()
                    case 9:
                        self.adj_base()
                    case _:
                        raise ValueError(f"Unknown OP Code: {opcode}")

                assert len(self.modes) == 0  # prev op should have emptied modes
                counter += 1
                if counter > 1000:
                    print("Stopping because of counter!")
                    return

        except:
            print(f"Counter: {counter}")
            print(f"Instr: {instr}")
            print(f"OP Code: {opcode}")
            print(f"Modes: {self.modes}")
            print(f"Position: {self.pos}")
            print(self.memory)
            raise
