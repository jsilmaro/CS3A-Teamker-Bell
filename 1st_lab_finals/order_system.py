from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

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

    # Collect results from workers via MPI
    completed_orders = []
    for _ in range(len(orders)):
        result = comm.recv(source=MPI.ANY_SOURCE, tag=22)
        completed_orders.append(result)

    print("\n[Master] ══════════ All Completed Orders ══════════")
    for entry in sorted(completed_orders):
        print(f"  ✅ {entry}")
    print(f"[Master] Total: {len(completed_orders)} orders processed.")

else:
    while True:
        order = comm.recv(source=0, tag=11)
        if order is None:
            break

        delay = 1 + (rank * 0.5)
        print(f"  [Worker {rank}] Processing Order #{order['id']}: {order['item']} (delay: {delay}s)")
        time.sleep(delay)
        print(f"  [Worker {rank}] ✔ Completed Order #{order['id']}: {order['item']}")

        # Send result back to master
        result = f"Order #{order['id']} ({order['item']}) - handled by Worker {rank}"
        comm.send(result, dest=0, tag=22)