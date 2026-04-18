



Sequential_searching: by Jeranch Quibra

​I implemented a sequential binary search to serve as the baseline for our performance testing.
Since this is a sequential algorithm it operates on a single control flow. It executes one operation 
at a time without any concurrency. This approach provided a very predictable and deterministic execution path.
Determinism is a key characteristic of the sequential model described in our activity.  

​In terms of performance the implementation showed almost zero overhead. It avoids the costs associated 
with process creation and synchronization required in parallel models. While it was fast for the 1000 element
dataset the limitations of being bound to a single CPU core became evident with the 1000000 element dataset. 
This highlighted the trade-off mentioned in the documentation where sequential algorithms are often better for
small workloads. Parallelism becomes beneficial only when the computational workload outweighs coordination costs.  
