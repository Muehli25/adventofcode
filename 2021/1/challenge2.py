with open("./input.txt") as file:
    input = [int(i.strip()) for i in file.readlines()]

sliding_windows = []

for i in range( 2,len(input)):
    sliding_windows.append(input[i] + input[i-1] + input[i-2])

increased_counter = 0

for i in range(1, len(sliding_windows)):
    if sliding_windows[i -1] < sliding_windows[i]:
        increased_counter +=1

print(increased_counter)