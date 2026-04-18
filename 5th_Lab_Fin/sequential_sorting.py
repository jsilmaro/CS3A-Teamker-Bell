import random
import time

# tutorialspoint
def sequential_bubble_sort(data):
    n = len(data)
    for i in range(n):
        swaps = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swaps = True
        
        if not swaps:
            break
    return data

# Dataset Generation
N = 100000 # 1000, 100000, 1000000
data = [random.randint(1, 1000000) for _ in range(N)]

print(f"Sorting {N} elements sequentially...\n")

# Performance Measurement
start = time.time()
sorted_data = sequential_bubble_sort(data)
end = time.time()

print(f"Sorted Array (first 10): {sorted_data[:10]}\n")
print(f"Sequential Execution Time: {end - start:.6f} seconds")
