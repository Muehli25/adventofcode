with open("./input.txt") as file:
    input = [i.strip() for i in file.readlines()]

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

print(gamma)

print(int(gamma,2) * int(epsilon,2))