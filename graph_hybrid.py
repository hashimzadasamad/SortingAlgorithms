import matplotlib.pyplot as plt

# Read the data from the text file
with open('time_hybrid.txt', 'r') as file:
    data = file.readlines()

# Initialize lists to store data
sizes = []
insertion = []
heap = []
radix_counting = []
quick = []
hybrid = []

# Parse the data and filter for sizes between 1 and 500
for line in data[1:]:
    size, insertion_val, heap_val, radix_counting_val, quick_val, hybrid_val = map(int, line.split())

    # Check the size
    sizes.append(size)
    insertion.append(insertion_val)
    heap.append(heap_val)
    radix_counting.append(radix_counting_val)
    quick.append(quick_val)
    hybrid.append(hybrid_val)

# Plot the data
plt.figure(figsize=(15, 10))

# Plot hybrid and insertion
plt.plot(sizes, hybrid, label='Hybrid', marker='o', color='purple')
plt.plot(sizes, insertion, label='Insertion', marker='o', color='red')
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Hybrid vs Insertion Sort Comparison')
plt.legend()
plt.grid(True)
plt.savefig('output_hybrid_vs_insertion.jpg')
plt.show()

# Plot hybrid and quick
plt.figure(figsize=(15, 10))
plt.plot(sizes, hybrid, label='Hybrid', marker='o', color='purple')
plt.plot(sizes, quick, label='Quick', marker='o', color='orange')
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Hybrid vs Quick Sort Comparison')
plt.legend()
plt.grid(True)
plt.savefig('output_hybrid_vs_quick.jpg')
plt.show()

# Plot hybrid and radix counting
plt.figure(figsize=(15, 10))
plt.plot(sizes, hybrid, label='Hybrid', marker='o', color='purple')
plt.plot(sizes, radix_counting, label='Radix Counting', marker='o', color='green')
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Hybrid vs Radix_Counting Sort Comparison')
plt.legend()
plt.grid(True)
plt.savefig('output_hybrid_vs_radix_counting.jpg')
plt.show()

# Plot hybrid and heap
plt.figure(figsize=(15, 10))
plt.plot(sizes, hybrid, label='Hybrid', marker='o', color='purple')
plt.plot(sizes, heap, label='Heap', marker='o', color='blue')
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Hybrid vs Heap Sort Comparison')
plt.legend()
plt.grid(True)
plt.savefig('output_hybrid_vs_heap.jpg')
plt.show()
