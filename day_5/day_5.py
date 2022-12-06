import re
FILENAME = "input.txt"
TESTNAME = "test.txt"

class Table:
    def __init__(self, table:str, instrs:str) -> None:
        self.table = self.parse_table(table)
        self.instrs = self.parse_instrs(instrs)

    def parse_table(self, table:str) -> dict:
        parsed_table = {}
        num_cols = len((table.split('\n')[-1]).replace(' ',''))
        for idx in range(1, num_cols + 1):
            parsed_table[idx] = []
        lines = table.split('\n')

        for line in range(0, len(lines) - 1):
            for col in range(1, len(lines[-1]), 4):
                if lines[line][col].isalpha():
                    parsed_table[int(lines[-1][col])].append(lines[line][col])
        
        for key in parsed_table:
            parsed_table.update({key: list(reversed(parsed_table[key]))})
        return parsed_table

    def parse_instrs(self, instrs:str):
        parsed_instrs = []
        for instr in instrs.split('\n'):
            parsed_instrs.append(list(map(lambda x: int(x), re.split("move | from | to ", instr)[1:])))
        return parsed_instrs[:len(parsed_instrs)-1]

def read_file(filename:str) -> str:
    with open(filename, 'r') as fp:
        return fp.read()

def build_table(cont:str):
    table, instrs = cont.split("\n\n")
    return Table(table, instrs)

def part_1(cont:str):
    table = build_table(cont)

    for inst in table.instrs:
        from_col = table.table[inst[1]]
        to_move = from_col[len(from_col) - inst[0]:]
        table.table[inst[1]] = from_col[:len(from_col) - inst[0]]
        table.table[inst[2]].extend(list(reversed(to_move)))
    
    ret_str = ''
    for k,v in table.table.items():
        ret_str += v[-1]
    
    return ret_str


def part_2(cont:str):
    table = build_table(cont)

    for inst in table.instrs:
        from_col = table.table[inst[1]]
        to_move = from_col[len(from_col) - inst[0]:]
        table.table[inst[1]] = from_col[:len(from_col) - inst[0]]
        table.table[inst[2]].extend(to_move)
    
    ret_str = ''
    for k,v in table.table.items():
        ret_str += v[-1]
    
    return ret_str

def main():
    cont = read_file(FILENAME)
    print(f"Day 5:\n\tPart 1:\t{part_1(cont)}\n\tPart 2:\t{part_2(cont)}")

if __name__ == "__main__":
    main()