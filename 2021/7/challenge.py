import numpy as np
from tqdm import tqdm

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

def part_1(input):
    crabs =  [*map(int, input[0].split(","))]
    smallest_index = min(crabs)
    biggest_index = max(crabs)

    fuel_consumption = dict()

    for i in range(smallest_index, biggest_index):
        test_numbers = [i] * len(crabs)
        fuel_consumption[i] = sum(list(abs(np.array(crabs) - np.array(test_numbers))))

    return min(fuel_consumption.values())

def part_2(input):
    crabs =  [*map(int, input[0].split(","))]
    smallest_index = min(crabs)
    biggest_index = max(crabs)

    fuel_consumption = dict()

    for i in tqdm(range(smallest_index, biggest_index)):
        test_numbers = [i] * len(crabs)
        difference = list(abs(np.array(crabs) - np.array(test_numbers)))

        fuel_consumption_dict = dict()
        for position in range(len(difference)):
            fuel_consumption_dict[position] = (difference[position] * (difference[position] + 1)) // 2
        
        fuel_consumption[i] = sum(list(fuel_consumption_dict.values()))
    return min(fuel_consumption.values())

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