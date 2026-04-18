import random
import time

def merge(left, right):
    result = []
    i = j = 0
    # Compare elements from both lists and merge them in order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Add any remaining elements
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

# --- Execution ---
N = 1000
data = [random.randint(1, 1000000) for _ in range(N)]

start = time.time()
sorted_data = sequential_merge_sort(data)
end = time.time()

print(f"Time taken (Sequential Merge Sort): {end - start:.6f} seconds")
