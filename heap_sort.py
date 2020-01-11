def heapify(array, heap_size, root_index):
    """
    To heapify subtree of the binary heap reperesentation of
    a given array.
    :param array: input array.
    :param heap_size: size of subarray to be heapified.
    :param root_index: index of root element of subtree to be heapified.
    """
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and array[left_child] > array[largest]:
        largest = left_child
    if right_child < heap_size and array[right_child] > array[largest]:
        largest = right_child
    if largest != root_index:
        array[root_index], array[largest] = array[largest], array[root_index]
        heapify(array, heap_size, largest)


def heap_sort(array):
    """
    Sort array using heap-sort algorithm.
    :param array: sorted 1D-array to be sorted.
    """
    n = len(array)
    for i in range(n, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


if __name__ == '__main__':
    example_array = [-2,1,-3,4,-1,2,1,-5,4]
    example_array_copy=example_array.copy()
    heap_sort(example_array)
    print(f'The array {example_array_copy} sorted is {example_array}')
