# Cathode-Ray Tube
from load_data import get_data

def crt(data):
    instructions = data.split('\n')[:-1]
    X = 1
    cyclecount = 0
    signal = {}
    for line in instructions:
        if line.split()[0] == 'addx':
            for i in range(2):
                cyclecount += 1
                if cyclecount in [20,60,100,140,180,220]:
                    signal[cyclecount] = X
            X += int(line.split()[-1])
        if line.split()[0] == 'noop':
            cyclecount += 1
            if cyclecount in [20,60,100,140,180,220]:
                    signal[cyclecount] = X
    total = 0
    for k,v in signal.items():
        total += k * v
    return total

def crt_2(data):
    instructions = data.split('\n')[:-1]
    X = 1
    cyclecount = 0
    signal = {}
    sprite = {}
    for line in instructions:
        if line.split()[0] == 'addx':
            for i in range(2):
                cyclecount += 1
                signal[cyclecount] = X
                sprite[cyclecount] = [X-1, X, X+1]
            X += int(line.split()[-1])
        if line.split()[0] == 'noop':
            cyclecount += 1
            signal[cyclecount] = X
            sprite[cyclecount] = [X-1, X, X+1]
    lines = []
    for row in range(6):
        line = []
        for i in range(40):
            if i in sprite[i+1 + 40*row]:
                line.append('#')
            else:
                line.append('.')
        lines.append(line)
    with open('10_answer.txt', 'w') as f:
        for each in lines:
            f.write(''.join(each))
            f.write('\n')
    return lines

# with open("test_data/test10.txt") as file:
#      test_data = file.read()
#      print(crt(test_data))

raw_data = get_data(10)

# print(f'part 1 solution = {crt(raw_data)}')

with open("test_data/test10.txt") as file:
    test_data = file.read()
    print(crt_2(test_data))

print(f'part 2 solution = {crt_2(raw_data)}')
