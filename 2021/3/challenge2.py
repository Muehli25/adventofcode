import copy

with open("./input.txt") as file:
    input = [i.strip() for i in file.readlines()]

gamma_rate = []
epsilon_rate = []

life_support_rating = 0
oxygen_generator_rating = 0
co2_scrubber_rating = 0

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

print(int(result_o2,2))
print(int(result_co2,2))

print(int(result_o2,2) * int(result_co2,2))