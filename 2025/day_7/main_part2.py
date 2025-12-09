from typing import Tuple
testfile = './inputs/real.txt'

class Manifold():
    manifold: list[list[int]]
    tick_pos: int
    num_timelines_at_pos: dict[Tuple[int, int], int]

    def __init__(self, file_lines: list[str]):
        self.manifold = [['.S^'.index(c) for c in line.strip()] for line in file_lines]
        self.tick_pos = 1
        self.num_timelines_at_pos = {}

    # Ticks the beam forward. Returns number of splits from tick and false if beam cannot
    # be ticked any more.
    def beam_tick(self) -> Tuple[int, bool]:
        if self.tick_pos == len(self.manifold):
            return (0, False)

        num_splits = 0
        previous_line = self.manifold[self.tick_pos-1]
        for i, char in enumerate(self.manifold[self.tick_pos]):
            if previous_line[i] == 1: # 'S' or '|'
                if char == 2: # '^'
                    num_splits += 1
                    self.manifold[self.tick_pos][i-1] = 1
                    self.manifold[self.tick_pos][i+1] = 1
                else:
                    self.manifold[self.tick_pos][i] = 1

        self.tick_pos += 1
        return (num_splits, True)

    def find_num_timelines(self) -> int:
        start_pos = self.manifold[0].index(1)
        return self.find_num_timelines_at_pos(0, start_pos)

    def find_num_timelines_at_pos(self, i: int, j: int) -> int:
        if i == len(self.manifold)-1:
            return 1

        try:
            return self.num_timelines_at_pos[(i, j)]
        except KeyError:
            pass

        next_line = self.manifold[i+1]
        if next_line[j] == 2:
            result = self.find_num_timelines_at_pos(i+1, j-1) + self.find_num_timelines_at_pos(i+1, j+1) 
            self.num_timelines_at_pos[(i, j)] = result
            return result
        result = self.find_num_timelines_at_pos(i+1, j) 
        self.num_timelines_at_pos[(i, j)] = result
        return result

    def __str__(self) -> str:
        return '\n'.join(''.join('.|^'[cell] for cell in row) for row in self.manifold)


with open(testfile, 'r') as file:
    manifold = Manifold(file.readlines())
    print(manifold, '\n')
    total_num_ticks = 0
    while True:
        num_ticks, should_continue = manifold.beam_tick()

        total_num_ticks += num_ticks
        if not should_continue: 
            break

        print(manifold, '\n')

    print('Total number of ticks was', total_num_ticks)
    print('Number of timelines was', manifold.find_num_timelines())
