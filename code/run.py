# You can do all of this in the `__main__.py` file, but this file exists
# to shows how to do relative import functions from another python file in
# the same directory as this one.
import numpy as np
from .algs import quicksort, bubblesort, insertionsort


def run_stuff():
    """
    This function is called in `__main__.py`
    """
    print("This is `run()` from ", __file__)

    # x = np.random.rand(10).tolist()
    # x = ['bulbasaur', 'evee', 'pikachu', 'zappados', 'growlithe', 'richu']
    x = [9,10,11]
    print("Unsorted input: ", x)

    print("Bubble sort output: ", bubblesort(x))
    # print("Quick sort output: ", quicksort(x))
    # print("Insertion sort output: ", insertionsort(x))


    #test_pointless_sort()

