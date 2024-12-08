import os

# ------ Read Input ------
path, _ = os.path.split(os.path.abspath(__file__))

def input_data():
    with open(f"{path}/data/input.txt") as file:
        return [i.strip() for i in file.readlines()]


def test_data():
    with open(f"{path}/data/test_1.txt") as file:
        return [i.strip() for i in file.readlines()]


def test_data_2():
    with open(f"{path}/data/test_2.txt") as file:
        return [i.strip() for i in file.readlines()]


def result_challenge_1():
    with open(f"{path}/data/result_test_1.txt") as file:
        return int(file.read())


def result_challenge_2():
    with open(f"{path}/data/result_test_2.txt") as file:
        return int(file.read())

# ------ Helper ------
import re
import numpy as np

def transpose_input(input):
    transpose_input_array = []
    num_columns = len(input[0])
    num_rows = len(input)
    for column in range(num_columns):
        column_string = ""
        for row in range(num_rows):
            column_string = f"{column_string}{input[row][column]}"
        transpose_input_array.append(column_string)
    return transpose_input_array

def horizontal(input):
    xmas = "XMAS"
    xmas_reversed = "SAMX"
    result = 0
    for line in input:
        result += len(re.findall(xmas, line))
        result += len(re.findall(xmas_reversed, line))
    return result

def vertical(input):
    return horizontal(transpose_input(input))

def diagonal(input, row, col):
    result = 0
    try:
        if input[row][col] == "X" and input[row+1][col+1] == "M" and input[row+2][col+2] == "A" and input[row+3][col+3] == "S":
            result += 1
    except IndexError:
        result += 0
    try:
        if col >= 3 and input[row][col] == "X" and input[row+1][col-1] == "M" and input[row+2][col-2] == "A" and input[row+3][col-3] == "S":
            result += 1
    except IndexError:
        result += 0
    try:    
        if row >= 3 and input[row][col] == "X" and input[row-1][col+1] == "M" and input[row-2][col+2] == "A" and input[row-3][col+3] == "S":
            result += 1
    except IndexError:
        result += 0
    try:
        if row >= 3 and col >= 3 and input[row][col] == "X" and input[row-1][col-1] == "M" and input[row-2][col-2] == "A" and input[row-3][col-3] == "S":
            result += 1
    except IndexError:
        result += 0
    return result

# ------ Parts ------
def part_1(input):
    result = 0
    result += horizontal(input)
    result += vertical(input)
    for row in range(len(input)):
        for column in range(len(input[0])):
            if(input[row][column] == "X"):
                result += diagonal(input, row, column)
    return result


def part_2(input):
    return 0

if __name__ == "__main__":
    if part_1(test_data()) == result_challenge_1():
        print("Challenge 1: Success ! 🥳")
        print(f"Final Solution for Challenge 1: {part_1(input_data())}")
    else:
        print("Challenge 1: Implementation is wrong! 😔")

    if part_2(test_data_2()) == result_challenge_2():
        print("Challenge 2: Success ! 🥳")
        print(f"Final Solution for Challenge 2: {part_2(input_data())}")
    else:
        print("Challenge 2: Implementation is wrong! 😔")
