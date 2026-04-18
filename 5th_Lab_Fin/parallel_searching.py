import multiprocessing as mp
import random
import time


def segment_search(segment, target, start_index, result_queue, stop_signal):

    for i, value in enumerate(segment):

        # Stop if another process already found target
        if stop_signal.is_set():
            return

        if value == target:
            result_queue.put(start_index + i)
            stop_signal.set()
            return


def parallel_search(data, target, workers=4):

    manager = mp.Manager()
    result_queue = manager.Queue()
    stop_signal = manager.Event()

    processes = []

    # Dynamic chunking strategy
    chunk_length = len(data) // workers

    for i in range(workers):

        start = i * chunk_length

        if i == workers - 1:
            end = len(data)
        else:
            end = start + chunk_length

        sub_array = data[start:end]

        p = mp.Process(
            target=segment_search,
            args=(sub_array, target, start, result_queue, stop_signal)
        )

        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    if not result_queue.empty():
        return result_queue.get()

    return -1


if __name__ == "__main__":

    SIZE = 100000
    data = [random.randint(1, 1000000) for _ in range(SIZE)]

    target = data[random.randint(0, SIZE - 1)]

    start_time = time.time()

    result = parallel_search(data, target, workers=4)

    end_time = time.time()

    if result != -1:
        print("Target found at index:", result)
    else:
        print("Target not found")

    print("Execution time:", end_time - start_time)