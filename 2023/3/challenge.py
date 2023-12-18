import os
from enum import Enum
from operator import mul

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
    symbol_positions = []
    currently_number = False
    current_number = ""
    current_number_pos = ()
    current_state = State.FIRST

    for row, line in enumerate(input):
        line = parse_data(line)
        for col, symbol in enumerate(line):
            if symbol == "*":
                symbol_positions.append((row, line.index(symbol, col)))
    result = []

    for current_symbol in symbol_positions:
        current_state= State.FIRST
        first_number = 0
        second_number = 0
        for row, line in enumerate(input):
            line = parse_data(line)
            for col, symbol in enumerate(line):
                if symbol == " ":
                    if currently_number:
                        currently_number = False
                        if current_state == State.FIRST:
                            if is_neighbor([current_symbol], (current_number_pos,current_number)):
                                first_number = int(current_number)
                                current_state= State.SECOND
                        elif current_state == State.SECOND:
                            if is_neighbor([current_symbol], (current_number_pos,current_number)):
                                second_number = int(current_number)
                                current_state= State.CORRECT
                        else: 
                            if is_neighbor([current_symbol], (current_number_pos,current_number)):
                                current_state = State.ERROR
                                print("ERROR", first_number, second_number, current_number)
                elif not symbol in "1234567890" and symbol == "*":
                    if currently_number:
                        currently_number = False
                        if current_state == State.FIRST:
                            if is_neighbor([current_symbol], (current_number_pos,current_number)):
                                first_number = int(current_number)
                                current_state= State.SECOND
                        elif current_state == State.SECOND:
                            if is_neighbor([current_symbol], (current_number_pos,current_number)):
                                second_number = int(current_number)
                                current_state= State.CORRECT
                        else: 
                            if is_neighbor([current_symbol], (current_number_pos,current_number)):
                                current_state = State.ERROR
                                print("ERROR", first_number, second_number, current_number)
                else:
                    if currently_number:
                        current_number = current_number + symbol
                    else:
                        current_number_pos = (row, col)
                        current_number = symbol
                        currently_number = True
        if current_state == State.CORRECT:
            result.append([first_number, second_number])
            
    return sum(mul(*num) for num in result)

def is_neighbor(symbol_positions, number):
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
    (row, cols) , value = number
    for i in range(len(value)):
        if (row, cols + i) in allowed_pos:
            return True
    return False

def parse_data(line):
    return line.replace(".", " ")

class State(Enum):
    FIRST = 1
    SECOND = 2
    CORRECT = 3
    ERROR = 4

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
