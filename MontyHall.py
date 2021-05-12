import random


def run(switch_doors, doors_amount=3):
    doors = [False for _ in range(doors_amount)]
    doors[random.randint(0, len(doors) - 1)] = True
    chosen = random.randint(0, len(doors) - 1)

    if switch_doors and len(doors) > 2:
        switched = False
        while not switched:
            pick = random.randint(0, len(doors) - 1)
            if chosen != pick and not doors[pick]:
                switched, new_pick = True, False
                while not new_pick:
                    new_chosen = random.randint(0, len(doors) - 1)
                    if new_chosen != pick and new_chosen != chosen:
                        new_pick = True
                        chosen = new_chosen

    return doors[chosen]


def monty_hall(runs, switch_doors, doors=3):
    wins = 0
    for i in range(runs):
        if run(switch_doors, doors):
            wins += 1
    return wins


if __name__ == '__main__':
    doors, runs = 3, 10000
    wins_without_switch = monty_hall(runs, False, doors)
    wins_with_switch = monty_hall(runs, True, doors)

    print(f'Monty Hall Problem with {doors} doors')
    print(f'Percentage of wins without switching: {(wins_without_switch / runs) * 100:.3f}%')
    print(f'Percentage of wins with switching: {(wins_with_switch / runs) * 100:.3f}%')
