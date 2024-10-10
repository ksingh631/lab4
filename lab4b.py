#!/usr/bin/env python3

def join_lists(l1, l2):
    return list(set(l1) | set(l2))  # Union of the two lists as sets, then convert back to a list

def match_lists(l1, l2):
    return list(set(l1) & set(l2))  # Intersection of the two lists as sets, then convert back to a list

def diff_lists(l1, l2):
    return list(set(l1) ^ set(l2))  # Symmetric difference of the two lists as sets, then convert back to a list

if __name__ == '__main__':
    list1 = list(range(1, 10))
    list2 = list(range(5, 15))
    print(list1)
    print(list2)
    print(join_lists(list1, list2))
    print(match_lists(list1, list2))
    print(diff_lists(list1, list2))
