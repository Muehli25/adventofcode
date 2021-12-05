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

def clean_input_data(input):
    points = []
    for line in input:
        coordinate_1, coordinate_2 = line.split(" -> ")
        x1,y1 = [int(x) for x in coordinate_1.split(",")]
        x2,y2 = [int(y) for y in coordinate_2.split(",")]
        if x1 == x2 or y1 == y2:
            points.append((x1,y1))
            points.append((x2,y2))
            if x1 == x2 and y1 < y2:
                for i in range(y1+1,y2):
                    points.append((x1,y1+(i-y1)))

            elif x1 == x2 and y1 > y2:
                for i in range(y2+1,y1):
                    points.append((x1,y2+(i-y2)))

            elif y1 == y2 and x1 < x2:
                for i in range(x1+1,x2):
                    points.append((x1+(i-x1),y1))

            elif y1 == y2 and x1 > x2:
                for i in range(x2+1,x1):
                    points.append((x2+(i-x2),y1))       
    return points

def create_matrix(points):
    max_x, max_y = get_size_of_matrix(points)
    matrix = dict()
    for x in range(max_x+1):
        for y in range(max_y+1):
            matrix[(x,y)] = 0
    for point in points:
        matrix[point] += 1
    return matrix

def get_size_of_matrix(points):
    max_x = 0
    max_y = 0
    for point in points:
        if point[0] > max_x:
            max_x = point[0]
        if point[1] > max_y:
            max_y = point[1]
    return max_x, max_y

def pretty_print_matrix(matrix, size_x, size_y):
    row = ""
    rows = dict()
    for y in range(size_y+1):
        rows[y] = ""
        for _ in range(size_x+1):
            rows[y] += "."
    for point in matrix.keys():
        if matrix[point] != 0:
            row = rows[point[1]]
            row = row[:point[0]] + str(matrix[point]) + row[point[0] + 1:]
            rows[point[1]] = row
    for row in rows.keys():
            print(rows[row])

def get_overlaps(matrix, limit):
    overlaps = 0
    for point in matrix.keys():
        if matrix[point] >= limit:
            overlaps += 1
    return overlaps

def part_1(input):
    points = clean_input_data(input)
    matrix = create_matrix(points)
    #size_x , size_y = get_size_of_matrix(points)
    #pretty_print_matrix(matrix, size_x , size_y )
    return get_overlaps(matrix, 2)

def part_2(input):
    matrix = {}
    for line in input:
        # extract points from input data
        point_a, point_b = [[*map(int, i.split(","))] for i in line.split(" -> ")]
        # get x and y values
        x = sorted([point_a[0], point_b[0]])
        y = sorted([point_a[1], point_b[1]])
        
        X = Y = None

        # add horizontal lines, only if x_a and x_b differ
        if len(set(x)) == 1:
            Y = [*range(y[0], y[1] + 1)]
            X = [x[0]] * len(Y)
        # vertical lines, only if y_a and y_b differ
        elif len(set(y)) == 1:
            X = [*range(x[0], x[1] + 1)]
            Y = [y[0]] * len(X)
        # diagonal, check if both value differ by the same degree
        elif x[1] - x[0] == y[1] - y[0]:
                s = 1 if point_b[0] > point_a[0] else -1
                t = 1 if point_b[1] > point_a[1] else -1
                X = [*range(point_a[0], point_b[0] + s, s)]
                Y = [*range(point_a[1], point_b[1] + t, t)]

        if X and Y:
            for p, q in zip(X, Y):
                key = p * 234567 + q
                matrix[key] = matrix.get(key, 0) + 1
    return len([i for i in matrix.values() if i > 1])

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