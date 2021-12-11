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
    values = { "(" :1, "[": 2,"{": 3, "<": 4 }
    results = []

    opening = "([{<"
    closing = ")]}>"  
      
    incomplete = []
    for line in input:
        sub_score = 0
        stack = []
        incomplete = True
        for l in line:
            if l in opening:
                stack.append(l)
            elif l in closing:
                pos = closing.index(l)
                if opening[pos] != stack[-1]:
                    incomplete = False
                    break
                stack.pop()
        if incomplete:
            for bracket in stack[::-1]:
                sub_score = sub_score * 5 + values[bracket]
            results.append(sub_score)

    results = sorted(results)
    return results[len(results) // 2]

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
