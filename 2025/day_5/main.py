testfile = './inputs/real.txt'

class Range():
    low: int
    high: int

    def __init__(self, low: int, high: int):
        self.low, self.high = low, high

    def __lt__(self, other):
        return self.low < other.low

    def __str__(self):
        return f"{self.low}-{self.high}"

    def __repr__(self):
        return self.__str__()

def combine_ranges(ranges: list[Range]) -> list[Range]:
    ranges.sort()
    disjoint_ranges = []
    for i in range(len(ranges)):
        if len(disjoint_ranges) > 0:
            if disjoint_ranges[-1].high >= ranges[i].low:
                disjoint_ranges[-1].high = max(disjoint_ranges[-1].high, ranges[i].high)
                continue
        disjoint_ranges.append(ranges[i])

    return disjoint_ranges

def is_fresh(ingredient_id: int, ranges: list[Range]) -> bool:
    low = 0
    high = len(ranges)-1
    while low <= high:
        curr_idx = (low + high) // 2
        rang = ranges[curr_idx]
        if ingredient_id >= rang.low and ingredient_id <= rang.high:
            return True
        elif ingredient_id < rang.low:
            high = curr_idx - 1
        else:
            low = curr_idx + 1

    return False

with open(testfile, 'r') as file:
    ranges, fresh_ingredients = [], []
    parsing_ranges = True
    for line in file.readlines():
        if line == '\n':
            parsing_ranges = False
            ranges = combine_ranges(ranges)
            continue
        if parsing_ranges:
            split_line = line.split('-')
            ranges.append(Range(int(split_line[0]), int(split_line[1])))
            continue
        ingredient_id = int(line.strip('\n'))
        if is_fresh(ingredient_id, ranges):
            fresh_ingredients.append(ingredient_id)
    print("Ranges:", ranges)
    print("Fresh ingredients:", fresh_ingredients)
    print("Number of fresh ingredients:", len(fresh_ingredients))
    total_num_fresh_ingredients = 0
    for rang in ranges:
        total_num_fresh_ingredients += rang.high - rang.low + 1
    print("Number of fresh ingredient IDs:", total_num_fresh_ingredients)

