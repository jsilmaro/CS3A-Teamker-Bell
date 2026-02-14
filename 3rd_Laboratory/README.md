Analysis Questions
Provide concise but well-structured explanations.

1. Differentiate Task and Data Parallelism. Identify which part of the lab demonstrates each and justify the workload division.
- Task Parallelism executes different operations concurrently on the same data, while Data Parallelism applies the same operation concurrently to multiple data elements. In this lab, task-parallelism.py demonstrates Task Parallelism because separate deduction types (SSS, PhilHealth, Pag-IBIG, and Withholding Tax) are computed simultaneously for a single employee using ThreadPoolExecutor, meaning the workload is divided by task. On the other hand, data-parallelism.py demonstrates Data Parallelism because the same compute_payroll() function is applied to multiple employees using ProcessPoolExecutor, meaning the workload is divided by data, with each process handling a different employee.

2. Explain how concurrent.futures managed execution, including submit(), map(), and Future objects. Discuss the purpose of with when creating an Executor.
- The concurrent.futures module manages asynchronous execution where submit() schedules individual tasks returning Future objects, map() applies a function across iterable data in parallel, and the with statement ensures proper resource management and automatic shutdown of the executor.

3. Analyze ThreadPoolExecutor execution in relation to the GIL and CPU cores. Did true parallelism occur?
- ThreadPoolExecutor does not achieve true parallelism for CPU-bound tasks because of Python’s GIL, which allows only one thread to execute at a time. Threads run concurrently but not simultaneously across multiple CPU cores.

4. Explain why ProcessPoolExecutor enables true parallelism, including memory space separation and GIL behavior.
- ProcessPoolExecutor enables true parallelism because each process has its own memory space and its own GIL. This allows multiple processes to run simultaneously on different CPU cores.

5. Evaluate scalability if the system increases from 5 to 10,000 employees. Which approach scales better and why?
- Data Parallelism using ProcessPoolExecutor scales better for 10,000 employees because it distributes the workload across multiple CPU cores and avoids GIL limitations.

6. Provide a real-world payroll system example. Indicate where Task Parallelism and Data Parallelism would be applied, and which executor you would use.
- In a real-world payroll system, ThreadPoolExecutor would handle concurrent I/O-bound tasks like database or API calls for one employee, while ProcessPoolExecutor would compute payroll for thousands of employees in parallel using Data Parallelism.
