def merge_sort(array):
    """
    Sort array using merge-sort algorithm.
    :param array: 1D-array to be sorted.
    :return: sorted version of input array.
    """
    if len(array) > 1:
        mid_index = len(array)//2
        left_subarray = array[:mid_index]
        right_subarray = array[mid_index:]
        merge_sort(left_subarray)
        merge_sort(right_subarray)

        left_index = 0
        right_index = 0
        overall_index = 0
        while left_index < len(left_subarray) and right_index < len(right_subarray):
            if left_subarray[left_index] < right_subarray[right_index]:
                array[overall_index] = left_subarray[left_index]
                left_index +=1
            else:
                array[overall_index] = right_subarray[right_index]
                right_index +=1
            overall_index +=1
        #check if there is any remainder
        while left_index < len(left_subarray):
            array[overall_index] = left_subarray[left_index]
            left_index +=1
            overall_index +=1
        while right_index < len(right_subarray):
            array[overall_index] = right_subarray[right_index]
            right_index +=1
            overall_index +=1




if __name__ == '__main__':
    example_array = [-2,1,-3,4,-1,2,1,-5,4]
    example_array_copy=example_array.copy()
    merge_sort(example_array)
    print(f'The array {example_array_copy} sorted is {example_array}')
