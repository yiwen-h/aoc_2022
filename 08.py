# Treetop Tree House
from load_data import get_data
import numpy as np

raw_data = get_data(8)

def treetop(data):
    #make numpy grid of trees
    data_split = data.split('\n')[:-1]
    forest = np.zeros((len(data_split[0]),len(data_split)))
    for line in range(len(data_split)):
        for each in range(len(data_split[0])):
            forest[line][each] = int(data_split[line][each])
    #outer trees are all visible
    tree_count = 2* len(data_split) + 2* (len(data_split)-2)
    #compare each tree not in outer lanes
    for line in range(1,len(data_split)-1):
        for col in range(1,len(data_split)-1):
            #check all above
            if forest[line][col] > forest[:, col][:line].max():
                tree_count += 1
            #check all below
            elif forest[line][col] > forest[:, col][line+1:].max():
                tree_count += 1
            #check to the left
            elif forest[line][col] > forest[line][:col].max():
                tree_count += 1
            #check to the right
            elif forest[line][col] > forest[line][col+1:].max():
                tree_count += 1
    return tree_count


def treetop_2(data):
    #make numpy grid of trees
    data_split = data.split('\n')[:-1]
    forest = np.zeros((len(data_split[0]),len(data_split)))
    for line in range(len(data_split)):
        for each in range(len(data_split[0])):
            forest[line][each] = int(data_split[line][each])
    #compare each tree not in outer lanes
    max_score = 0
    for line in range(1,len(data_split)-1):
        for col in range(1,len(data_split)-1):
            distances = {'up': 0, 'down': 0, 'left':0, 'right':0}
        # check up
            for i in range(1,line+1):
                if forest[line][col] > forest[line-i, col]:
                    distances['up'] += 1
                else:
                    distances['up'] += 1
                    break
            #check down
            for i in range(1,len(data_split)-line):
                if forest[line][col] > forest[line+i, col]:
                    distances['down'] += 1
                else:
                    distances['down'] += 1
                    break
            #check left
            for i in range(1,col+1):
                if forest[line][col] > forest[line, col-i]:
                    distances['left'] += 1
                else:
                    distances['left'] += 1
                    break
            #check right
            for i in range(1,len(data_split)-col):
                if forest[line][col] > forest[line, col+i]:
                    distances['right'] += 1
                else:
                    distances['right'] += 1
                    break
            score = np.prod(list(distances.values()))
            if score > max_score:
                max_score = score
    return max_score

with open("test_data/test08.txt") as file:
    test_data = file.read()
    print(treetop(test_data))

print(f'part 1 solution = {treetop(raw_data)}')

with open("test_data/test08.txt") as file:
    test_data = file.read()
    print(treetop_2(test_data))

print(f'part 2 solution = {treetop_2(raw_data)}')
