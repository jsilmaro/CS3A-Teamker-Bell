📄 Reflection and Analysis
🌼 Charesh – Sequential Sorting Algorithm

In this task, I implemented a sequential sorting algorithm using Merge Sort, which follows a divide-and-conquer approach. The algorithm recursively splits the dataset into smaller parts, sorts them, and then merges them back together into a fully sorted list. When tested with a small dataset of 1,000 elements, the algorithm performed very efficiently, completing the sorting in 0.001658 seconds while producing a correct and fully sorted output.

As the dataset size increased, the execution time also increased, but remained manageable due to the efficiency of Merge Sort. For a medium dataset of 100,000 elements, the algorithm completed in 0.305667 seconds, and for a large dataset of 1,000,000 elements, it took 4.857920 seconds.

From this task, I learned that even within sequential execution, choosing an efficient algorithm like Merge Sort significantly improves performance and scalability.


🤍 Hannah – Parallel Sorting Algorithm

For this part, I implemented a parallel sorting algorithm by ...


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

For the parallel searching algorithm, I ...


