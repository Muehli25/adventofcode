with open("./input.txt") as file:
    input = [i.strip() for i in file.readlines()]

depth = 0
horizontal_pos = 0

for position in input:
    command, value = position.split(" ")
    if command == "up":
        depth -= int(value)
    elif command == "down":
        depth += int(value)
    elif command == "forward":
        horizontal_pos += int(value)

print(depth * horizontal_pos)