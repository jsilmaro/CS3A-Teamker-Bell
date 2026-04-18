📄 Reflection and Analysis
🌼 Charesh – Sequential Sorting Algorithm

In this task, I implemented a sequential sorting algorithm, where ...

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


