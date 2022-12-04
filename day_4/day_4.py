FILENAME = "input.txt"
TESTNAME = "test.txt"

class Assignment:
    def __init__(self, start, finish):
        self.start = int(start)
        self.finish = int(finish)
        self.full = True

    def __str__(self):
        return f"{self.start}-{self.finish}"

    def __contains__(self, other):
        if self.full:
            if (self.start <= other.start and other.finish <= self.finish):
                return True
            return False
        else:
            if (self.start in range(other.start, other.finish+1) or self.finish in range(other.start, other.finish+1)):
                return True
            return False


class Pair:
    def __init__(self, elf_0, elf_1):
        self.elf_0 = elf_0
        self.elf_1 = elf_1

    def __str__(self):
        return f"{self.elf_0}\n{self.elf_1}"

    def check_full_overlap(self):
        if self.elf_0 in self.elf_1 or self.elf_1 in self.elf_0:
            return True
        return False

    def check_partial_overlap(self):
        self.elf_0.full = False
        self.elf_1.full = False
        if self.elf_0 in self.elf_1 or self.elf_1 in self.elf_0:
            return True
        return False

def read_file(filename: str) -> str:
    with open(filename, 'r') as fp:
        return fp.read().strip()

def get_pairs(cont:str):
    cont = list(map(lambda elf: list(map(lambda x: x.split('-'), elf.split(','))), cont.split('\n')))
    pairs = []
    for pair in cont:
        elf_0 = Assignment(pair[0][0], pair[0][1])
        elf_1 = Assignment(pair[1][0], pair[1][1])
        pairs.append(Pair(elf_0, elf_1))
    
    return pairs


def part_one(cont: str) -> int:
    pairs = get_pairs(cont)
    
    ctr = 0
    for pair in pairs:
        if pair.check_full_overlap():
            ctr +=1
    return ctr

def part_two(cont: str) -> int:
    pairs = get_pairs(cont)

    ctr = 0
    for pair in pairs:
        if pair.check_partial_overlap():
            ctr +=1
    return ctr

def main():
    cont = read_file(FILENAME)
    print(f"Day 4:\n\tPart 1:\t{part_one(cont)}\n\tPart 2:\t{part_two(cont)}")

if __name__ == "__main__":
    main()