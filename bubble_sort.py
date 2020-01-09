def bubble_sort(array):
    """
    Sort array using bubble-sort algorithm.
    :param array: 1D-array to be sorted.
    :return: sorted version of input array.
    """
    for iteration in range(len(array)):
        for index in range(len(array)- iteration - 1):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
    return array

if __name__ == '__main__':
    example_array = [-2,1,-3,4,-1,2,1,-5,4]
    print(f'The array {example_array} sorted is {bubble_sort(example_array)}')
