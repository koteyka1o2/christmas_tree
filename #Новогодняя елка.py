import random
from colorama import init, Fore, Style
import time
import os

init(autoreset=True)

color_list = [
    Fore.RED + "*" + Style.RESET_ALL,
    Fore.GREEN + "*" + Style.RESET_ALL,
    Fore.BLUE + "*" + Style.RESET_ALL,
    Fore.YELLOW + "*" + Style.RESET_ALL
]

Tree = [
    "     *     ",
    "    ***    ",
    "   *****   ",
    "  *******  ",
    " ********* ",
    "***********",
    "    |||    "
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    tree = [list(line) for line in Tree]

    positions = []
    for i, line in enumerate(tree):
        for j, ch in enumerate(line):
            if ch == '*':
                positions.append((i, j))

    k = random.randint(1, len(positions))
    chosen = random.sample(positions, k)

    for i, j in positions:
        tree[i][j] = random.choice(color_list) if (i, j) in chosen else "*"

    clear_console()
    for line in tree:
        print("".join(line))
    time.sleep(0.6)
#Новогодняя елка by koteyka1o2