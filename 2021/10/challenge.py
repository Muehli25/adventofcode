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
    values = { ")" :3, "]": 57,"}": 1197, ">": 25137 }
    score = 0

    opening = "([{<"
    closing = ")]}>"  
      
    for line in input:
        stack = []
        for l in line:
            if l in opening:
                stack.append(l)
            elif l in closing:
                pos = closing.index(l)
                if opening[pos] != stack[-1]:
                    score += values[l]
                    break
                stack.pop()
    return score


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
