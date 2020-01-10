def binary_search(lst, element):
    start_index = 0
    end_index = len(lst)-1
    index = -1
    while end_index >= start_index and index == -1:
        mid = int((end_index+start_index)/2)
        if lst[mid] == element:
            index = mid
        elif lst[mid] > element:
            end_index = mid-1
        else:
            start_index = mid+1
    return index



if __name__ == '__main__':

    lst = [2, 3, 5, 7, 9, 11, 16, 100, 500]
    print (binary_search(lst, 10))
    print (binary_search(lst, 11))
    lst = [3, 5, 7, 9, 11, 16, 100, 500]
    print (binary_search(lst, 10))
    print (binary_search(lst, 11))
