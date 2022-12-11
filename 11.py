# Monkey in the Middle
from load_data import get_data
import numpy as np

class Monkey:
    def __init__(self, id, items, operation, test, iftrue, iffalse):
        self.id = id
        self.items = items
        self.operation = operation

        self.test = test
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.inspections = 0

    def op(self, item):
        self.inspections += 1
        if self.operation[1] == 'old':
            num = item
        else:
            num = int(self.operation[1])
        if self.operation[0] == '*':
            return item * num
        elif self.operation[0] == '+':
            return item + num

    def new_worry(self):
        new_values = []
        for i in range(len(self.items)):
            val = self.op(self.items[i])
            val = int(val / 3)
            new_values.append(val)
        self.items = new_values

    def tst(self, worry):
        if worry % self.test == 0:
            return True
        else:
            return False


def mim(data):
    monkeydata = [m.split('\n') for m in data.split('\n\n')]
    monkeys = []
    for i in range(len(monkeydata)):
        items = [int(x.strip()) for x in monkeydata[i][1].split(':')[1].split(',')]
        operation = monkeydata[i][2].split(':')[1].split()[-2:]
        test = int(monkeydata[i][3].split(':')[1].split()[-1])
        iftrue = int(monkeydata[i][4].split()[-1])
        iffalse = int(monkeydata[i][5].split()[-1])
        monkeys.append(Monkey(i, items, operation, test, iftrue, iffalse))
    for i in range(20):
        for m in range(len(monkeys)):
            if len(monkeys[m].items) != 0:
                monkeys[m].new_worry()
                t = []
                f = []
                for each in monkeys[m].items:
                    if monkeys[m].tst(each) == True:
                        t.append(each)
                    else:
                        f.append(each)
                monkeys[monkeys[m].iftrue].items.extend(t)
                monkeys[monkeys[m].iffalse].items.extend(f)
                monkeys[m].items = []
    inspections = [m.inspections for m in monkeys]
    return sorted(inspections)[-1] * sorted(inspections)[-2]


def mim_2(data):
    pass

with open("test_data/test11.txt") as file:
     test_data = file.read()
     print(mim(test_data))

raw_data = get_data(11)

print(f'part 1 solution = {mim(raw_data)}')

# with open("test_data/test11.txt") as file:
#     test_data = file.read()
#     print(mim_2(test_data))

# print(f'part 2 solution = {mim_2(raw_data)}')
