from io import StringIO

from advent_of_code.utils.intcode import Intcode


def test_day_2():
    program = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    intcode = Intcode(program)
    intcode.run()
    assert intcode.memory[0] == 3500


def test_save_load():
    program = [3, 0, 4, 0, 99]
    intcode = Intcode(program)
    intcode.run()
    assert intcode.memory[0] == int(input("Input the same number again: "))


def test_modes():
    program = [1002, 4, 3, 4, 33]
    intcode = Intcode(program)
    intcode.run()
    assert intcode.memory[4] == 99


def test_neg():
    program = [1101, 100, -1, 4, 0]
    intcode = Intcode(program)
    intcode.run()
    print(intcode.memory)


def test_jump_pos():
    program = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    intcode = Intcode(program)
    intcode.run()


def test_jump_imm():
    program = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    intcode = Intcode(program)
    intcode.run()


def test_less_pos(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("8"))
    program = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    intcode = Intcode(program)
    intcode.run()


def test_less_imm():
    program = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    intcode = Intcode(program)
    intcode.run()


def test_eq_pos(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("8"))
    program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    intcode = Intcode(program)
    intcode.run()


def test_eq_imm():
    program = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    intcode = Intcode(program)
    intcode.run()


def test_day_5():
    program = [
        3,
        21,
        1008,
        21,
        8,
        20,
        1005,
        20,
        22,
        107,
        8,
        21,
        20,
        1006,
        20,
        31,
        1106,
        0,
        36,
        98,
        0,
        0,
        1002,
        21,
        125,
        20,
        4,
        20,
        1105,
        1,
        46,
        104,
        999,
        1105,
        1,
        46,
        1101,
        1000,
        1,
        20,
        4,
        20,
        1105,
        1,
        46,
        98,
        99,
    ]
    intcode = Intcode(program, 5)
    intcode.run()
