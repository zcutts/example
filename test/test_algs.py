import numpy as np
from code import algs

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10).tolist()

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    # x = np.array([1,2,4,0,1]).tolist()
    v = [1, 2, 8, 3]
    w = [5]
    x = ['a', 'c', 'b']
    y = [1, 2, 3, 8, 2]
    z = []
    # for now, just attempt to call the bubblesort function, should
    # actually check output
    # algs.bubblesort(x)
    # algs.bubblesort(y)
    # algs.bubblesort(z)
    assert np.array_equal(algs.bubblesort(v), np.array([1,2,3,8]))
    assert np.array_equal(algs.bubblesort(w), np.array([5]))
    assert np.array_equal(algs.bubblesort(x), np.array(['a', 'b', 'c']))
    assert np.array_equal(algs.bubblesort(y), np.array([1,2,2,3,8]))
    assert np.array_equal(algs.bubblesort(z), np.array([]))

    print("Bubble sort output: ", algs.bubblesort(x))

def test_quicksort():

    v = [1, 2, 8, 3]
    w = [5]
    x = ['zach', 'hannah', 'josh']
    y = [1, 2, 3, 8, 2]
    z = []
    # for now, just attempt to call the quicksort function, should
    # actually check output
    algs.quicksort(x)

    assert np.array_equal(algs.quicksort(v), np.array([1,2,3,8]))
    assert np.array_equal(algs.quicksort(w), np.array([5]))
    # need to figure out why this test isn't working
    assert np.array_equal(algs.quicksort(x), np.array(['hannah', 'josh', 'zach']))
    assert np.array_equal(algs.quicksort(y), np.array([1,2,2,3,8]))
    assert np.array_equal(algs.quicksort(z), np.array([]))

def test_insertionsort():
    v = [1, 2, 8, 3]
    w = [5]
    x = ['a', 'c', 'b']
    y = [1, 2, 3, 8, 2]
    z = []

    assert np.array_equal(algs.bubblesort(v), np.array([1,2,3,8]))
    assert np.array_equal(algs.bubblesort(w), np.array([5]))
    assert np.array_equal(algs.bubblesort(x), np.array(['a', 'b', 'c']))
    assert np.array_equal(algs.bubblesort(y), np.array([1,2,2,3,8]))
    assert np.array_equal(algs.bubblesort(z), np.array([]))


