testfile = './inputs/test.txt'

with open(testfile, 'r') as file:
    clicks_to_point_at_zero = 0
    lands_on_zero = 0

    curr_pos = 50 # start at 50

    for line in file:
        new_pos = 0

        passed = False
        if line[0] == 'L': # L is "negative"
            new_pos = curr_pos - int(line[1:])
            # If we've gone "negative" from positive, increment clicks.
            if new_pos < 0 and curr_pos > 0:
                clicks_to_point_at_zero += 1
                passed = True
        elif line[0] == 'R': # R is "positive"
            new_pos = curr_pos + int(line[1:])
        else:
            raise BaseException('unknown movement')

        # Increment clicks by number of times we can spin by 100.
        spin_inc = int(abs(new_pos) / 100)
        if spin_inc > 0:
            clicks_to_point_at_zero += spin_inc
            # Do not double count the movement from negative to positive above.
            if passed:
                clicks_to_point_at_zero -= 1


        # Mod new_pos by 100 and potentially increment to get a valid dial position.
        new_pos %= 100
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
