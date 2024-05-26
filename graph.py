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

# Plot insertion, heap, and quick on the same y-axis
plt.plot(sizes, insertion, label='Insertion', marker='o', color='red')
plt.plot(sizes, heap, label='Heap', marker='o', color='blue')
plt.plot(sizes, quick, label='Quick', marker='o', color='orange')
plt.plot(sizes, radix_counting, label='Radix Counting', marker='o', color='green')
plt.plot(sizes, hybrid, label='Hybrid', marker='o', color='purple')


# Add labels and title
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Sorting Algorithms Comparison with Random but Sorted Arrays')
plt.legend()
plt.grid(True)

# Save the plot as a JPG file
plt.savefig('output_hybrid.jpg')

# Show the plot
plt.show()

