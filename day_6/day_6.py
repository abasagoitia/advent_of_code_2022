
def read_file(filename: str) -> str:
    with open(filename, 'r') as fp:
        return fp.read().strip()

def parse_contents_one(contents: str) -> list[str]:
    return contents.split('\n')

def part_one(parsed: list[str]) -> int:
    count = 0

    for line in parsed:
        for idx in range(5, len(line)):
            if len(set(line[idx-4: idx])) == 4:
                count += idx
                break

    return count

def part_two(parsed: list[str]) -> int:
    count = 0

    for line in parsed:
        for idx in range(15, len(line)):
            if len(set(line[idx-14: idx])) == 14:
                count += idx
                break

    return count

def main():
    filename = "input.txt"
    contents = read_file(filename)

    print(f"Day 6:\n\tPart 1: {part_one(parse_contents_one(contents))}\n\tPart 2: {part_two(parse_contents_one(contents))}")

if __name__ == "__main__":
    main()