from math import prod

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
    risklevel = 0
    heatmap = dict()
    for row in range(len(input)):
        for column in range(len(input[row])):
            heatmap[(row, column)] = int(input[row][column])

    for row in range(len(input)):
        for column in range(len(input[row])):
            up = heatmap.get((row-1, column)) if heatmap.get((row-1, column)) != None else 9
            down = heatmap.get((row+1, column)) if heatmap.get((row+1, column)) != None else 9
            right = heatmap.get((row, column+1)) if heatmap.get((row, column+1)) != None else 9
            left = heatmap.get((row, column-1)) if heatmap.get((row, column-1)) != None else 9

            parameter = [up,down,right,left]
            if all(i > heatmap.get((row,column)) for i in parameter ):
                risklevel += heatmap.get((row, column)) + 1

    return risklevel


def part_2(input):
    lowpoints = []
    heatmap = dict()
    for row in range(len(input)):
        for column in range(len(input[row])):
            heatmap[(row, column)] = int(input[row][column])

    for row in range(len(input)):
        for column in range(len(input[row])):
            up = heatmap.get((row+1, column)) if heatmap.get((row+1, column)) != None else 9
            down = heatmap.get((row-1, column)) if heatmap.get((row-1, column)) != None else 9
            right = heatmap.get((row, column+1)) if heatmap.get((row, column+1)) != None else 9
            left = heatmap.get((row, column-1)) if heatmap.get((row, column-1)) != None else 9

            parameter = [up,down,right,left]
            if all(i > heatmap.get((row,column)) for i in parameter ):
                lowpoints.append((row,column))

    basins = []

    for lowpoint in lowpoints:

        unchecked , checked = [lowpoint], set([lowpoint])
        while len(unchecked) != 0:
            prev_unchecked, unchecked = unchecked, []

            for row, column in prev_unchecked:
                up = heatmap.get((row+1, column)) if heatmap.get((row+1, column)) != None else 9
                down = heatmap.get((row-1, column)) if heatmap.get((row-1, column)) != None else 9
                right = heatmap.get((row, column+1)) if heatmap.get((row, column+1)) != None else 9
                left = heatmap.get((row, column-1)) if heatmap.get((row, column-1)) != None else 9

                if row < len(input) and up < 9 and (row+1, column) not in checked:
                    checked.add((row+1, column))
                    unchecked.append((row+1, column))

                if row >= 0 and down < 9 and (row-1, column) not in checked:
                    checked.add((row-1, column))
                    unchecked.append((row-1, column))

                if column < len(input[0]) and right < 9 and (row, column+1) not in checked:
                    checked.add((row, column+1))
                    unchecked.append((row, column+1))
                if column >= 0 and left < 9 and (row, column-1) not in checked:
                    checked.add((row, column-1))
                    unchecked.append((row, column-1))
                    
        basins.append(len(checked))
    return prod(sorted(basins)[-3:])


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
