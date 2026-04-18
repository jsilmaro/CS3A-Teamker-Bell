import time
import random

def search_sequential(data, target):
    low = 0
    high = len(data) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

N = 1000000 
data = sorted([random.randint(1, 1000000) for _ in range(N)])
target = data[random.randint(0, N-1)]

start = time.time()
result = search_sequential(data, target)
end = time.time()

print(f"Index: {result}")
print(f"Time: {end - start:.8f}")
