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

def part_1(input, days):
    fishs =  [*map(int, input[0].split(","))]
    for _ in range (0, days):
        new_fish = 0
        for i in range(0, len(fishs)):
            if fishs[i] == 0:
                fishs[i] = 6
                new_fish += 1
            else:
                fishs[i] = fishs[i] - 1
        for i in range(new_fish):
            fishs.append(8)

    return len(fishs)

def part_2(input):

    return 0

if __name__ == "__main__":
    if part_1(test_data(), 80) == result_challenge_1():
        print("Challenge 1: Success ! 🥳")
        print(f"Final Solution for Challenge 1: {part_1(input_data(), 80)}")
    else:
        print("Challenge 1: Implementation is wrong! 😔")

    if part_2(test_data()) == result_challenge_2():
        print("Challenge 2: Success ! 🥳")
        print(f"Final Solution for Challenge 2: {part_2(input_data())}")
    else:
        print("Challenge 2: Implementation is wrong! 😔")