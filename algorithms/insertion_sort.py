# insertion sort

import random
import time

def initialize_array(n: int) -> list:
    ''' initialize_array
        ----------------
        Returns an array of n elements with random values
    '''
    return [random.randint(1, 100) for i in range(n)]

def insertion_sort(array: list) -> list:
    ''' insertion_sort
        ----------------
        Sorts an array using the insertion sort algorithm
    '''
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

if __name__ == '__main__':
    n = 10
    array = initialize_array(n)
    print(f"input: {array}")
    print(f"running insertion sort...")
    t = time.time()
    sorted_array = insertion_sort(array)
    elapsed = time.time() - t
    print(f"output: {sorted_array}")
    print(f"elapsed time: {elapsed:.9f} seconds")

