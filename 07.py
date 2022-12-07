# No space left on device
from load_data import get_data

raw_data = get_data(7)

def spacecheck(data):
    data_split = data.split('\n')[:-1]
    # get lines relevant to each dir and store dirnames
    dirs = {}
    dirname = ''
    for i in range(len(data_split)):
        if data_split[i].startswith('$ cd '):
            if data_split[i][5:] == '..':
                dirname = '-'.join(dirname.split('-')[:-1])
            else:
                dirname = dirname + '-' + data_split[i][5:]
                dirs.setdefault(dirname, [i])
    dir_keys = list(dirs.keys())
    for each in range(1,len(dir_keys)):
         dirs[dir_keys[each-1]].append(dirs[dir_keys[each]][0] -1)
    dirs[dir_keys[-1]].append(len(data_split)-1)
    # get actual dir contents
    dir_contents = {}
    for each in dirs:
        contents = []
        for i in range(dirs[each][0], dirs[each][1] +1):
            line_value = data_split[i]
            if line_value.split()[0].isnumeric():
                contents.append(int(line_value.split()[0]))
            if line_value.split()[0] == 'dir':
                contents.append(f'{each}-{line_value.split()[1]}')
        dir_contents[each] = contents
    # get vals
    for dir in dir_contents:
        while all(isinstance(x, int) for x in dir_contents[dir]) != True:
            for content in dir_contents[dir]:
                if isinstance(content, str):
                    dir_contents[dir].remove(content)
                    dir_contents[dir] += dir_contents[content]
        dir_contents[dir] = sum(dir_contents[dir])
    total = 0
    for val in dir_contents.values():
        if val < 100000:
            total += val
    return total


with open("test_data/test07.txt") as file:
    test_data = file.read()
    print(spacecheck(test_data))

print(f'part 1 solution = {spacecheck(raw_data)}')


def spacecheck_2(data):
    data_split = data.split('\n')[:-1]
    # get lines relevant to each dir and store dirnames
    dirs = {}
    dirname = ''
    for i in range(len(data_split)):
        if data_split[i].startswith('$ cd '):
            if data_split[i][5:] == '..':
                dirname = '-'.join(dirname.split('-')[:-1])
            else:
                dirname = dirname + '-' + data_split[i][5:]
                dirs.setdefault(dirname, [i])
    dir_keys = list(dirs.keys())
    for each in range(1,len(dir_keys)):
         dirs[dir_keys[each-1]].append(dirs[dir_keys[each]][0] -1)
    dirs[dir_keys[-1]].append(len(data_split)-1)
    # get actual dir contents
    dir_contents = {}
    for each in dirs:
        contents = []
        for i in range(dirs[each][0], dirs[each][1] +1):
            line_value = data_split[i]
            if line_value.split()[0].isnumeric():
                contents.append(int(line_value.split()[0]))
            if line_value.split()[0] == 'dir':
                contents.append(f'{each}-{line_value.split()[1]}')
        dir_contents[each] = contents
    # get vals
    for dir in dir_contents:
        while all(isinstance(x, int) for x in dir_contents[dir]) != True:
            for content in dir_contents[dir]:
                if isinstance(content, str):
                    dir_contents[dir].remove(content)
                    dir_contents[dir] += dir_contents[content]
        dir_contents[dir] = sum(dir_contents[dir])
    currentspace = dir_contents[list(dir_contents.keys())[0]]
    available = 70000000 - currentspace
    needed = 30000000 - available
    possibles = []
    for val in dir_contents.values():
        if val > needed:
            possibles.append(val)
    return min(possibles)


with open("test_data/test07.txt") as file:
    test_data = file.read()
    print(spacecheck_2(test_data))

print(f'part 2 solution = {spacecheck_2(raw_data)}')
