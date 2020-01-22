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
    # equal sign
    assignment = 0

    # ==, <, > is a conditional
    conditional = 0

    list_length = len(x)
    assignment += 1

    for j in range(list_length):
        swap = False
        assignment +=2

        for i in range(list_length-1):
            assignment += 1
            conditional += 1
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
                assignment += 2

        swap = True
        assignment += 1

        conditional += 1
        if swap == False:
            break
    return x, assignment, conditional

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
    assignment += 1

    conditional += 1
    if list_length <= 1:
        return x
    else:
        pivot = x.pop()

    items_greater = []
    items_lower = []

    for items in x:

        conditional += 1
        if items > pivot:
            items_greater.append(items)
        else:
            items_lower.append(items)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)

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

assignment_list = []
conditional_list = []
for i in range(10):
    x = np.random.rand(i).tolist()
    sorted_list, Assignment, Conditional = bubblesort(x)
    assignment_list.append(Assignment)
    conditional_list.append(Conditional)

print(assignment_list)



