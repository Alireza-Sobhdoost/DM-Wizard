import re
from time import time

import numpy as np

number_of_varables = 0
target = 0

def sort_conditions(conditions):
    def get_number(condition):
        parts = condition.split('X')
        return int(parts[-1].split()[0])

    sorted_conditions = sorted(conditions, key=get_number)
    return sorted_conditions

def parse_condition(condition ):
    global number_of_varables
    global target
    Ub_diff = 0

    # print(condition)
    number = condition.find("X") + 1
    parts_c = condition.split("X"+condition[number])
    # print(parts_c)
    ranges = list()
    for i in range (len(parts_c)) :
        if parts_c[i] == ' '  :
            if i == 0 :
                ranges.append(0)
                continue
            elif i == 1 :
                ranges.append(target)
                break
        bound = 0
        if '!' in parts_c[i]:
            parts = parts_c[i].split('!')
            parts = [x for x in parts if x.strip()]
            bound = int(parts[0])
            if i == 0 :
                Ub_diff = bound
                target -= bound
                ranges.append(0)
            if i == 1:
                bound -= Ub_diff
                ranges.append(bound)
        elif '<' in parts_c[i]:
            parts = parts_c[i].split('<')
            parts = [x for x in parts if x.strip()]
            if i == 0 :
                bound = int(parts[0])+1
                Ub_diff = bound
                target -= bound
                ranges.append(0)
            elif i == 1 :
                bound = int(parts[0])-1
                bound -= Ub_diff
                ranges.append(bound)


    ranges[1] += 1
    # print(ranges)
    arange = tuple(ranges)
    # print(arange)
    return arange



def set_range(conditions ):
    global number_of_varables
    global  target
    ranges = list()
    j = 0
    for i in range (number_of_varables) :
        # print(j)
        # print(conditions)
        if j < len(conditions):
            if ("X"+str(i+1) in conditions[j]) :
                conditions[j] = conditions[j].replace("<=", "!")
                if "=" in conditions[j] :
                    parts = conditions[j].split("X"+str(i+1))
                    parts = [x for x in parts if x.strip()]
                    partx = parts[0].split("=")
                    partx = [x for x in partx if x.strip()]
                    bound = int(partx[0])
                    target -= bound
                    number_of_varables -= 1
                else :
                    Bound = parse_condition(conditions[j])
                    ranges.append(Bound)

        else :
            ranges.append((0 ,target+1))
            j -= 1
        j += 1
    # print(ranges)
    return ranges

def find_combinations(num_values, arange_ranges, target_sum):
    values = [np.arange(*arange_range) for arange_range in arange_ranges]
    # print(values)
    meshgrid_result = np.meshgrid(*values, indexing='ij')
    # print(meshgrid_result)
    combinations = np.stack(meshgrid_result, axis=-1).reshape(-1, num_values)

    # Filter combinations that sum up to the target sum
    valid_combinations = combinations[combinations.sum(axis=1) == target_sum]
    # print(valid_combinations)

    return len(valid_combinations)

def set_combinations (s):
    global number_of_varables
    global target
    # try :
    sperated_lines = re.split("\n" , s)
    # print(sperated_lines[0])
    number_of_varables = sperated_lines[0].count("+") + 1
    target = int((re.split("=" , sperated_lines[0]))[-1])
    conditions=[]
    if len(sperated_lines) > 1:
        conditions = re.split("," ,  sperated_lines[1])
        conditions = sort_conditions(conditions)
    # print(conditions)
    aranges = set_range(conditions)
    # print(aranges)
    output = find_combinations(number_of_varables , aranges , target)
    return str(output)
    # except :
    #     print("Error please check your input")

s = time()
print(set_combinations("X1 + X2 + X3 + X4 = 54\n0 <= X2 <= 10 , 2 < X1 <= 4 , 1 <= X4 < 5 , X3 = 42"))
e = time()
# print(e - s)

