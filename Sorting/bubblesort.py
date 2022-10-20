import numpy as np
import random as rd

""" BubbleSort and helper function. """


def swap(array, index1, index2):
    cache = array[index1]
    array[index1] = array[index2]
    array[index2] = cache
    return array

def bubblesort(array) -> list:
    # defining variables. 
    n = len(array)
    token = False
    # While there are still unordered pairs.
    while(token == False):
        # Variable for unordered pairs.
        cache = 0
        for i in range(1, n):
            # Find two consequtive wrong values.  
            if array[i-1] > array[i]:
                # Swap values and change cache to one. 
                array = swap(array, i -1, i)
                cache = 1
        # If cache == 0, then there are no two consequtive values out of order.
        if cache == 0:
            token = True
    return array

""" Test function to check results. """

# Checks if the given array A is sorted correctly.
def check_array(A):
    # Calculate the difference between two consequtive values, should be negative for each pair of values if sorted correctly.
    cache = [A[i] - A[i +1] for i in range(0, len(A) -1)]
    # True if max value is negative, else False.
    return (np.max(cache) < 0)


if __name__ == "__main__":
    val_range, set_size = 100, 15

    array = np.arange(val_range)
    array = rd.sample(list(array), k = set_size)
    print(f"Array Test: {array}")

    # Run the sorting algorithms.
    test_bubblesort = bubblesort(array)
    print(test_bubblesort)

    # Check results.
    if not check_array(test_bubblesort): 
        print(f"Something went wrong: {test_bubblesort}")