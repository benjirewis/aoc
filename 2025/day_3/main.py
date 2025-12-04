testfile = './inputs/real.txt'

def find_highest_joltage(bank: str) -> int:
    print(bank)
    if len(bank) < 2:
        raise BaseException('bank too small')

    left = "0"
    right = "0"

    # Range backwards in batteries twice. First to find left digit, second to find right
    # digit.
    left_index = 0
    for i in range(len(bank)-1,-1,-1):
        # Left digit cannot be farthest to the right.
        if i == len(bank)-1:
            continue

        battery = bank[i]
        # An equivalence is preferable as it's farther to the left.
        if int(battery) >= int(left):
            left = battery
            left_index = i

    # Stop right digit loop once we reach left digit.
    for i in range(len(bank)-1,left_index,-1):
        battery = bank[i]
        print('Looking for right', battery)
        if int(battery) > int(right):
            print('Setting for right', battery)
            right = battery

    return int(left+right)

with open(testfile, 'r') as file:
    joltages = [find_highest_joltage(line.strip()) for line in file]
    print('Joltages are:', joltages)
    print('Sum of joltages is:', sum(joltages))
