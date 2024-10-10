#!/usr/bin/env python3

def join_sets(s1, s2):
    return s1 | s2  # Union of the two sets

def match_sets(s1, s2):
    return s1 & s2  # Intersection of the two sets

def diff_sets(s1, s2):
    return s1 ^ s2  # Symmetric difference of the two sets

if __name__ == '__main__':
    set1 = set(range(1, 10))
    set2 = set(range(5, 15))
    print(set1)
    print(set2)
    print(join_sets(set1, set2))
    print(match_sets(set1, set2))
    print(diff_sets(set1, set2))
