"""
--- Day 2: Cube Conundrum ---

You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
"""

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def sum_valid_games(file: str) -> (int, int):

    id_sum = 0
    power_sum = 0
    with open(file, 'r', encoding='utf_8') as file:
        for line in file:
            parsed = parse_line(line)
            id_sum += parsed[0]
            power_sum += parsed[1]
    
    return (id_sum, power_sum)

def parse_line(line: str) -> (int, int):
    """
    Returns value of game id if a valid game or zero if invalid
    """
    red = []
    green = []
    blue = []

    split_text = line.split(":") # ["Game id", game results list ]
    game_id = int(split_text[0].split()[1]) # [ Game, id ]

    valid_game = True
    hands = split_text[1].split(";")

    for hand in hands:
        cubes = hand.split(',')

        for cube in cubes:

            cube_split = cube.split()
            num_cubes = int(cube_split[0])
            color_cubes = cube_split[1].lower()

            if color_cubes == 'red':
                red.append(num_cubes)
            if color_cubes == 'green':
                green.append(num_cubes)
            if color_cubes == 'blue':
                blue.append(num_cubes)
    
    red_max = max(red)
    green_max = max(green)
    blue_max = max(blue)
    
    valid_game = red_max <= MAX_RED and green_max <= MAX_GREEN and blue_max <= MAX_BLUE
    power = red_max * green_max * blue_max

    if valid_game:
        return (game_id, power)
    else:
        return (0, power)


if __name__ == "__main__":
    sums = sum_valid_games("day 2/day_2_input.txt")
    print(f'sum of ids = {sums[0]}')
    print(f'power sum = {sums[1]}')
