import os
from tqdm import tqdm

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

def parse_game(input):
    parsed_input = []
    for line in input:
        game, cards = line.split(":")
        # in the test input only one space was present, maybe we need the game number in the future
        game = int(game.replace(' ',',').strip().split(",")[-1])
        winning_numbers, my_numbers = cards.strip().split("|")
        winning_numbers, my_numbers = numbers_only_array(winning_numbers), numbers_only_array(my_numbers)
        parsed_input.append((game, winning_numbers, my_numbers))
    return parsed_input

def numbers_only_array(input):
    return [int(i) for i in input.strip().split(" ") if i and i != " "]

def recursive_games_2(raw_games, input):
    if len(input) == 0:
        return 0
    value = len(input)
    for game in input:
        nr, win_num, my_num = game
        winning_games = len([x for x in my_num if x in win_num])
        if winning_games > 0:
            value += recursive_games_2(raw_games, raw_games[nr:nr + winning_games])

    return value

# ------ Parts ------
def part_1(input):
    input = parse_game(input)
    result = 0
    for game in input:
        nr, win_num, my_num = game
        if len([x for x in my_num if x in win_num]) > 0:
            result += 2 ** (len([x for x in my_num if x in win_num]) -1)
    return result


def part_2(input):
    input = parse_game(input)
    return recursive_games_2(input, input)

if __name__ == "__main__":
    if part_1(test_data()) == result_challenge_1():
        print("Challenge 1: Success ! 🥳")
        print(f"Final Solution for Challenge 1: {part_1(input_data())}")
    else:
        print("Challenge 1: Implementation is wrong! 😔")

    if part_2(test_data()) == result_challenge_2():
        print("Challenge 2: Success ! 🥳")
        print(f"Final Solution for Challenge 2: {part_2(input_data())}")
    else:
        print("Challenge 2: Implementation is wrong! 😔")
