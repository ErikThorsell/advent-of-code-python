"""An OP Code Module"""

from typing import List, Tuple


def op_init(input: List[int], noun, verb: int) -> List[int]:
    input[1] = noun
    input[2] = verb
    try:
        return op(input)
    except:
        return []


def op(input: List[int]) -> List[int]:
    """Run the input as an OP Code Program"""

    pos = 0
    while True:

        opcode = input[pos]

        # ABORT
        if opcode == 99:
            return input

        # ADD
        elif opcode == 1:
            r1 = input[pos + 1]
            r2 = input[pos + 2]
            r3 = input[pos + 3]
            input[r3] = input[r1] + input[r2]
            pos += 4

        # MULTIPLY
        elif opcode == 2:
            r1 = input[pos + 1]
            r2 = input[pos + 2]
            r3 = input[pos + 3]
            input[r3] = input[r1] * input[r2]
            pos += 4

        else:
            raise ValueError(f"Something went wrong, got opcode: {opcode}")
