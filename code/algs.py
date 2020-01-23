import numpy as np
import matplotlib.pyplot as plt

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
    # equal sign, use assignment for complexity
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
    assignment = 0
    conditional = 0

    list_length = len(x)
    assignment += 1

    conditional += 1
    if list_length <= 1:
        return x, assignment, conditional
    else:
        pivot = x.pop()

    items_greater = []
    items_lower = []
    assignment += 2

    for items in x:

        conditional += 1
        if items > pivot:
            items_greater.append(items)
        else:
            items_lower.append(items)

    x1, assignment_1, conditional_1 = quicksort(items_lower)
    x2, assignment_2, conditional_2 = quicksort(items_greater)
    assignment += 2

    return x1 + [pivot] + x2, assignment_1 + assignment_2, conditional_1 + conditional_2

def insertionsort(x):
    """
    Describe how you are sorting 'x'
    """
    assignment = 0
    conditional = 0

    list_length = len(x)
    assignment += 1

    for i in range(1,list_length):
        cur_value = x[i]
        pos = i
        assignment += 3

        conditional += 2
        while pos > 0 and x[pos-1] > cur_value:
            x[pos] = x[pos-1]
            pos = pos - 1
            assignment +=2

        x[pos] = cur_value
        assignment += 1

    return x

# assignment_list = []
# conditional_list = []
# x_label = []
# for i in range(10):
#     x = np.random.rand(i).tolist()
#     sorted_list, Assignment, Conditional = quicksort(x)
#     assignment_list.append(Assignment)
#     conditional_list.append(Conditional)
#     x_label.append(i)

# print(assignment_list)

# plt.plot(x_label, assignment_list)

