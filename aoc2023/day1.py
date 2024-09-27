# day 1: trebuchet?!

import re

def part1():
    input_path = 'input1.txt'
    with open(input_path) as file:
        lines = [line.rstrip() for line in file]

    print(lines)

    number_list = []
    for line in lines:
        number = re.findall('\d+', line)[0]

        if len(number) == 1:
            number = int(str(number) + str(number))
        if len(str(number)) > 2:
            number = int(str(number[0]) + str(number[-1]))

        number_list.append(int(number))

    print(f'the sum of the number_list is {sum(number_list)}')

if __name__ == '__main__':
    part1()
