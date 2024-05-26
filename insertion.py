def insertion_sort(array):
    for i in range(1, len(array)):
        valid = array[i]
        k = i
        while k > 0 and array[k-1] > valid:
            array[k] = array[k-1]
            k -= 1
        array[k] = valid
