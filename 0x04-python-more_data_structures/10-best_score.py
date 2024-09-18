#!/usr/bin/python3
def best_score(a_dictionary):
    result_val = 0
    result_key = ""
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    for k, v in a_dictionary.items():
        if v > result_val:
            result_val = v
            result_key = k
    return result_key
