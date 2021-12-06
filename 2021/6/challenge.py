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
    fishs =  [*map(int, input[0].split(","))]
    for _ in range (0, 80):
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
    fishs =  [*map(int, input[0].split(","))]
    
    # The first implementation is very slow because the array is growing relly fast.
    # since i don't care for the state of every fish i can optimize it by only looking at the fish in a specific state.

    fish_age = [0] * 9 # a fish can only have a value in range of 0 - 8
    
    for i in fishs:
        fish_age[i] += 1

    for _ in range (0, 256):
        x = fish_age[0]
        fish_age = fish_age[1:] + [x]
        fish_age[6] += x 
    
    return sum(fish_age)

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