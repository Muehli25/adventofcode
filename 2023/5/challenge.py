import os
# ------ Read Input ------
path, _ = os.path.split(os.path.abspath(__file__))

def input_data():
    with open(f"{path}/data/input.txt") as file:
        return [i.strip() for i in file.readlines()]


def test_data():
    with open(f"{path}/data/test_1.txt") as file:
        return [i.strip() for i in file.readlines()]


def test_data_2():
    with open(f"{path}/data/test_2.txt") as file:
        return [i.strip() for i in file.readlines()]


def result_challenge_1():
    with open(f"{path}/data/result_test_1.txt") as file:
        return int(file.read())


def result_challenge_2():
    with open(f"{path}/data/result_test_2.txt") as file:
        return int(file.read())

# ------ Helper ------

def get_seeds(input):
    _, seeds = input.split(": ")
    seeds = [int(x.strip()) for x in seeds.split(" ") if x]
    return seeds

def get_mapping(source, map_list):
    for dest_start, source_start, length in map_list:
        if source_start <= source < source_start + length:
            return dest_start + (source - source_start)
    return source

def create_mapping(input, map_line):
    start = input.index(map_line)
    try:
        end = input.index("", start)
    except:
        end = len(input)
    mapping = []
    for line in input[start + 1:end]:
        source, dest, step = [int(x) for x in line.split()]
        mapping.append((source, dest, step))
    return mapping

# ------ Parts ------
def part_1(input):
    seeds = get_seeds(input[0])
    
    maps = [
        create_mapping(input, "seed-to-soil map:"),
        create_mapping(input, "soil-to-fertilizer map:"),
        create_mapping(input, "fertilizer-to-water map:"),
        create_mapping(input, "water-to-light map:"),
        create_mapping(input, "light-to-temperature map:"),
        create_mapping(input, "temperature-to-humidity map:"),
        create_mapping(input, "humidity-to-location map:")
    ]

    locations = []
    for seed in seeds:
        for map in maps:
            seed = get_mapping(seed, map)
        locations.append(seed)
    return min(locations)


def part_2(input):
    return 0

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
