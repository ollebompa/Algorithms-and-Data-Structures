def binary_search(array, target_value):
    """
    Search for a target value within a sorted using binary search.
    :param array: sorted 1D-array to be searched.
    :param target_value: value to be searched for in array.
    :return: if element with target value is in array:
             ---> index of element with target value in array.
             if target_value is not in array:
             ---> -1.
    """
    start_index = 0
    end_index = len(lst)-1
    index = -1
    while end_index >= start_index and index == -1:
        mid = int((end_index+start_index)/2)
        if array[mid] == target_value:
            index = mid
        elif array[mid] > target_value:
            end_index = mid-1
        else:
            start_index = mid+1
    return index



if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 11, 16, 100, 500]
    print (binary_search(lst, 10))
    print (binary_search(lst, 11))
    lst = [3, 5, 7, 9, 11, 16, 100, 500]
    print (binary_search(lst, 10))
    print (binary_search(lst, 11))
