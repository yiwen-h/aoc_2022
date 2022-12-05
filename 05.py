# Supply Stacks

from load_data import get_data

raw_data = get_data(5)



def supplystacks(data):
    parse = data.split('\n\n')
    map = parse[0].split('\n')
    instructions = parse[1].split('\n')[:-1]
    stack_ids = map[-1].split()
    stack_maps = {}
    for k in stack_ids:
        stack_maps[k] = []
    for row in map[:-1]:
        for i in range(1,len(stack_ids)+1):
            pos = 4 * i - 3
            if len(row) > pos:
                if row[pos] !=  ' ':
                    stack_maps[stack_ids[i-1]].append(row[pos])
    for k, v in stack_maps.items():
        stack_maps[k] = list(reversed(v))
    for each in instructions:
        instr_split = [x for x in each.split() if x.isnumeric()]
        for moves in range(int(instr_split[0])):
            tomove = stack_maps[instr_split[1]][-1]
            stack_maps[instr_split[2]] += tomove
            stack_maps[instr_split[1]].pop()
    answer = ''
    for s in stack_maps:
        if stack_maps[s] is not None:
            answer += stack_maps[s][-1]
    return answer


# with open("test_data/test05.txt") as file:
#     test_data = file.read()
#     print(supplystacks(test_data))

print(f'part 1 solution = {supplystacks(raw_data)}')


def supplystacks_2(data):
    parse = data.split('\n\n')
    map = parse[0].split('\n')
    instructions = parse[1].split('\n')[:-1]
    stack_ids = map[-1].split()
    stack_maps = {}
    for k in stack_ids:
        stack_maps[k] = []
    for row in map[:-1]:
        for i in range(1,len(stack_ids)+1):
            pos = 4 * i - 3
            if len(row) > pos:
                if row[pos] !=  ' ':
                    stack_maps[stack_ids[i-1]].append(row[pos])
    for k, v in stack_maps.items():
        stack_maps[k] = list(reversed(v))
    for each in instructions:
        instr_split = [x for x in each.split() if x.isnumeric()]
        num_to_move = int(instr_split[0])
        tomove = stack_maps[instr_split[1]][-num_to_move:]
        stack_maps[instr_split[2]] += tomove
        stack_maps[instr_split[1]] = stack_maps[instr_split[1]][:-num_to_move]
    answer = ''
    for s in stack_maps:
        if stack_maps[s]:
            answer += stack_maps[s][-1]
    return answer


with open("test_data/test05.txt") as file:
    test_data = file.read()
    print(supplystacks_2(test_data))

print(f'part 2 solution = {supplystacks_2(raw_data)}')
