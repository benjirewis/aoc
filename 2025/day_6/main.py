from math import prod
testfile = './inputs/test.txt'

with open(testfile, 'r') as file:
    lines = file.readlines()
    columns, results = [], []
    for i, line in enumerate(lines):
        line = line.split()
        if i == len(lines) - 1:
            for j, op_str in enumerate(line):
                op = sum if op_str == '+' else prod
                results.append(op(columns[j]))
            continue
        for j, num_str in enumerate(line):
            if i == 0:
                columns.append([])
            columns[j].append(int(num_str))
           
    print('Columns are:', columns)
    print('Results are:', results)
    print('Sum of results is:', sum(results))
