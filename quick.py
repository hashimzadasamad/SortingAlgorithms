def quick_sort(array, low, high):
  while low < high:
    pivot = partition(array, low, high)

    if pivot - low < high - pivot:
      quick_sort(array, low, pivot - 1)
      low = pivot + 1
    else:
      quick_sort(array, pivot + 1, high)
      high = pivot - 1


def partition(array, low, high):
  pivot = array[high]
  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      array[i], array[j] = array[j], array[i]

  array[i + 1], array[high] = array[high], array[i + 1]
  return i + 1

