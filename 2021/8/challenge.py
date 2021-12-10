from numpy import number, sign


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
    data = [i.split("|") for i in input]

    instances = 0
    for _, output in data:
        for digits in output.split(" "):
            if len(digits) in (2,4,3,7):
                instances += 1

    return instances

def part_2(input):
    result_sum = 0
    for line in input:
        signal, output = map(str.strip, line.split("|"))
        
        signal = ["".join(sorted(t)) for t in signal.split()]
        output = ["".join(sorted(t)) for t in output.split()]

        letter_dictionary = dict()
        number_dictionary = dict()

        for i in range(len(signal)):
            if len(signal[i]) == 2:
                letter_dictionary[1] = signal[i]
                number_dictionary[signal[i]] = 1
            elif len(signal[i]) == 3:
                letter_dictionary[7] = signal[i]
                number_dictionary[signal[i]] = 7
            elif len(signal[i]) == 4:
                letter_dictionary[4] = signal[i]
                number_dictionary[signal[i]] = 4
            elif len(signal[i]) == 7:
                letter_dictionary[8] = signal[i]
                number_dictionary[signal[i]] = 8
        
        diff1_4 = "".join(set(letter_dictionary[1]).symmetric_difference(set(letter_dictionary[4])))

        for i in range(len(signal)):
            if len(signal[i]) == 6:
                if all(map(signal[i].__contains__, diff1_4)):
                    if all(map(signal[i].__contains__, letter_dictionary[7])):
                        letter_dictionary[9] = signal[i]
                        number_dictionary[signal[i]] = 9
                    else:
                        letter_dictionary[6] = signal[i]
                        number_dictionary[signal[i]] = 6
                else:
                    letter_dictionary[0] = signal[i]
                    number_dictionary[signal[i]] = 0
            elif len(signal[i]) == 5:
                if all(map(signal[i].__contains__, letter_dictionary[1])):
                    letter_dictionary[3] = signal[i]
                    number_dictionary[signal[i]] = 3
                elif all(map(signal[i].__contains__, diff1_4)):
                    number_dictionary[signal[i]] = 5
                else:
                    number_dictionary[signal[i]] = 2
                
        result = [""] * 4
        for i in range(len(output)):
            result[i] = str(number_dictionary[output[i]])

        result_sum += int(''.join(result))
    return result_sum

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