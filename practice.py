# # Reader Writer

# import time
# import threading 
# import random

# data = 0
# read_count = 0

# mutex = threading.Lock()
# rw_mutex = threading.Lock()

# # Reader Function

# def reader(reader_id):
#     global read_count
#     while True:
#         time.sleep(random.uniform(0.5,2))

#         #Entry Section
#         mutex.acquire()
#         read_count += 1
#         if(read_count==1):
#             rw_mutex.acquire()
#         mutex.release()

#         # Critical Section
#         print(f"Reader {reader_id} is reading data: {data}")
#         time.sleep(random.uniform(0.5,1.5))

#         #exit section
#         mutex.acquire()
#         read_count -=1
#         if read_count==0:
#             rw_mutex.release()
#         mutex.release()

# # Writer function
# def writer(writer_id):
#     global data
#     while True:
#         time.sleep(random.uniform(1,3))

#         rw_mutex.acquire()

#         #Entry Section
#         data = data+1
#         print(f"Writer {writer_id} is writing data: {data}")
#         time.sleep(random.uniform(0.5,1.5))

#         rw_mutex.release()


# num_readers = 2
# num_writers = 1

# for i in range(num_readers):
#     threading.Thread(target=reader, args=(i+1,)).start()

# for i in range(num_writers):
#     threading.Thread(target=writer, args=(i+1,)).start()


# import threading
# import time
# import random

# data = 0
# read_count = 0

# mutex = threading.Lock()
# rw_mutex = threading.Lock()

# #Reader function
# def reader(reader_id):
#     global read_count
#     while True:
#         time.sleep(random.uniform(0.5,2))

#         #entry section
#         mutex.acquire()
#         read_count += 1
#         if read_count==1:
#             rw_mutex.acquire()
#         mutex.release()

#         # Critical Section
#         print(f"Reader {reader_id} is reading data: {data}")
#         time.sleep(random.uniform(0.5,1.5))

#         # Exit Section
#         mutex.acquire()
#         read_count-=1
#         if read_count==0:
#             rw_mutex.release()
#         mutex.release()

# # Writer function
# def writer(writer_id):
#     global data
#     while True:
#         time.sleep(random.uniform(1,2))

#         #Entry section
#         rw_mutex.acquire()

#         #critical section
#         data += 1
#         print(f"Writer {writer_id} is writing data: {data}")
#         time.sleep(random.uniform(0.5,1.5))

#         rw_mutex.release() 

# num_readers = 3
# num_writers = 2

# for i in range(num_readers):
#     threading.Thread(target=reader,args=(i+1,)).start()

# for i in range(num_writers):
#     threading.Thread(target=writer,args=(i+1,)).start()



# import threading
# import time
# import random

# data = 0
# read_count = 0

# mutex = threading.Lock()
# rw_mutex = threading.Lock()

# def reader(reader_id):
#     global read_count
#     while True:
#         time.sleep(random.uniform(0.5,2))

#         # Entry section
#         mutex.acquire()
#         read_count += 1
#         if read_count==1:
#             rw_mutex.acquire()
#         mutex.release()

#         # Critical section
#         print(f"Reader {reader_id} is reading data: {data}")
#         time.sleep(random.uniform(0.5,1.5))

#         #Exit Section
#         mutex.acquire()
#         read_count -= 1
#         if read_count == 0:
#             rw_mutex.release()
#         mutex.release()


# def writer(writer_id):
#     global data
#     while True:
#         time.sleep(random.uniform(1,3))

#         #entry section
#         rw_mutex.acquire()

#         #critical section
#         data+=1
#         print(f"Writer {writer_id} is writing data: {data}")
#         time.sleep(random.uniform(0.5,1.5))

#         # Exit Section
#         rw_mutex.release()


# num_readers = 3
# num_writers = 2

# for i in range(num_readers):
#     threading.Thread(target=reader,args=(i+1,)).start()

# for i in range(num_writers):
#     threading.Thread(target=writer, args=(i+1,)).start()



# import threading
# import time
# import random

# read_count = 0
# data = 0

# mutex = threading.Lock()
# rw_mutex = threading.Lock()
# write_priority = threading.Semaphore(1)


# # Reader Function
# def reader(reader_id):
#     global read_count
#     while True:
#         time.sleep(random.uniform(0.5,2))

#         # entry section
#         write_priority.acquire()
#         mutex.acquire()
#         read_count +=1
#         if read_count == 1:
#             rw_mutex.acquire()
#         mutex.release()
#         write_priority.release()


#         # Critical Section
#         print(f"Reader {reader_id} is reading data: {data}")
#         time.sleep(random.uniform(0.5,1.5))

#         # Exit section
#         mutex.acquire()
#         read_count -=1
#         if read_count == 0:
#             rw_mutex.release()
#         mutex.release()


# # Writer Function

# def writer(writer_id):
#     global data
#     while True:
#         time.sleep(random.uniform(1,3))

#         # Entry Section
#         write_priority.acquire()
#         rw_mutex.acquire()
        

#         # Critical Secction
#         data += 1
#         print(f'Writer {writer_id} is writing data: {data}')
#         time.sleep(random.uniform(0.5,1.5))


#         # Exit Section
#         rw_mutex.release()
#         write_priority.release()



# num_readers = 3
# num_writers = 2


# for i in range(num_readers):
#     threading.Thread(target=reader, args=(i+1,)).start()

# for i in range(num_writers):
#     threading.Thread(target=writer,args=(i+1,)).start()



# import threading
# import time
# import random
# from queue import Queue

# BUFFER_SIZE = 5

# buffer = Queue(BUFFER_SIZE)

# # PRODUCER FUNCTION

# def producer(id):
#     while True:
#         item = random.randint(1,100)
#         buffer.put(item)
#         print(f"Producer {id} produced item: {item}")
#         time.sleep(random.uniform(0.5,1.5))

# # Consumer function

# def consumer(id):
#     while True:
#         item = buffer.get()
#         print(f"Consumer {id} consumed item {item}")
#         buffer.task_done()
#         time.sleep(random.uniform(0.5,2))


# num_prod = 2
# prod_thread = []

# for i in range(num_prod):
#     t = threading.Thread(target=producer,args=(i+1,))
#     t.start()
#     prod_thread.append(t)




# num_con = 3
# con_thread = []

# for i in range(num_con):
#     t = threading.Thread(target=consumer,args=(i+1,))
#     t.start()
#     con_thread.append(t)

# for t in prod_thread + con_thread:
#     t.join()


from queue import PriorityQueue

class Process:
    def __init__(self,pid,arrival_time,burst_time,priority):
        self.pid=pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.completion_time = 0

def fcfs(processes):
    time = 0
    for process in sorted(processes, key=lambda x: x.arrival_time):
        if time < process.arrival_time:
            time = process.arrival_time
        process.waiting_time = time - process.arrival_time
        time += process.burst_time
        process.completion_time = time
        process.turnaround_time = process.waiting_time + process.burst_time
    print("Results: ")
    print_res(processes)


def sjf_preemptive_scheduling(processes):
    time = 0
    comp = []
    pq = PriorityQueue()

    while processes or not pq.empty():
        while processes and processes[0].arrival_time <= time:
            process = processes.pop(0)
            pq.put((process.remaining_time,process.arrival_time,process))

        if not pq.empty():
            process = pq.get()[2]
            time +=1 
            process.remaining_time -= 1

            if process.remaining_time == 0:
                process.completion_time = time
                process.turnaround_time = process.completion_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
                comp.append(process)
            else:
                pq.put((process.remaining_time,process.arrival_time,process))
        else:
            time+=1

    print("resluts: ")
    print_res(comp)



def print_res(processes):
    print("PID\tArrival\tBurst\tPriority\tWaiting\tTurnaround")
    for p in sorted(processes, key=lambda x:x.pid):
        print(f"{p.pid} \t {p.arrival_time} \t {p.burst_time} \t {p.priority} \t\t {p.waiting_time}")

processes = [
    Process(1,2,4,1),
    Process(2,3,1,2),
    Process(3,1,3,4),
    Process(4,2,4,1)
]


print("FCFS ka res")
fcfs([Process(p.pid,p.arrival_time,p.burst_time,p.priority) for p in processes])

print("SJF ka result: ")
sjf_preemptive_scheduling([Process(p.pid,p.arrival_time,p.burst_time,p.priority) for p in processes])