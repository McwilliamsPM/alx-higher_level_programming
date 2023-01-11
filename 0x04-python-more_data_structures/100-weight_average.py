#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    a = 0
    b = 0
    for n, m in my_list:
        a += n * m
        b += m
    return (a / b)
