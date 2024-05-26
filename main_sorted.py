import random, timeit
import insertion, heap, radix_counting, quick

x = 1
repeat = 100
with open('time_sorted.txt', 'a') as file:
    file.write('size   insertion    heap   radix_counting   quick\n')
    while x < 1001:
        for z in range(1, 10):
            size = x * z

            time_passed_insertion = 0
            time_passed_heap = 0
            time_passed_radix = 0
            time_passed_quick = 0

            for _ in range(repeat):
                array = [random.randint(0, 1000000) for _ in range(size)]
                array = sorted(array)
                current_time_insertion = timeit.timeit(lambda: insertion.insertion_sort(array[:]), number=1) * 1e9
                current_time_heap = timeit.timeit(lambda: heap.heap_sort(array[:]), number=1) * 1e9
                current_time_radix = timeit.timeit(lambda: radix_counting.radix_sort(array[:]), number=1) * 1e9
                current_time_quick = timeit.timeit(lambda: quick.quick_sort(array[:],0, len(array)-1), number=1) * 1e9

                time_passed_insertion += current_time_insertion
                time_passed_heap += current_time_heap
                time_passed_radix += current_time_radix
                time_passed_quick += current_time_quick

            time_passed_insertion /= repeat
            time_passed_heap /= repeat
            time_passed_radix /= repeat
            time_passed_quick /= repeat

            file.write(f'{size}       {int(time_passed_insertion)}       {int(time_passed_heap)}        {int(time_passed_radix)}       {int(time_passed_quick)}\n')


        x *= 10


