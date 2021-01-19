# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pathlib
import time

DIR = pathlib.Path(__file__).parent.absolute()


def create_pattern(counter, size):
    pattern = []
    needed_iterations = int(size / 4) + 1
    for i in range(0, needed_iterations):
        for i in range(0, counter):
            pattern.append(0)
        if len(pattern) > size + 1:
            pattern = pattern[1:]
            pattern.append(0)
            return pattern

        for i in range(0, counter):
            pattern.append(1)
        if len(pattern) > size + 1:
            pattern = pattern[1:]
            pattern.append(0)
            return pattern

        for i in range(0, counter):
            pattern.append(0)
        if len(pattern) > size + 1:
            pattern = pattern[1:]
            pattern.append(0)
            return pattern

        for i in range(0, counter):
            pattern.append(-1)
        if len(pattern) > size + 1:
            pattern = pattern[1:]
            pattern.append(0)
            return pattern

    return pattern


def get_num_array(input):
    return [int(x) for x in str(input)]


def get_phase(input_number):
    num_array = get_num_array(input_number)
    result = []
    for i in range(len(num_array)):
        temp_result = 0
        pattern = create_pattern(i + 1, len(num_array))
        for j in range(i, len(num_array)):
            pattern_pos = int(pattern[j])
            number = int(num_array[j])
            if pattern_pos != 0 and number != 0:
                temp_result += pattern_pos * number
        result.append(abs(temp_result) % 10)

    return result


def get_string_from_num(array):
    return ''.join(map(str, array))


def challenge(input):
    result = input
    for i in range(100):
        temp = get_phase(result)
        result = get_string_from_num(temp)

    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test0 = 80871224585914546619083218645595
    test1 = 19617804207202209144916044189917
    test2 = 69317163492948606335995924319873

    result0 = 24176176
    result1 = 73745418
    result2 = 52432133

    print("Control values should be true:")
    print(result0 == int(challenge(test0)[0:8]))
    print(result1 == int(challenge(test1)[0:8]))
    print(result2 == int(challenge(test2)[0:8]))

    with open(DIR / 'input.txt') as f:
        input = f.read().split("\n")[0]
    tic = time.perf_counter()
    print(f'Result: {int(challenge(input)[0:8])}')
    toc = time.perf_counter()
    print(f"Took {toc - tic:0.4f} seconds")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
