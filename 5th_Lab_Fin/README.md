📄 Reflection and Analysis
🌼 Charesh – Sequential Sorting Algorithm

In this task, I implemented a sequential sorting algorithm using Merge Sort, which follows a divide-and-conquer approach. The algorithm recursively splits the dataset into smaller parts, sorts them, and then merges them back together into a fully sorted list. When tested with a small dataset of 1,000 elements, the algorithm performed very efficiently, completing the sorting in 0.001658 seconds while producing a correct and fully sorted output.

As the dataset size increased, the execution time also increased, but remained manageable due to the efficiency of Merge Sort. For a medium dataset of 100,000 elements, the algorithm completed in 0.305667 seconds, and for a large dataset of 1,000,000 elements, it took 4.857920 seconds.

From this task, I learned that even within sequential execution, choosing an efficient algorithm like Merge Sort significantly improves performance and scalability.


🤍 Hannah – Parallel Sorting Algorithm

For this part, I implemented a parallel sorting algorithm by utilizing multiple processes. The dataset was divided into smaller chunks, and each chunk was sorted independently using separate processes. After all chunks were sorted, the results were merged to produce a single fully sorted output.

From this task, I learned that even in sequential execution, selecting an efficient algorithm such as Merge Sort significantly improves performance and scalability. I also observed that while execution time naturally grows with dataset size, a well-designed algorithm can still handle large inputs effectively without excessive performance degradation.

👤 Jeranch – Sequential Searching Algorithm

​I implemented a sequential binary search to serve as the baseline for our performance testing.
Since this is a sequential algorithm it operates on a single control flow. It executes one operation 
at a time without any concurrency. This approach provided a very predictable and deterministic execution path.
Determinism is a key characteristic of the sequential model described in our activity.  

​In terms of performance the implementation showed almost zero overhead. It avoids the costs associated 
with process creation and synchronization required in parallel models. While it was fast for the 1000 element
dataset the limitations of being bound to a single CPU core became evident with the 1000000 element dataset. 
This highlighted the trade-off mentioned in the documentation where sequential algorithms are often better for
small workloads. Parallelism becomes beneficial only when the computational workload outweighs coordination costs.  


🪻 Janelle – Parallel Searching Algorithm

For the parallel searching algorithm, I used a multiprocessing linear search that split the dataset into smaller pieces and had different processes search them at the same time. Instead of checking elements one by one like a sequential search, each process worked on its own segment. I tried it out on a randomly generated dataset with 100,000 elements, and it found the target correctly while keeping the global index right. It was hard to make sure that the right index was returned by coordinating results between processes.

Overall, parallel searching made performance better on larger datasets by using more CPU cores. However, it also added overhead from creating and syncing processes, which made it less efficient for smaller inputs.


