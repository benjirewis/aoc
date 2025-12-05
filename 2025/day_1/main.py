testfile = './inputs/test.txt'

with open(testfile, 'r') as file:
    clicks_past_zero, lands_on_zero = 0, 0
    curr_pos = 50

    for line in file:
        new_pos = 0
        if line[0] == 'L':
            new_pos = curr_pos - int(line[1:])
        else:
            new_pos = curr_pos + int(line[1:])

        spins = abs(int(new_pos / 100))
        if spins > 0:
            clicks_past_zero += spins
        elif new_pos % 100 == 0:
            clicks_past_zero += 1
            lands_on_zero += 1
        if new_pos < 0 and curr_pos > 0:
            clicks_past_zero += 1

        new_pos %= 100
        if new_pos < 0:
            new_pos += 100

        curr_pos = new_pos

print('Part 1:', lands_on_zero)
print('Part 2:', clicks_past_zero)
