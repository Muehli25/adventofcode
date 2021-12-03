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


def part_1(input):
    gamma_rate = []
    epsilon_rate = []
    data_len = len(input[0])

    for i in range(0, data_len):
        num_0 = 0
        num_1 = 0
        for j in range(0, len(input)):
            if input[j][i] == "1":
                num_1 += 1
            else:
                num_0 += 1
        gamma_rate.append("0" if num_1 < num_0 else "1")
        epsilon_rate.append("1" if num_1 < num_0 else "0")
    
    gamma = ''.join(gamma_rate)
    epsilon = ''.join(epsilon_rate)

    return int(gamma,2) * int(epsilon,2)

def part_2(input):
    data_len = len(input[0])

    oxygen_list = copy.deepcopy(input)
    co2_list = copy.deepcopy(input)

    result_o2 = ""
    result_co2 = ""

    for i in range(0, data_len):
        count_1 = 0
        count_0 = 0

        for j in range(0, len(oxygen_list)):
            if oxygen_list[j][i] == "1":
                count_1 += 1
            else:
                count_0 += 1
        
        num_o2 = "1" if count_1 >= count_0 else "0"

        oxygen_list_copy = copy.deepcopy(oxygen_list)
        for x in range(0, len(oxygen_list)):
            if oxygen_list[x][i] != num_o2:
                oxygen_list_copy.remove(oxygen_list[x])
        oxygen_list = oxygen_list_copy

        #print(f"oxygen in {oxygen_list}")

        if len(oxygen_list) == 1:
            result_o2 = oxygen_list[0]


        count_1 = 0
        count_0 = 0
        for j in range(0, len(co2_list)):
            if co2_list[j][i] == "1":
                count_1 += 1
            else:
                count_0 += 1

        num_co2 = "0" if count_1 >= count_0 else "1"

        co2_list_copy = copy.deepcopy(co2_list)
        for x in range(0, len(co2_list)):
            if co2_list[x][i] != num_co2:
                co2_list_copy.remove(co2_list[x])
        co2_list = co2_list_copy

        if len(co2_list) == 1:
            result_co2 = co2_list[0]

    return int(result_o2,2) * int(result_co2,2)

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