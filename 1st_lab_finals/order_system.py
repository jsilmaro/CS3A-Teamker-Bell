from mpi4py import MPI
import time
from multiprocessing import Manager, Lock, Process

def run_worker(rank, size, shared_orders, lock):
    comm = MPI.COMM_WORLD
    while True:
        order = comm.recv(source=0, tag=11)
        if order is None:
            break

        # Simulate processing delay
        delay = 1 + (rank * 0.5)
        print(f"  [Worker {rank}] Processing Order #{order['id']}: {order['item']} (will take {delay}s)")
        time.sleep(delay)

        # Store result in shared memory
        result = f"Order #{order['id']} ({order['item']}) - handled by Worker {rank}"
        with lock:
            shared_orders.append(result)
        print(f"  [Worker {rank}] ✔ Completed Order #{order['id']}: {order['item']}")

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    manager = Manager()
    shared_orders = manager.list()
    lock = Lock()

    if rank == 0:
        orders = [
            {"id": i + 1, "item": item}
            for i, item in enumerate([
                "Laptop", "Phone", "Tablet", "Monitor",
                "Keyboard", "Mouse", "Headset", "Webcam"
            ])
        ]

        num_workers = size - 1
        print(f"[Master] Generated {len(orders)} orders. Distributing to {num_workers} workers...\n")

        for i, order in enumerate(orders):
            destination = (i % num_workers) + 1
            comm.send(order, dest=destination, tag=11)
            print(f"[Master] Sent Order #{order['id']} ({order['item']}) → Worker {destination}")

        # Stop signals
        for w in range(1, size):
            comm.send(None, dest=w, tag=11)

        # Wait for workers to finish (barrier)
        comm.Barrier()

        print("\n[Master] ══════════ All Completed Orders ══════════")
        for entry in shared_orders:
            print(f"  ✅ {entry}")
        print(f"[Master] Total: {len(shared_orders)} orders processed.")

    else:
        run_worker(rank, size, shared_orders, lock)
        comm.Barrier()

if __name__ == "__main__":
    main()
