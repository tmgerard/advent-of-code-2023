from queue import Queue

def parse_line(line: str) -> (list, list):
    win_num_start = line.find(":")
    win_num_end = line.find("|")

    winning_numbers = line[win_num_start: win_num_end].split()
    numbers = line[win_num_end:].split()

    return winning_numbers, numbers


def check_winning_numbers(winning_numbers: list, numbers: list) -> int:
    count = 0
    for num in winning_numbers:
        if num in numbers:
            count += 1
    
    if count > 0:
        score = 1
        for x in range(count - 1):
            score *= 2
        return score
    else:
        return 0


def build_card_queue(input: str) -> Queue:
    cards = Queue()
    with open("day 4/day_4_input.txt") as file:
        for line in file:
            winning_numbers, numbers = parse_line(line)
            cards.put([winning_numbers, numbers])
    return cards


def get_total_cards():
    pass


if __name__ == "__main__":

    # part one - tally points
    score = 0
    with open("day 4/day_4_input.txt") as file:
        for line in file:
            winning_numbers, numbers = parse_line(line)
            score += check_winning_numbers(winning_numbers, numbers)

    print(f'Total Score = {score}')
