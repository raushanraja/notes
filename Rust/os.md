### Operating System Fundamentals

## Basic Overview
```
                            +------------------------+
                            |        Operating       |
                            |       System (OS)      |
                            +------------------------+
                                        |
                                        |
                               +------------------+
                               | Program          |
                               | (Application)    |
                               +------------------+
                                        |
                               +------------------+
                               | Process          |
                               | (Instance of     |
                               |  a Program)      |
               +------------------------+-------------------+  
               |                        |                   |
               |                        |                   |
            +-------+-------+-------+ +-------+-------+-------+------+
            | Thread 1         | Thread 2         | Thread 3         |
            | (Execution Unit  | (Execution Unit  | (Execution Unit  |
            |  within Process) |  within Process) |  within Process) |
            +------------------+------------------+------------------+
```
**Processes and Threads:**
- Processes represent instances of programs running on a computer, while threads are smaller units of execution within a process.
- Processes have their own memory space, while threads share memory within a process.

**Process States and Lifecycle:**
- Processes transition through states like start, ready, running, waiting, and terminated.
- The operating system uses Process Control Blocks (PCBs) to manage processes.

**Process Creation and Termination:**
- Processes are created using system calls like exec() and fork().
- Orphan processes are adopted by the init process in Unix-like systems.

**Threads:**
- Threads are smaller units of execution within a process, sharing memory and resources.
- Multithreading allows concurrent execution within a single process.

**Process vs Threads:**
- Processes have separate memory spaces, while threads share memory within a process.
- Threads are lightweight compared to processes.

**Process Scheduling:**
- Schedulers manage process execution, including long-term, short-term, and medium-term scheduling.
- Scheduling algorithms aim to maximize CPU utilization and system performance.

**Process Synchronization:**
- Process synchronization prevents race conditions and ensures data consistency.
- Techniques like semaphores and mutexes are used for synchronization.

**Deadlocks and Starvation:**
- Deadlocks occur when processes are stuck due to cyclical dependencies.
- Starvation is when a process is unable to progress due to resource blocking.

**Handling Deadlocks:**
- Deadlocks can be detected and recovered using techniques like process termination or resource preemption.

**Conclusion:**
Understanding operating system fundamentals like processes, threads, synchronization, and scheduling is crucial for building efficient and reliable software systems.
