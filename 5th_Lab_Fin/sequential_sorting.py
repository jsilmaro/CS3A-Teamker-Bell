import random
import time

#MergeSort
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def sequential_merge_sort(data):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    left = sequential_merge_sort(data[:mid])
    right = sequential_merge_sort(data[mid:])
    
    return merge(left, right)

# Dataset Generation
N = 1000 # 1000, 100000, 1000000
data = [random.randint(1, 1000000) for _ in range(N)]

# Performance Measurement
start = time.time()
sorted_data = sequential_merge_sort(data)
end = time.time()

print(f"Time taken (Sequential Merge Sort): {end - start:.6f} seconds")
