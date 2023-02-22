def bubblesort(array):
    for i in range(len(array)):
        for index in range(0, len(array)-i-1):
            # if current is larger than next, swap
            if array[index] > array[index+1]:
                temp = array[index+1]
                array[index+1] = array[index]
                array[index] = temp
    return array

def selsort(array):
    for i in range(len(array)):
        # set current index as the minimum index
        min_idx = i
        current = array[i]
        # compare current element with every other element in the unsorted list
        for j in range(i+1, len(array)):
            # if new minimum exists, it's index becomes min index
            if array[min_idx] > array[j]:
                min_idx = j
        # swap current element with the actual minimum element
        array[i] = array[min_idx]
        array[min_idx] = current
    return array

def inssort(array):
    for i in range(1, len(array)-1):
        current = array[i]
        pos = i
        # while not at the leftmost and current unsorted is less than left element:
        # move left element to current pos and reduce pos by 1
        while pos > 0 and current < array[pos-1]:
                array[pos] = array[pos-1]
                pos -= 1
        # when nothing is smaller, put current at pos
        array[pos] = current
    return array

def partition(arr, left, right):
    # i moves right, j moves left
    i = left
    j = right-1
    # choose last element as pivot
    pivot = arr[right]
    # while j has not passed i yet
    while i < j:
        # i finds element greater than pivot and stops
        # j finds element less than pivot and stops
        while i < right and arr[i] < pivot:
            # move right
            i += 1
        while j > left and arr[i] > pivot:
            # move left
            j -= 1
        # check again j has not passed i
        # then swap
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # once j has passed i,
    # if pivot is smaller than element at i
    # swap pivot element and element at i
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    # return pivot index which should be at i
    return i


def quicksort(arr, left, right):
    # if left index is still less than right index, meaning length still more than 1
    if left < right:
        # find partition index
        partitionPos = partition(arr, left, right)
        # sort left and then right excluding pivot element
        quicksort(arr, left, partitionPos-1)
        quicksort(arr, partitionPos+1, right)
    return arr


list1 = [-2, 3, 0, 11, 111,88,-97,231,747, 0, 3]

print(bubblesort(list1))
print(selsort(list1))
print(inssort(list1))
print(quicksort(list1, 0, len(list1)-1))