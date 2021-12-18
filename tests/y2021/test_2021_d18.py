"""TEST MODULE"""
import ast
from functools import reduce

from advent_of_code.y2021.d18 import solution_1
from advent_of_code.y2021.d18 import solution_2
from advent_of_code.y2021.d18 import explode, add


def test_explode():
    example_input = [
        [[[[[9, 8], 1], 2], 3], 4],
        [7, [6, [5, [4, [3, 2]]]]],
        [[6, [5, [4, [3, 2]]]], 1],
        [[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]],
        [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]],
    ]
    example_result = [
        [[[[0, 9], 2], 3], 4],
        [7, [6, [5, [7, 0]]]],
        [[6, [5, [7, 0]]], 3],
        [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]],
        [[3, [2, [8, 0]]], [9, [5, [7, 0]]]],
    ]
    e = 2
    print(f"\nTest case: {e}")
    _, _, expr, _ = explode(example_input[e])
    assert expr == example_result[e]


def test_add_1():
    example_input = [
        [[[[4, 3], 4], 4], [7, [[8, 4], 9]]],
        [1, 1],
    ]
    example_result = [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]
    assert add(example_input[0], example_input[1]) == example_result


def test_add_2():
    example_input_l = [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]]
    example_input_r = [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]
    example_result = [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]]
    assert add(example_input_l, example_input_r) == example_result


def test_reduce():
    example_input = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]"""
    example_result = [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]
    parsed_input = list(map(ast.literal_eval, example_input.splitlines()))
    assert reduce(add, parsed_input) == example_result


def test_solution_1():
    example_input = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""
    example_result = 4140
    parsed_input = list(map(ast.literal_eval, example_input.splitlines()))
    assert solution_1(parsed_input) == example_result


def test_solution_2():
    example_input = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""
    example_result = 3993
    parsed_input = list(map(ast.literal_eval, example_input.splitlines()))
    assert solution_2(parsed_input) == example_result
