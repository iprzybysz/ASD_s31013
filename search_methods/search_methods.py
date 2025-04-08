import math
from typing import List


def binary_search(array: List[int], key: int) -> int:
    l = 0
    r = len(array) - 1

    while (l <= r):
        m = math.floor((l + r) / 2)

        if array[m] == key:
            return m
        
        if array[m] > key:
            r = m - 1
        else:
            l = m + 1

    return -1

def jump_k(array: List[int], key: int) -> int:
    array_len = len(array)
    if array_len == 0:
        return -1
        
    k = math.floor(math.sqrt(array_len))
    current_k = k
    prev_k = 0 

    while current_k < array_len and array[min(current_k, array_len - 1)] < key:
        prev_k = current_k
        current_k += k
        if prev_k >= array_len:
            return -1

    while prev_k <= min(current_k, array_len - 1):
        if array[prev_k] == key:
            return prev_k
        prev_k += 1

    return -1
