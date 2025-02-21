def fifo(pages, capacity):
    memory = []
    page_faults = 0
    
    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
        print(f"Page: {page}, Memory: {memory}")
    
    print(f"Total Page Faults (FIFO): {page_faults}\n")

def lru(pages, capacity):
    memory = []
    page_faults = 0
    recent_usage = {}
    
    for i, page in enumerate(pages):
        if page not in memory:
            page_faults += 1
            if len(memory) < capacity:
                memory.append(page)
            else:
                lru_page = min(memory, key=lambda p: recent_usage[p])
                memory.remove(lru_page)
                memory.append(page)
        recent_usage[page] = i
        print(f"Page: {page}, Memory: {memory}")
    
    print(f"Total Page Faults (LRU): {page_faults}\n")

def optimal(pages, capacity):
    memory = []
    page_faults = 0
    
    for i, page in enumerate(pages):
        if page not in memory:
            page_faults += 1
            if len(memory) < capacity:
                memory.append(page)
            else:
                farthest_page, farthest_index = -1, -1
                for m in memory:
                    try:
                        next_use = pages[i+1:].index(m)
                    except ValueError:
                        next_use = float('inf')
                    if next_use > farthest_index:
                        farthest_index, farthest_page = next_use, m
                memory.remove(farthest_page)
                memory.append(page)
        print(f"Page: {page}, Memory: {memory}")
    
    print(f"Total Page Faults (Optimal): {page_faults}\n")

# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
capacity = 3

# print("FIFO Algorithm:")
# fifo(pages, capacity)

print("LRU Algorithm:")
lru(pages, capacity)

# print("Optimal Algorithm:")
# optimal(pages, capacity)
