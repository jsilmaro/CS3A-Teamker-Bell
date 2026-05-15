from mpi4py import MPI
import time
from multiprocessing import Manager

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

manager = Manager()
shared_orders = manager.list()

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

    for w in range(1, size):
        comm.send(None, dest=w, tag=11)

    comm.Barrier()

    print("\n[Master - NO LOCK] Final list (may be incomplete or inconsistent):")
    for entry in shared_orders:
        print(f"  {entry}")
    print(f"Total: {len(shared_orders)} orders processed.")

else:
    while True:
        order = comm.recv(source=0, tag=11)
        if order is None:
            break
        time.sleep(0.5)
        # No lock — race condition possible
        shared_orders.append(f"Order #{order['id']} ({order['item']}) - Worker {rank}")
        print(f"  [Worker {rank}] ✔ Done: {order['item']}")

    comm.Barrier()