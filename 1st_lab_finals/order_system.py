from mpi4py import MPI

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

else:
    while True:
        order = comm.recv(source=0, tag=11)
        if order is None:
            break
        print(f"  [Worker {rank}] Handling Order #{order['id']}: {order['item']}")