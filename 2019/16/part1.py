# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pathlib

DIR = pathlib.Path(__file__).parent.absolute()

def create_pattern(counter, size):
    pattern = []
    needed_iterations = int(size / 4) + 1
    for i in range(0,needed_iterations):
        for i in range(0,counter):
            pattern.append(0)
        for i in range(0, counter):
            pattern.append(1)
        for i in range(0,counter):
            pattern.append(0)
        for i in range(0, counter):
            pattern.append(-1)
        if len(pattern) > size + 1:
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
        pattern = pattern[1:]
        pattern.append(0)
        for j in range(len(num_array)):
            pattern_pos = int(pattern[j])
            temp_result += pattern_pos * int(num_array[j])
        result.append(abs(temp_result) % 10)

    return result

def get_string_from_num(array):
    return ''.join(map(str, array))

def challenge(input):
    result = input
    for i in range(100):
        temp = get_phase(result)
        result = get_string_from_num(temp)
        print(f'Phase {i}')

    return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #global input
    #test1 = 69317163492948606335995924319873

    #print(challenge(test1))

    with open(DIR / 'input.txt') as f:
       input = f.read().split("\n")[0]
    print(input)
    print(challenge(input))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
