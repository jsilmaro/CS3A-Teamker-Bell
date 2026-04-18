📄 Reflection and Analysis
🌼 Charesh – Sequential Sorting Algorithm

In this task, I implemented a sequential sorting algorithm, where the data is processed step by step using a single control flow. Among the three dataset sizes, I observed that sequential sorting performs efficiently on small datasets due to its low overhead and straightforward execution. When testing with a small dataset of 1,000 elements, the algorithm performed efficiently and completed the sorting in 0.042834 seconds, producing a correctly sorted output. However, when I attempted to run the algorithm on a medium dataset of 100,000 elements, the program became extremely slow and has been stuck during execution. Because of this limitation, I was unable to proceed with testing the large dataset of 1,000,000 elements.

One challenge I encountered was dealing with the long execution time for larger inputs, which made it difficult to fully evaluate performance across all dataset sizes. In this activity, I learned that while sequential sorting is reliable and efficient for small datasets, it becomes impractical for larger workloads due to its lack of scalability and increasing execution time.


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


