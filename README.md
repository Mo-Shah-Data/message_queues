# message_queues

Make improvements to code where possible.
No coding for concurrency suggestions required just thoughts and ideas.
Think of idea for concurrency and brainstorm ideas on how to do this?
How can we make this concurrent, using concurrency in python?

Use Mockaroo to create mock data.
https://mockaroo.com/


Learn Clean code in own time.

Concurrency and Parallelism
https://learning.oreilly.com/course/concurrent-and-parallel/9781771375313/

Concurrency and Parallelism

Concurrency
For now, Handling Many tasks at the same time(or same time span).

Parallelism
for now, processing many tasks at the same time.

Two Classic Mechanisms for Concurrency: multiprocessing and multithreading.

I/O operations are usually the slowest. For this consider non-blocking I/O

JSON file example
Going through one main file will take longer than splitting the file and using different processors or cores to work on each file.
Process may need tracking and management. However, it will also be important to timestamp the changes to get the last one when comparing the latest update/change.

The difference between a process and thread.
A process is a program in execution(test.exe being run in windows command line)
A thread is a sequence of executable instructions within a process.
Every process has at least one thread, more than one means it is multithreaded.
Threads within a process share the same address space.


Multi-processing

Multi-Threading

Parallelism.

Next Steps:
Processing or Data Parallelism
Aim for data parallelism here
Generate more rows of data

Functional concurrency

Task 1:
Go through sequential file and create multiple processes
Task 2:
Split to chunks and process separate to eventually combine in one place.

Look into MapReduce, VSStudio code, set timer to se improvements.

Why is threading faster?


Threading Task

Use threading module

get 1,000,000 random numbers - an array

go through in a for loop and add them all together

initially just sum for the array

then split to two lots of 500,000 numbers and run in 2 threads and then join and sum

then split to two lots of 250,000 numbers and run in 4 threads

then 8 threads split into 8ths

then 16 threads

then 24 threads

Calculate time for each number of these options
Experiment with more or less data.

Visualize results/graph


