# Distributed Order Processing

## Reflection Questions

### 1. How did you distribute orders among worker processes?
The master process (rank 0) generated a list of 8 orders and distributed them
to worker processes using `comm.send()` in a round-robin pattern. Each order
was assigned using `destination = (i % num_workers) + 1`, spreading orders
evenly across workers 1, 2, and 3.

### 2. What happens if there are more orders than workers?
Workers receive multiple orders. Each worker loops with `comm.recv()` until it
receives a `None` sentinel signal from the master, meaning it keeps processing
additional orders assigned to it before stopping.

### 3. How did processing delays affect the order completion?
Workers completed orders in a non-deterministic order since each had a different
sleep duration (1.5s, 2.0s, 2.5s). Faster workers finished their orders first
and the final list reflects completion order, not submission order. This mirrors
real-world distributed systems where task completion is unpredictable.

### 4. How did you implement shared memory, and where was it initialized?
We initially attempted `Manager().list()` from Python's `multiprocessing` module,
but it does not work across MPI process boundaries in Codespaces. We instead used
MPI's own message passing — workers send completed results back to the master via
`comm.send()` with tag 22, and the master collects them with `comm.recv()`.

### 5. What issues occurred when multiple workers wrote to shared memory simultaneously?
Without synchronization, the `Manager().list()` showed 0 orders processed despite
all workers completing their tasks. This is a race condition — concurrent writes
across MPI boundaries caused all appended data to be lost, demonstrating why
synchronization is critical in distributed systems.

### 6. How did you ensure consistent results when using multiple processes?
We replaced shared memory with MPI-based result collection. Each worker sends its
completed order back to the master using `comm.send()`, and the master collects
exactly `len(orders)` results using `comm.recv(source=MPI.ANY_SOURCE)`. This
guarantees a complete and consistent final list every time.