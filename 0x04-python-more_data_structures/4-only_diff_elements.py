#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result1 = {x for x in set_1 if x not in set_2}
    result2 = {x for x in set_2 if x not in set_1}
    result = result1.union(result2)
    return result
