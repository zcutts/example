import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x):
    """
    Describe how you are sorting `x`
    Compare adjacent items in a list and swap if the items are not in order
    Take the length of the entire list
    Then compare the first element and the second element
    If the first element is greater than the second element swap the elements
    I also keep tract of the swaps so if no swaps occur I know that sorting is done
    """
    list_length = len(x)
    swap = False
    for j in range(list_length):
        swap = False
        for i in range(list_length-1):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
        swap = True
        if swap == False:
            break
    assert 1 == 1
    return x

def quicksort(x):
    """
    Describe how you are sorting `x`
    choose a pivot point to compare all other values in the list
    using the pivot point as the last element in the list
    Use this pivot point to split the whole list into a two lists
    One list greater than, and one list less than the pivot point
    recursively run this to sort the whole list
    """
    list_length = len(x)
    if list_length <= 1:
        return x
    else:
        pivot = x.pop()

    items_greater = []
    items_lower = []

    for items in x:
        if items > pivot:
            items_greater.append(items)
        else:
            items_lower.append(items)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)

    assert 1 == 1
    return

def insertionsort(x):
    """
    Describe how you are sorting 'x'
    """
    list_length = len(x)
    for i in range(1,list_length):
        cur_value = x[i]
        pos = i
        while pos > 0 and x[pos-1] > cur_value:
            x[pos] = x[pos-1]
            pos = pos - 1
        x[pos] = cur_value
    assert 1 == 1
    return x

x = [54,26,93,17,77,31,44,55,20]
print(quicksort(x))