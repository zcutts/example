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

    # reverse ordered list
    s = [11,10,9]

    # ordered list
    t = [9,10,11]

    # negative numbers
    u = [-1, -100, -30, -50, 20, 50, 61]

    # unordered list
    v = [1, 2, 8, 3]

    # one element list
    w = [5]

    # characters
    x = ['a', 'c', 'b']

    # duplicates
    y = [1, 2, 3, 8, 2]

    # empty array
    z = []


    assert np.array_equal(algs.bubblesort(s)[0], np.array([9,10,11]))
    assert np.array_equal(algs.bubblesort(t)[0], np.array([9,10,11]))
    assert np.array_equal(algs.bubblesort(u)[0], np.array([-100,-50,-30,-1,20,50,61]))
    assert np.array_equal(algs.bubblesort(v)[0], np.array([1,2,3,8]))
    assert np.array_equal(algs.bubblesort(w)[0], np.array([5]))
    assert np.array_equal(algs.bubblesort(x)[0], np.array(['a', 'b', 'c']))
    assert np.array_equal(algs.bubblesort(y)[0], np.array([1,2,2,3,8]))
    assert np.array_equal(algs.bubblesort(z)[0], np.array([]))

    print("Bubble sort output: ", algs.bubblesort(x))

def test_quicksort():
    # reverse ordered list
    s = [11,10,9]

    # ordered list
    t = [9,10,11]

    # negative numbers
    u = [-1, -100, -30, -50, 20, 50, 61]

    # unordered list
    v = [1, 2, 8, 3]

    # one element list
    w = [5]

    # characters
    x = ['a', 'c', 'b']

    # duplicates
    y = [1, 2, 3, 8, 2]

    # empty array
    z = []

    assert np.array_equal(algs.quicksort(s)[0], np.array([9,10,11]))
    assert np.array_equal(algs.quicksort(t)[0], np.array([9,10,11]))
    assert np.array_equal(algs.quicksort(u)[0], np.array([-100,-50,-30,-1,20,50,61]))
    assert np.array_equal(algs.quicksort(v)[0], np.array([1,2,3,8]))
    assert np.array_equal(algs.quicksort(w)[0], np.array([5]))
    assert np.array_equal(algs.quicksort(x)[0], np.array(['a', 'b', 'c']))
    assert np.array_equal(algs.quicksort(y)[0], np.array([1,2,2,3,8]))
    assert np.array_equal(algs.quicksort(z)[0], np.array([]))

def test_insertionsort():
    # reverse ordered list
    s = [11,10,9]

    # ordered list
    t = [9,10,11]

    # negative numbers
    u = [-1, -100, -30, -50, 20, 50, 61]

    # unordered list
    v = [1, 2, 8, 3]

    # one element list
    w = [5]

    # characters
    x = ['a', 'c', 'b']

    # duplicates
    y = [1, 2, 3, 8, 2]

    # empty array
    z = []

    # assert np.array_equal(algs.insertionsort(s)[0], np.array([9,10,11]))
    assert np.array_equal(algs.insertionsort(t)[0], np.array([9,10,11]))
    assert np.array_equal(algs.insertionsort(u)[0], np.array([-100,-50,-30,-1,20,50,61]))
    assert np.array_equal(algs.insertionsort(v)[0], np.array([1,2,3,8]))
    assert np.array_equal(algs.insertionsort(w)[0], np.array([5]))
    assert np.array_equal(algs.insertionsort(x)[0], np.array(['a', 'b', 'c']))
    assert np.array_equal(algs.insertionsort(y)[0], np.array([1,2,2,3,8]))
    assert np.array_equal(algs.insertionsort(z)[0], np.array([]))


