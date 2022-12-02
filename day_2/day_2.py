FILE_NAME = "input.txt"

WIN = 6
DRAW = 3
LOSS = 0

ROCK = 1
PAPER = 2
SCISSORS = 3

game_scores_1 = {
    'A X': DRAW + ROCK,
    'A Y': WIN + PAPER,
    'A Z': LOSS + SCISSORS,
    'B X': LOSS + ROCK,
    'B Y': DRAW + PAPER,
    'B Z': WIN + SCISSORS,
    'C X': WIN + ROCK,
    'C Y': LOSS + PAPER,
    'C Z': DRAW + SCISSORS,
}

game_scores_2 = {
    'A X': LOSS + SCISSORS,
    'A Y': DRAW + ROCK,
    'A Z': WIN + PAPER,
    'B X': LOSS + ROCK,
    'B Y': DRAW + PAPER,
    'B Z': WIN + SCISSORS,
    'C X': LOSS + PAPER,
    'C Y': DRAW + SCISSORS,
    'C Z': WIN + ROCK,
}

def open_file(file: str) -> str:
    with open(file, 'r') as f:
        return f.read().strip().split('\n')

def challenge_1(cont: str) -> int:
    return sum(list(map(lambda game: game_scores_1[game], cont)))

def challenge_2(cont: str) -> int:
    return sum(list(map(lambda game: game_scores_2[game], cont)))

def main():
    cont = open_file(FILE_NAME)
    print(f"Day 2:\n\tChallenge 1:\t{challenge_1(cont)}\n\tChallenge_2:\t{challenge_2(cont)}")

if __name__ == "__main__":
    main()