
def quick_sort(array, low, high):
    """
    Sort array using quick-sort algorithm.
    :param array: 1D-array to be sorted.
    :return: sorted version of input array.
    """
    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index - 1)
        quick_sort(array, pivot_index + 1, high)


def partition(array, low, high):
    """
    Partition array using Lomuto partition scheme.
    :param array: 1D-array to be partitioned.
    :param high: index if last element in array.
    :param low: index of first element of array.
    :return: index if pivots final postion in sorted array.
    """
    pivot = array[high]
    i = low
    for j in range(low, high):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[high] = array[high], array[i]
    return i



if __name__ == '__main__':
    example_array = [-2,1,-3,4,-1,2,1,-5,4]
    example_array_copy=example_array.copy()
    quick_sort(example_array, 0, len(example_array) - 1)
    print(f'The array {example_array_copy} sorted is {example_array}')
