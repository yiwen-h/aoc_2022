# Camp CLeanup

from load_data import get_data

raw_data = get_data(4)



def cleanup(data):
    split_data = data.split('\n')[:-1]
    count = 0
    for i in split_data:
        pairs = []
        each = i.split(',')
        for e in each:
            combo = e.split('-')
            comboint = [int(x) for x in combo]
            pairs.append(comboint)
        if pairs[0][0] >= pairs[1][0] and pairs[0][-1] <= pairs[1][-1]:
            count += 1
        elif pairs[1][0] >= pairs[0][0] and pairs[1][-1] <= pairs[0][-1]:
            count += 1
    return count


with open("test_data/test04.txt") as file:
    test_data = file.read()
    print(cleanup(test_data))

print(f'part 1 solution = {cleanup(raw_data)}')

def cleanup_2(data):
    split_data = data.split('\n')[:-1]
    count = 0
    for i in split_data:
        pairs = []
        each = i.split(',')
        for e in each:
            combo = e.split('-')
            comboint = [int(x) for x in combo]
            pairs.append(comboint)
        if pairs[0][0] >= pairs[1][0] and pairs[0][0] <= pairs[1][-1]:
            count += 1
        elif pairs[1][0] >= pairs[0][0] and pairs[1][0] <= pairs[0][-1]:
            count += 1
    return count


with open("test_data/test04.txt") as file:
    test_data = file.read()
    print(cleanup_2(test_data))

print(f'part 2 solution = {cleanup_2(raw_data)}')
