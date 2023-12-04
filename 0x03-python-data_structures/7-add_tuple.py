#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_a = 0
    sum_b = 0
    if tuple_a[0] is None:
        tuple_a[0] = 0
    if tuple_a[1] is None:
        tuple_a[1] = 0
    if tuple_b[0] is None:
        tuple_b[0] = 0
    if tuple_b[1] is None:
        tuple_b[1] = 0
    new_tuple[0] = tuple_a[0] + tuple_b[0]
    new_tuple[1] = tuple_a[1] + tuple_b[1]
    return new_tuple
