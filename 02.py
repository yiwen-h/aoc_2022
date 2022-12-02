# Rock Paper Scissors
from load_data import get_data

raw_data = get_data(2)

"""
A = Rock
B = Paper
C = Scissors

X = Rock
Y = Paper
Z = Scissors
"""

points_for_chosen = {'X': 1, 'Y': 2, 'Z': 3}
shape = {'A': 'Rock',
        'B': 'Paper',
        'C': 'Scissors',
        'X': 'Rock',
        'Y': 'Paper',
        'Z': 'Scissors'}

def rockpaperscissors(data):
    split_data = data.split('\n')[:-1]
    selections = []
    score = 0
    for i in split_data:
        score += points_for_chosen[i[-1]]
        selected = (shape[i[0]], shape[i[-1]])
        selections.append(selected)
    # get points for outcome
    for match in selections:
        if match[0] == match[1]:
            score += 3
        elif match[0] == 'Rock':
            if match[1] == 'Paper':
                score += 6
            elif match[1] == 'Scissors':
                score += 0
        elif match[0] == 'Paper':
            if match[1] == 'Rock':
                score += 0
            elif match[1] == 'Scissors':
                score += 6
        elif match[0] == 'Scissors':
            if match[1] == 'Rock':
                score += 6
            elif match[1] == 'Paper':
                score += 0
    return score


# with open("test_data/test02.txt") as file:
#     test_data = file.read()
#     print(rockpaperscissors(test_data))

print(f'part 1 solution = {rockpaperscissors(raw_data)}')



points_for_chosen_2 = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
shape_2 = {'A': 'Rock',
        'B': 'Paper',
        'C': 'Scissors'}
outcomes = {'X': 'Lose',
            'Y': 'Draw',
            'Z': 'Win'}
points_for_outcome = {'Lose': 0,
                      'Draw': 3,
                      'Win': 6}

def rockpaperscissors_2(data):
    split_data = data.split('\n')[:-1]
    selections = []
    score = 0
    for i in split_data:
        selected = (shape_2[i[0]], outcomes[i[-1]])
        selections.append(selected)
    # Score for outcomes
        score += points_for_outcome[selected[1]]
    # Get score for selected shape
    for match in selections:
        if match[1] == 'Draw':
            score += points_for_chosen_2[match[0]]
        elif match[0] == 'Rock':
            if match[1] == 'Win':
                score += points_for_chosen_2['Paper']
            elif match[1] == 'Lose':
                score += points_for_chosen_2['Scissors']
        elif match[0] == 'Paper':
            if match[1] == 'Win':
                score += points_for_chosen_2['Scissors']
            elif match[1] == 'Lose':
                score += points_for_chosen_2['Rock']
        elif match[0] == 'Scissors':
            if match[1] == 'Win':
                score += points_for_chosen_2['Rock']
            elif match[1] == 'Lose':
                score += points_for_chosen_2['Paper']
    return score

# with open("test_data/test02.txt") as file:
#     test_data = file.read()
#     print(rockpaperscissors_2(test_data))

print(f'part 2 solution = {rockpaperscissors_2(raw_data)}')
