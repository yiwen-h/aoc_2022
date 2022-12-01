# Calorie Counting
from load_data import get_data

raw_data = get_data(1)

def count_calories(data):
    split_data = data.split('\n\n')
    new_list = []
    for i in split_data:
        cals = i.split('\n')
        new_list.append([int(x) for x in cals if x != ''])
    totals = [sum(each) for each in new_list]
    return max(totals)


# with open("test01.txt") as file:
#     test_data = file.read()
#     print(count_calories(test_data))

print(f'part 1 solution = {count_calories(raw_data)}')

def count_calories_2(data):
    split_data = data.split('\n\n')
    new_list = []
    for i in split_data:
        cals = i.split('\n')
        new_list.append([int(x) for x in cals if x != ''])
    totals = [sum(each) for each in new_list]
    totals_sorted = sorted(totals, reverse=True)
    top_3 = sum(totals_sorted[:3])
    return top_3

print(f'part 2 solution = {count_calories_2(raw_data)}')
