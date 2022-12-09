TO_FREE = 3441553
PART_ONE = 0
POSS = []

class Directory:
    def __init__(self, name:str, dirs: list, files: list, parent):
        self.name = name
        self.dirs = dirs
        self.files = files
        self.parent = parent
        self.size = 0
        self.tot_size = 0

    def calc_size(self, part_one: False) -> int:
        global PART_ONE, POSS
        if self.dirs == []:
            self.size = 0
        
        else:
            for d in self.dirs:
                self.size += d.calc_size(part_one)

        for fi in self.files:
            self.size += fi.size

        if self.size <= 100000 and part_one:
            PART_ONE += self.size

        if self.size >= TO_FREE and not part_one:
            print(f"Size: {self.size}\nfree: {TO_FREE}")
            POSS.append(self)
        
        return self.size

class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    

def get_root(parsed):
    root = Directory('/', [], [], None)
    cur_dir = root

    for cmd in parsed:
        if cmd[0] == 'dir':
            cur_dir.dirs.append(Directory(cmd[1], [], [], cur_dir))
            continue

        if cmd[0].isdigit():
            cur_dir.files.append(File(cmd[1], int(cmd[0])))
            # cur_dir.size += int(cmd[0])
            continue

        if cmd[0] == '$':
            if cmd[1] == "cd":
                if cmd[2] == '/':
                    cur_dir = root
                    continue
                
                if cmd[2] == "..":
                    cur_dir = cur_dir.parent
                    continue

                for d in cur_dir.dirs:
                    if d.name == cmd[2]:
                        cur_dir = d
                        break
                
            

            if cmd[1] == "ls":
                continue

    return root

def read_file(filename: str) -> str:
    with open(filename, 'r') as fp:
        return fp.read().strip()

def parse_contents_one(contents: str) -> list[str]:
    return list(map(lambda x: x.split(' '), contents.split('\n')))

def part_one(parsed: list[str]) -> int:
    root = get_root(parsed)
    root.calc_size(True)
    return PART_ONE
    

def part_two(parsed: list[str]) -> int:
    global TO_FREE
    max_size = 70000000
    needed_sz = 30000000
    root = get_root(parsed)
    to_free = needed_sz + root.calc_size(False) - max_size
    TO_FREE = to_free
    print(f"Need to free: {TO_FREE}")
    
    return sorted(POSS, key=lambda x: x.size)[0].size


def main():
    filename = "input.txt"
    contents = read_file(filename)

    print(f"Day 7:\n\tPart 1: {part_one(parse_contents_one(contents))}\n\tPart 2: {part_two(parse_contents_one(contents))}")

if __name__ == "__main__":
    main()