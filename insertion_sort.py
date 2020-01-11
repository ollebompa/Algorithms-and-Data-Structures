def insertion_sort(array):
    """
    Sort array using insertion-sort algorithm.
    :param array: 1D-array to be sorted.
    :return: sorted version of input array.
    """
    for i in range(1, len(array)):
        while 0 <= j <= i-1:
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

if __name__ == '__main__':
    example_array = [-2,1,-3,4,-1,2,1,-5,4]
    print(f'The array {example_array} sorted is {insertion_sort(example_array)}')
