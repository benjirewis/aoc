testfile = './inputs/input.txt'

with open(testfile, 'r') as file:
    clicks_to_point_at_zero = 0
    lands_on_zero = 0

    curr_pos = 50 # start at 50

    for line in file:
        new_pos = 0

        if line[0] == 'L': # L is "negative"
            new_pos = curr_pos - int(line[1:])
            # If we've gone "negative" and we're not _at_ zero (already counted),
            # increment clicks.
            if new_pos < 0 and curr_pos != 0:
                clicks_to_point_at_zero += 1
        elif line[0] == 'R': # R is "positive"
            new_pos = curr_pos + int(line[1:])
        else:
            raise BaseException('unknown movement')

        # Increment clicks by number of times we can spin by 101.
        spin_inc = abs(new_pos) // 101
        if spin_inc > 0:
            clicks_to_point_at_zero += spin_inc

        # Mod new_pos by 100 to get a valid position.
        new_pos %= 100

        # If we've gone negative, express that position as a positive (add 100).
        if new_pos < 0:
            new_pos += 100

        # If we've actually hit 0, increment clicks and lands.
        if new_pos == 0:
            clicks_to_point_at_zero += 1
            lands_on_zero += 1

        # Set curr_pos.
        curr_pos = new_pos

print('Part 1:', lands_on_zero)
print('Part 2:', clicks_to_point_at_zero)
