import copy

def input_data():
    with open("./data/input.txt") as file:
        return [i.strip() for i in file.readlines()]
    
def test_data():    
    with open("./data/test.txt") as file:
        return [i.strip() for i in file.readlines()]

def result_challenge_1():
    with open("./data/result_test_1.txt") as file:
        return int(file.read())

def result_challenge_2():
    with open("./data/result_test_2.txt") as file:
        return int(file.read())


def extract_numbers_and_boards(input):
    numbers = [int(i) for i in input[0].split(',')]
    bingo_fields = []
    for i in range(2, len(input), 6):
        bingo_fields_temp = [input[i], input[i+1], input[i+2], input[i+3], input[i+4]]
        rows = []
        for row in range(0,5):
            input_columns = bingo_fields_temp[row].split()
            columns = []
            for column in range(0,len(input_columns)):
                columns.append((int(input_columns[column]), False))
            rows.append(columns)
        bingo_fields.append(rows)
    return numbers, bingo_fields

def mark_number_in_bingo(number, board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column][0] == number:
                board[row][column] = (number, True)
    return board

def check_for_solution(board):
    for row in range(len(board)):
        result = True
        for column in range(len(board[row])):
            if result:
                result = board[row][column][1]
        if result:
            return True

    for column in range(5):
        result = True
        for row in range(5):
            if result:
                result = board[row][column][1]
        if result:
            return True

    return False

def get_sum_of_missing_numbers(board):
    sum = 0
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column][1] == False:
                sum += board[row][column][0]

    return sum
    
def pretty_print_bingo(board):
    for row in board:
        print(row)
    print(" ")

def part_1(input):
    numbers, bingo_fields = extract_numbers_and_boards(input)
    for number in numbers:
        for board in bingo_fields:
            board = mark_number_in_bingo(number, board)
            if check_for_solution(board):
                return number * get_sum_of_missing_numbers(board)
    return 0

def part_2(input):
    numbers, bingo_fields = extract_numbers_and_boards(input)
    bingos_done = 0
    for number in numbers:
        for board in bingo_fields:
            if check_for_solution(board):
                continue
            board = mark_number_in_bingo(number, board)
            if check_for_solution(board):
                bingos_done += 1
                if bingos_done == len(bingo_fields):
                    return number * get_sum_of_missing_numbers(board)
    return 0

if __name__ == "__main__":
    if part_1(test_data()) == result_challenge_1():
        print("Challenge 1: Success ! 🥳")
        print(f"Final Solution for Challenge 1: {part_1(input_data())}")
    else:
        print("Challenge 1: Implementation is wrong! 😔")

    if part_2(test_data()) == result_challenge_2():
        print("Challenge 2: Success ! 🥳")
        print(f"Final Solution for Challenge 1: {part_2(input_data())}")
    else:
        print("Challenge 2: Implementation is wrong! 😔")