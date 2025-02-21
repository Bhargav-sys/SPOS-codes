from queue import PriorityQueue

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def fcfs_scheduling(processes):
    time = 0
    for process in sorted(processes, key=lambda x: x.arrival_time):
        if time < process.arrival_time:
            time = process.arrival_time
        process.waiting_time = time - process.arrival_time
        time += process.burst_time
        process.completion_time = time
        process.turnaround_time = process.burst_time + process.waiting_time
    print("FCFS Scheduling Results:")
    print_results(processes)

def sjf_preemptive_scheduling(processes):
    time = 0
    pq = PriorityQueue()
    completed = []
    
    while processes or not pq.empty():
        while processes and processes[0].arrival_time <= time:
            process = processes.pop(0)
            pq.put((process.remaining_time, process.arrival_time, process))
        
        if not pq.empty():
            process = pq.get()[2]
            time += 1
            process.remaining_time -= 1
            
            if process.remaining_time == 0:
                process.completion_time = time
                process.turnaround_time = process.completion_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
                completed.append(process)
            else:
                pq.put((process.remaining_time, process.arrival_time, process))
        else:
            time += 1
    
    print("SJF Preemptive Scheduling Results:")
    print_results(completed)

def priority_scheduling(processes):
    time = 0
    completed_processes = []
    
    while processes:
        arrived_processes = [p for p in processes if p.arrival_time <= time]
        if arrived_processes:
            process = min(arrived_processes, key=lambda p: p.priority)
            processes.remove(process)
            if time < process.arrival_time:
                time = process.arrival_time
            process.waiting_time = time - process.arrival_time
            time += process.burst_time
            process.completion_time = time
            process.turnaround_time = process.burst_time + process.waiting_time
            completed_processes.append(process)
        else:
            time += 1
    
    print("Priority Scheduling Results:")
    print_results(completed_processes)

def round_robin_scheduling(processes, quantum):
    time = 0
    queue = [p for p in sorted(processes, key=lambda x: x.arrival_time)]
    
    while queue:
        process = queue.pop(0)
        if time < process.arrival_time:
            time = process.arrival_time
        execute_time = min(quantum, process.remaining_time)
        time += execute_time
        process.remaining_time -= execute_time
        
        if process.remaining_time == 0:
            process.completion_time = time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
        else:
            queue += [p for p in processes if p.arrival_time <= time and p not in queue and p.remaining_time > 0]
            queue.append(process)
    
    print("Round Robin Scheduling Results:")
    print_results(processes)

def print_results(processes):
    print("PID\tArrival\tBurst\tPriority\tWaiting\tTurnaround")
    for p in sorted(processes, key=lambda x: x.pid):
        print(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.priority}\t\t{p.waiting_time}\t\t{p.turnaround_time}")
    avg_waiting_time = sum(p.waiting_time for p in processes) / len(processes)
    avg_turnaround_time = sum(p.turnaround_time for p in processes) / len(processes)
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}\n")

# Example usage:
processes = [
    Process(pid=1, arrival_time=2, burst_time=8, priority=2),
    Process(pid=2, arrival_time=1, burst_time=4, priority=1),
    Process(pid=3, arrival_time=3, burst_time=9, priority=3),
    Process(pid=4, arrival_time=2, burst_time=5, priority=2)
]

print("Simulating FCFS Scheduling:")
fcfs_scheduling([Process(p.pid, p.arrival_time, p.burst_time, p.priority) for p in processes])

print("Simulating SJF (Preemptive) Scheduling:")
sjf_preemptive_scheduling([Process(p.pid, p.arrival_time, p.burst_time, p.priority) for p in processes])

print("Simulating Priority Scheduling:")
priority_scheduling([Process(p.pid, p.arrival_time, p.burst_time, p.priority) for p in processes])

print("Simulating Round Robin Scheduling with Quantum = 3:")
round_robin_scheduling([Process(p.pid, p.arrival_time, p.burst_time, p.priority) for p in processes], quantum=3)


