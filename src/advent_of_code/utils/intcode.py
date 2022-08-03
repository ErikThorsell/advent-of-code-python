"""An OP Code Module"""

import numpy as np

class Intcode:

    def __init__(self, program, mode="position"):
        self.memory = program
        self.pos = 0
        self.modes = []


    def modify(self, modifications):
        for (address, value) in modifications.items():
            self.memory[address] = value

    def value(self, mode, pos):
        if mode == 0:
            return self.memory[self.memory[pos]]
        return self.memory[pos]


    def add_mul(self, opcode):  # [1/2, a, b, c]
        """Addition and multiplication only differ by the np.sum() and np.prod()."""
        self.pos += 1  # increment to get to parameters
        self.modes += [0] * (3 - len(self.modes))  # pad to handle leading 0 in instruction

        params = []
        for _ in range(2):  # we only want the modes for a and b
            m = self.modes.pop(0)
            v = self.memory[self.pos]
            if m == 0:
                params.append(self.memory[v])
            if m == 1:
                params.append(v)
            self.pos += 1

        
        # We must pop or the mode list will grow and become wrong
        m = self.modes.pop(0)
        assert m == 0  # x will always be a position in memory (mode 0)
        if opcode == 1:
            self.memory[self.memory[self.pos]] = np.sum(params)
        elif opcode == 2:
            self.memory[self.memory[self.pos]] = np.prod(params)
        self.pos += 1


    def save(self):  # [3, a]
        self.modes += [0] * (1 - len(self.modes))  # pad to handle leading 0 in instruction
        m = self.modes.pop(0)  # not used, but we add and pop for consistency
        assert m == 0
        v = self.memory[self.pos + 1]
        self.memory[v] = int(input(f"Input a number to store at position {v}: "))
        self.pos += 2


    def load(self):  # [4, a]
        self.modes += [0] * (1 - len(self.modes))  # pad to handle leading 0 in instruction
        v = self.memory[self.pos + 1]
        if m := self.modes.pop(0) == 0:
            print(self.memory[v])
        elif m == 1:
            print(v)
        self.pos += 2


    def jump_t(self):  # [5, a, b]
        self.modes += [0] * (2 - len(self.modes))  # pad to handle leading 0 in instruction
        m = self.modes.pop(0)

        if m == 0:
            if self.memory[self.memory[self.pos+1]] != 0:
                self.pos = self.memory[self.memory[self.pos+2]]
            else:
                self.pos += 3
        elif m == 1:
            if self.memory[self.pos+1] != 0:
                self.pos = self.memory[self.pos+2]
            else:
                self.pos += 3
        
        _ = self.modes.pop(0)


    def jump_f(self):  # [6, a, b]
        self.modes += [0] * (2 - len(self.modes))  # pad to handle leading 0 in instruction
        m = self.modes.pop(0)

        if m == 0:
            if self.memory[self.memory[self.pos+1]] == 0:
                self.pos = self.memory[self.memory[self.pos+2]]
            else:
                self.pos += 3
        elif m == 1:
            if self.memory[self.pos+1] == 0:
                self.pos = self.memory[self.pos+2]
            else:
                self.pos += 3

        _ = self.modes.pop(0)


    def less(self):  # [7, a, b, c]
        self.pos += 1  # increment to get to parameters
        self.modes += [0] * (3 - len(self.modes))  # pad to handle leading 0 in instruction

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
        self.modes += [0] * (3 - len(self.modes))  # pad to handle leading 0 in instruction

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


    def run(self):
        """Run the program in memory."""

        counter = 0
        try:
            while True:

                instruction = self.memory[self.pos]
                opcode = int(str(instruction)[-2:])
                self.modes = [int(p) for p in str(instruction)[:-2][::-1]]

                match opcode:
                    case 99:
                        return 
                    case 1:
                        self.add_mul(1)
                    case 2:
                        self.add_mul(2)
                    case 3:
                        self.save()
                    case 4:
                        self.load()
                    case 5:
                        self.jump_t()
                    case 6:
                        self.jump_f()
                    case 7:
                        self.less()
                    case 8:
                        self.eq()
                    case _:
                        raise ValueError(f"Unknown OP Code: {opcode}")
            
                assert len(self.modes) == 0  # prev op should have emptied modes
                counter += 1
                if counter > 1000:
                    print("Stopping because of counter!")
                    return

        except:
            print(f"Counter: {counter}")
            print(f"Instr: {instruction}")
            print(f"OP Code: {opcode}")
            print(f"Modes: {self.modes}")
            print(f"Position: {self.pos}")
            print(self.memory)
            raise
