import random
import time
from multiprocessing import Process, Queue

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

def worker_sort(chunk, queue):
    """Worker function to sort a chunk and put it in the queue."""
    # Using your sequential merge sort logic within the worker
    sorted_chunk = sequential_merge_sort(chunk)
    queue.put(sorted_chunk)

def sequential_merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = sequential_merge_sort(data[:mid])
    right = sequential_merge_sort(data[mid:])
    return merge(left, right)

if __name__ == "__main__":
    # 1. Dataset Generation
    N = 100000  
    data = [random.randint(1, 1000000) for _ in range(N)]
    
    print(f"Sorting {N} elements in parallel...\n")
    start = time.time()

    # 2. Partitioning (Remove the tags here)
    chunk_size = len(data) // 4 
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    # 3. Parallel Execution (Remove the tags here)
    queue = Queue() 
    processes = []
    
    for chunk in chunks:
        p = Process(target=worker_sort, args=(chunk, queue)) 
        processes.append(p)
        p.start()

    # 4. Collect Results
    sorted_chunks = []
    for _ in range(len(processes)):
        sorted_chunks.append(queue.get())
    
    for p in processes:
        p.join()

    # 5. Merging Results into a single globally sorted output
    # Merge the 4 sorted chunks back together [cite: 57]
    merged_1 = merge(sorted_chunks[0], sorted_chunks[1])
    merged_2 = merge(sorted_chunks[2], sorted_chunks[3])
    final_sorted = merge(merged_1, merged_2)

    end = time.time()
    print(f"Time taken (Parallel Merge Sort): {end - start:.6f} seconds")