
FILE_NAME = "input.txt"

def read_file(filename: str) -> str:
    with open(filename, 'r') as fp:
        return fp.read()

def part_one(cont: str) -> int:
    elves = cont.strip().split("\n\n")
    return max(list(map(lambda count: sum(count), list(map(lambda elf: list(map(lambda cal: int(cal), elf.split('\n'))), elves)))))

def part_two(cont: str) -> int:
    return sum(sorted(list(map(lambda count: sum(count), list(map(lambda elf: list(map(lambda cal: int(cal), elf.split('\n'))),cont.strip().split("\n\n"))))))[-3:])


def main():
    cont = read_file(FILE_NAME)
    print(f"Day 1:\n\tPart 1: {part_one(cont)}\n\tPart 2: {part_two(cont)}")

if __name__ == "__main__":
    main()