with open("./input.txt") as file:
    input = [int(i.strip()) for i in file.readlines()]

increased_counter = 0

for i in range(1, len(input)):
    if input[i -1] < input[i]:
        increased_counter +=1

print(increased_counter)
