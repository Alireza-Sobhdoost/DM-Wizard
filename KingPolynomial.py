import copy
import re
import time

import numpy as np


def find_neighbors(matrix, coord, king_were_there):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    iner = coord[0]
    row = coord[1]
    col = coord[2]

    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]

        if 0 <= new_row < len(matrix[iner]) and 0 <= new_col < len(matrix[iner][0]):
            matrix[iner][new_row][new_col] = 1

    for i, r, c in king_were_there:
        matrix[i][r][c] = 2

    matrix[iner][row][col] = 3

    available = 0
    for i in matrix:
        available += sum(row.count(0) for row in i)

    return available

def find_neighbors3d(matrix, row , col, king_were_there):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    # iner = coord[0]
    # row = coord[1]
    # col = coord[2]

    for direction in directions:
        new_row = row + direction[0]
        new_col = col + direction[1]

        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
            matrix[new_row][new_col] = 1

    for i, r, c in king_were_there:
        matrix[r][c] = 2

    matrix[row][col] = 3

    # available = 0
    # for i in matrix:
    available = sum(row.count(0) for row in matrix)

    return available


def index_key(matrix):
    flat_array = np.array(matrix).flatten()
    index = 0
    index_mapping = dict()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
                index_mapping[index] = (i, j, k)
                index += 1

    return index_mapping

def king_poly (board ) :
    number_of_kings = [1]
    if len(number_of_kings) == 1 :
        available = 0
        for i in board:
            available += sum(row.count(0) for row in i)
        key = index_key(board)
        # print(key)

        king_were_there = list()
        final_board = copy.deepcopy(board)
        number_of_posibles = 0
        reboard = []
        number_of_kings.append(available)
        i = 0
        for _ in range(available):
            final_board = copy.deepcopy(board)
            while True :
                position = key[i]
                if  final_board[position[0]][position[1]][position[2]] == 0:
                    break
                else:
                    i += 1

            king_were_there.append(position)
            number_of_posibles += find_neighbors(final_board, position, king_were_there)
            # for k in final_board:
            #     for j in k:
            #         print(j)
            #     print()
            i += 1

            if sum(sum(row.count(0) for row in i) for i in final_board) > 1:
                reboard.extend(final_board)

        number_of_kings.append(number_of_posibles)
        # print(number_of_posibles)

        # print(number_of_kings)
        board = reboard
        # for i in board:
        #     for j in i :
        #         print(j)
        #     print()

        # return board , number_of_kings

    while (len(board) != 0) :


        key = index_key(board)
        # print(key)
        number_of_posibles = 0
        reboard = []
        i = 0
        for index in range(len(board)):
            available = sum(row.count(0) for row in board[index])
            # print(available)
            king_were_there = list()
            i += 1
            for _ in range(available):
                final_board = copy.deepcopy(board[index])
                # print(final_board)
                position = key[i]
                while True:
                    # print(final_board[position[1]][position[2]])
                    if final_board[position[1]][position[2]] == 0:
                        #
                        break
                    else:
                        i += 1
                    position = key[i]
                # print(position)

                king_were_there.append(position)
                x = position
                number_of_posibles += find_neighbors3d(final_board, x[1], x[2], king_were_there)
                # for j in final_board:
                #         print(j)
                # print()

                # print(number_of_posibles)
                # #
                if sum(row.count(0) for row in final_board) > 1:
                    reboard.append(final_board)
                i += 1
        number_of_kings.append(number_of_posibles)

        # print(number_of_kings)
        board = reboard
        # print(reboard)

    result = np.array(number_of_kings)
    result = np.flip(result)
    result = np.poly1d(result)

    return result

# board = [[[0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0]]]


def parse_input_string(s):
    text = s.split("\n")
    dimensions = text[0].split(" ")
    n, m = int(dimensions[0]), int(dimensions[1])

    table = [[int(x) for x in row.split()] for row in text[1:]]

    return n, m, table
def Kingpolynomial (s) :

    n , m , table =parse_input_string(s)
    board = list()
    board.append(table)
    # print(board)
    # print(board)
    available = 0
    for i in board:
        available += sum(row.count(0) for row in i)
    # print(available)
    arr = [1,available]
    if (m <= 2 and n <= 2):
        result = np.array(arr)
        result = np.flip(result)
        result = np.poly1d(result)
        return result
    else:
        return king_poly(board)

s = time.time()
print(Kingpolynomial("5 5\n0 0 0 0 0\n0 0 0 0 0\n0 0 0 0 0\n0 0 0 0 0\n0 0 0 0 0"))
f = time.time()
print(f -s)
#
#
# board = [[[0, 0],
#           [0, 0]]]
# available = 0
# number_of_kings = [1]
# for i in board:
#     available += sum(row.count(0) for row in i)
# number_of_kings.append(available)

#
# print(king_poly(board ))
#
# # result = king_poly(board)
# #
# # a = np.array(result)
# # b = np.flip(a)
# print(np.poly1d(b))