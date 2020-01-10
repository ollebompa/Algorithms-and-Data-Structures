def insertion_sort(array):
    """
    Sort array using insertion-sort algorithm.
    :param array: 1D-array to be sorted.
    :return: sorted version of input array.
    """
    for i in range(1, len(array)):
        j = i-1
        element = array[i]
        while j>= 0 and element < array[j]:
            array[j+1] = array[j]
            j-= 1
        array[j+1] = element
    return array

if __name__ == '__main__':
    example_array = [-2,1,-3,4,-1,2,1,-5,4]
    print(f'The array {example_array} sorted is {insertion_sort(example_array)}')
