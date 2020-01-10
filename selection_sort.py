def selection_sort(array):
    """
    Sort array using selection-sort algorithm.
    :param array: 1D-array to be sorted.
    :return: sorted version of input array.
    """
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array

if __name__ == '__main__':
    example_array = [-2,1,-3,4,-1,2,1,-5,4]
    print(f'The array {example_array} sorted is {selection_sort(example_array)}')
