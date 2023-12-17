import os
import re

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


def part_1(input):
    result = 0
    symbol_positions = []
    currently_number = False
    current_number = ""
    current_number_pos = ()
    numbers = []
    for row, line in enumerate(input):
        line = parse_data(line)
        for col, symbol in enumerate(line):
            if symbol == " ":
                if currently_number:
                    currently_number = False
                    numbers.append((current_number_pos,current_number))
            elif not symbol in "1234567890":
                if currently_number:
                    currently_number = False
                    numbers.append((current_number_pos,current_number))
                symbol_positions.append((row, line.index(symbol, col)))
            else:
                if currently_number:
                    current_number = current_number + symbol
                else:
                    current_number_pos = (row, col)
                    current_number = symbol
                    currently_number = True
                
    allowed_pos = []
    for symbol in symbol_positions:
        allowed_pos.append((symbol[0]-1,symbol[1]-1))
        allowed_pos.append((symbol[0]-1,symbol[1]))
        allowed_pos.append((symbol[0]-1,symbol[1]+1))
        allowed_pos.append((symbol[0],symbol[1]+1))
        allowed_pos.append((symbol[0],symbol[1]-1))
        allowed_pos.append((symbol[0]+1,symbol[1]-1))
        allowed_pos.append((symbol[0]+1,symbol[1]))
        allowed_pos.append((symbol[0]+1,symbol[1]+1))
    result = 0
    for number in numbers:
        (row, cols) , value = number
        for i in range(len(value)):
            if (row, cols + i) in allowed_pos:
                result = result + int(value)
                break
    return result

def part_2(input):
    result = 0
    return result

def is_neighbor(pos_symbol, number):
    list_neighbors = []
    for i in range(len(number.value())):
        print(i)

def parse_data(line):
    return line.replace(".", " ")

def get_adjacent_numbers(input, x, y):
    return y

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
