import string 

def input_data():
    with open("./data/input.txt") as file:
        return [i.strip() for i in file.readlines()]


def test_data():
    with open("./data/test.txt") as file:
        return [i.strip() for i in file.readlines()]


def test_data_2():
    with open("./data/test_2.txt") as file:
        return [i.strip() for i in file.readlines()]


def result_challenge_1():
    with open("./data/result_test_1.txt") as file:
        return int(file.read())


def result_challenge_2():
    with open("./data/result_test_2.txt") as file:
        return int(file.read())


def part_1(input):
    result = 0
    for line in input:
        numbers = [i for i in line if i in string.digits]
        result = result + int(numbers[0] + numbers[-1])
    return result


def part_2(input):
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    digits_dict = {"one" :"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    input_cleanup = [e.replace(key, val) for e in input for key, val in digits_dict.items() if key in e]
    result = 0
    input_cleaned = []
    for line in input:
        print(line)
        updated_line
    #     for j in range(len(line)):
    #         if line[:j] in digits:
    #             line = line.replace(line[:j], str(digits.index(line[:j])+1))
    #     print(line)
    #     for j in range(len(line), 0, -1):
    #         print(line[j:])
    #         if line[j:] in digits:
    #             line = line.replace(line[j:], str(digits.index(line[j:])+1))
    #     print(line)
    #     # for i, digstr in enumerate(digits):
    #     #     line = line.replace(digstr, str(i+1))
    #     numbers = [i for i in line if i in string.digits]
    #     print(numbers)
    #     result = result + int(numbers[0] + numbers[-1])
    #     print(result)
    #     print("")
    return result

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
