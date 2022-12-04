# Rucksack Reorganization

from load_data import get_data

raw_data = get_data(3)

alphanums = [*range(ord('a'), ord('z')+1), *range(ord('A'), ord('Z')+1)]
alphas = [chr(l) for l in alphanums]
vals = [*range(1,53)]
priorities = dict(zip(alphas,vals))


def reorg(data):
    split_data = data.split('\n')[:-1]
    items = []
    for rucksack in split_data:
        half = int(len(rucksack)/2)
        rucksack_1 = rucksack[:half]
        rucksack_2 = rucksack[half:]
        for i in rucksack_1:
            if i in rucksack_2:
                items.append(priorities[i])
                break
    return sum(items)


# with open("test_data/test03.txt") as file:
#     test_data = file.read()
#     print(reorg(test_data))

print(f'part 1 solution = {reorg(raw_data)}')


def reorg_2(data):
    split_data = data.split('\n')[:-1]
    total = 0
    count = 0
    groups = []
    group = []
    for rucksack in split_data:
        count += 1
        items = set(rucksack)
        group += [i for i in items]
        if count == 3:
            groups.append(group)
            count = 0
            group = []
    for each in groups:
        for i in each:
            if each.count(i) == 3:
                total += priorities[i]
                break
    return total

# with open("test_data/test03.txt") as file:
#     test_data = file.read()
#     print(reorg_2(test_data))

print(f'part 2 solution = {reorg_2(raw_data)}')
