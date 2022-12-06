# Tuning Trouble
from load_data import get_data

raw_data = get_data(6)

def tuning(data):
    for i in range(len(data)-4):
        chunk = data[i:i+4]
        if len(set(chunk)) == 4:
            return i+4



# with open("test_data/test06.txt") as file:
#     test_data = file.readlines()
#     for line in test_data:
#         print(tuning(line))

print(f'part 1 solution = {tuning(raw_data)}')

def tuning_2(data):
    for i in range(len(data)-14):
        chunk = data[i:i+14]
        if len(set(chunk)) == 14:
            return i+14

with open("test_data/test06.txt") as file:
    test_data = file.readlines()
    for line in test_data:
        print(tuning_2(line))

print(f'part 2 solution = {tuning_2(raw_data)}')
