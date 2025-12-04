from typing import Tuple

testfile = './inputs/real.txt'

def find_battery(bank: str, battery_num: int, stop_index: int) -> Tuple[str, int]:
    next_battery = "0"
    next_stop_index = 0

    # Range backwards in batteries from battery_num batteries to the left up until
    # stop_index. The battery cannot be before battery_num indices to the left, e.g. the
    # 3rd battery cannot be in the 2nd to left spot. The battery can also not be any
    # further left than the stop_index (where the last battery was found).
    for i in range(len(bank)-battery_num,stop_index,-1):
        battery = bank[i]
        # An equivalence is preferable as it's farther to the left.
        if int(battery) >= int(next_battery):
            next_battery = battery
            next_stop_index = i

    return next_battery, next_stop_index

def find_highest_joltage(bank: str) -> int:
    if len(bank) < 2:
        raise BaseException('bank too small')

    joltage_batteries = ""
    stop_index = -1
    for battery_num in range(12,0,-1):
        joltage_battery, stop_index = find_battery(bank, battery_num, stop_index)
        joltage_batteries += joltage_battery

    return int(joltage_batteries)

with open(testfile, 'r') as file:
    joltages = [find_highest_joltage(line.strip()) for line in file]
    print('Joltages are:', joltages)
    print('Sum of joltages is:', sum(joltages))
