#!/usr/bin/python3
""" function find_peak with binary search  """
def find_peak(list_of_integers):
    if len(list) == 0:
        return None
    if len(list) == 1:
        return list[0]
    if len(list) == 2:
        return max(list)
    mid = len(list) / 2
    if list[mid] < list[mid - 1]:
        return find_peak(list[:mid])
    elif list[mid] < list[mid + 1]:
        return find_peak(list[mid + 1:])
    else:
        return list[mid] 

