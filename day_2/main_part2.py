testfile = './inputs/real.txt'

def is_invalid_id(id: str):
    if len(id) < 2:
        return False

    # Try cheeky halfway.
    halfway = len(id)//2
    if id[0:halfway] == id[halfway:]:
        return True

    # Brute force if not :)
    for i in range(len(id)):
        if i == 0 or len(id) % i != 0:
            continue
        if id[0:i] * (len(id)//i) == id:
            return True

    return False


with open(testfile, 'r') as file:
    invalid_ids = []
    range_strs = []
    for line in file:
        range_strs.extend(line.strip(',\n').split(','))

    ranges = [range_str.split('-') for range_str in range_strs]
    for r in ranges:
        left = int(r[0])
        right = int(r[1])

        while left != right + 1:
            if is_invalid_id(str(left)):
                invalid_ids.append(left)
            left += 1

    print('Invalid IDs are:', invalid_ids)
    print('Sum of invalid IDs is:', sum(invalid_ids))
