import random

def max_sum_subarray(array):
    """
    Compute the maximum sum subarray or array using Kadane's algorithm.
    :param array: 1D-array of which the maximum sum subarray is to be found.
    :return: 2-tuple (maximum sum subarray of array, sum of this subarray)
    """
    max_sum = float('-inf')
    start_index = end_index = sum = 0
    for end_index, element in enumerate(array):
        if sum <= 0:
            start_index = end_index
            sum = element
        else:
            sum += element

        if sum > max_sum:
            max_sum = sum
            max_start_index = start_index
            max_end_index = end_index

    return array[max_start_index: max_end_index + 1], max_sum


if __name__ == '__main__':
    example_array = [-2,1,-3,4,-1,2,1,-5,4]
    max_sum_sub, max_sum = max_sum_subarray(example_array)
    print(f'The maximum sum subarray of the array {example_array} is')
    print(f'{max_sum_sub}, and has a sum of {max_sum}')
