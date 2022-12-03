FILENAME = "input.txt"
TESTNAME = "test.txt"

value_lookup = {}

def create_lookup_dict():
    for i in range(0, 26):
        value_lookup[chr(ord('a') + i)] = i + 1

    for i in range(0, 26):
        value_lookup[chr(ord('A') + i )] = 27 + i

def open_file(file: str) -> str:
    with open(file, 'r') as fp:
        return fp.read().strip()

def get_pockets(cont: str) -> list:
    return list(map(lambda pocket: [pocket[:len(pocket) // 2], pocket[len(pocket) // 2:]],cont.split('\n')))

def get_shared_items(rucks: list) -> list:
    shared_items = []
    for ruck in rucks:
        shared_items.append(''.join(set(ruck[0]) & set(ruck[1])))
    return shared_items

def get_badges(teams: list) -> list:
    badges = []
    for team in teams:
        badges.append(''.join(set(team[0]) & set(team[1]) & set(team[2])))
    return badges


def part_1(cont: str) -> int:
    rucks = get_pockets(cont)
    return sum(list(map(lambda item: value_lookup[item], get_shared_items(rucks))))


def part_2(cont: str) -> int:
    rucks = cont.split('\n')
    teams = [rucks[i:i + 3] for i in range(0, len(rucks), 3)]
    return sum(list(map(lambda badge: value_lookup[badge], get_badges(teams))))
    

def main():
    cont = open_file(FILENAME)
    #cont = open_file(TESTNAME)
    create_lookup_dict()
    print(f"Day 3:\n\tPart 1:\t{part_1(cont)}\n\tPart 2:\t{part_2(cont)}")


if __name__ == "__main__":
    main()