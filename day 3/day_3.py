import re


def get_input_list(input: str) -> list:
    input_list = []
    with open(input) as file:
        for line in file:
            input_list.append(line)
    return input_list


def find_all_numbers(input_str: str) -> list:
    return re.findall(r'\d+', input_str)


def find_part_numbers(lines: list, numbers: list) -> list:
    part_nos = []

    for line in range(len(lines)):
        for num in numbers[line]:
            index = lines[line].find(num)
            if num_is_part(lines, num, index, line):
                part_nos.append(float(num))

    return part_nos


def num_is_part(lines: list, number: str, num_index: int, current_row: int) -> bool:
    IGNORE = '.'

    is_top_row = current_row == 0
    is_bot_row = current_row == len(lines)
    is_left_col = num_index == 0
    is_right_col = num_index == len(lines[0])

    symbol_found = False

    high_index = num_index + len(number) - 1
        

    return False

if __name__ == "__main__":
    lines = get_input_list('day 3/day_3_input.txt')

    possible_part_nos = []
    for line in lines:
        possible_part_nos.append(find_all_numbers(line))
    
    part_nos = find_part_numbers(lines, possible_part_nos)
                    
    print(f'sum = ?')
