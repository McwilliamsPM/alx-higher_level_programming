#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        for v in range(len(matrix[x])):
            print("{:d}".format(matrix[x][v]), end="")
            if v != (len(matrix[x]) - 1):
                print(" ", end="")
        print("")
