class MemoryBlock:
    def __init__(self, size):
        self.size = size
        self.remaining_size = size

    def reset(self):
        self.remaining_size = self.size

class Process:
    def __init__(self, pid, size):
        self.pid = pid
        self.size = size
        self.allocated_block = None

    def reset(self):
        self.allocated_block = None

def first_fit(processes, memory_blocks):
    for process in processes:
        for block in memory_blocks:
            if block.remaining_size >= process.size:
                allocate(process, block)
                break

def best_fit(processes, memory_blocks):
    for process in processes:
        best_block = None
        for block in memory_blocks:
            if block.remaining_size >= process.size:
                if not best_block or block.remaining_size < best_block.remaining_size:
                    best_block = block
        if best_block:
            allocate(process, best_block)

def worst_fit(processes, memory_blocks):
    for process in processes:
        worst_block = None
        for block in memory_blocks:
            if block.remaining_size >= process.size:
                if not worst_block or block.remaining_size > worst_block.remaining_size:
                    worst_block = block
        if worst_block:
            allocate(process, worst_block)



def allocate(process, block):
    process.allocated_block = block
    block.remaining_size -= process.size
    

def print_allocation(processes):
    print("\nProcess Allocation Results:")
    for process in processes:
        if process.allocated_block:
            print(f"Process {process.pid} allocated to Block with Remaining Size {process.allocated_block.remaining_size }")
        else:
            print(f"Process {process.pid} could not be allocated.")

def reset_memory_and_processes(processes, memory_blocks):
    for process in processes:
        process.reset()
    for block in memory_blocks:
        block.reset()

# Example usage
memory_blocks = [MemoryBlock(100), MemoryBlock(500), MemoryBlock(200), MemoryBlock(300), MemoryBlock(600)]
processes = [Process(1, 212), Process(2, 417), Process(3, 112), Process(4, 426)]


print("First Fit Allocation:")
first_fit(processes, memory_blocks)
print_allocation(processes)

print("\nBest Fit Allocation:")
reset_memory_and_processes(processes, memory_blocks)
best_fit(processes, memory_blocks)
print_allocation(processes)

print("\nWorst Fit Allocation:")
reset_memory_and_processes(processes, memory_blocks)
worst_fit(processes, memory_blocks)
print_allocation(processes)

