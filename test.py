import hybrid, quick, heap, radix_counting, insertion
import random

n = int(input('Enter size of array: '))

array_insertion = [random.randint(0, 200) for _ in range(n)]
array_heap = [random.randint(0, 200) for _ in range(n)]
array_hybrid = [random.randint(0, 200) for _ in range(n)]
array_radix = [random.randint(0, 200) for _ in range(n)]
array_quick = [random.randint(0, 200) for _ in range(n)]

sorted_insertion = sorted(array_insertion)
sorted_heap = sorted(array_heap)
sorted_hybrid = sorted(array_hybrid)
sorted_radix = sorted(array_radix)
sorted_quick = sorted(array_quick)

insertion.insertion_sort(array_insertion)
heap.heap_sort(array_heap)
hybrid.hybrid_sort(array_hybrid)
radix_counting.radix_sort(array_radix)
quick.quick_sort(array_quick, 0, len(array_quick)-1)

assert sorted_insertion == array_insertion, f'test failed'
assert sorted_heap == array_heap, f'test failed'
assert sorted_hybrid == array_hybrid, f'test failed'
assert sorted_radix == array_radix, f'test failed'
assert sorted_quick == array_quick, f'test failed'

print('All tests passed successfully')

