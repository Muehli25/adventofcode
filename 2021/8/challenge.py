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
    data = [i.split("|") for i in input]
    number_of_signal_lines_per_number = dict()
    number_of_signal_lines_per_number[1] = 2
    number_of_signal_lines_per_number[4] = 4
    number_of_signal_lines_per_number[7] = 3
    number_of_signal_lines_per_number[8] = 7

    instances = 0
    for signal, output in data:
        for digits in output.split(" "):
            if len(digits) in (2,4,3,7):
                instances += 1

    return instances

def part_2(input):
    return 0

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