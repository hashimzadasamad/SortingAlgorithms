from insertion import insertion_sort
from quick import quick_sort

def hybrid_sort(array):
    if len(array) < 30:
        insertion_sort(array)
    else:
        quick_sort(array, 0, len(array)-1)
