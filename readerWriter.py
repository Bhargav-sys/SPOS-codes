import threading
import time
import random

data = 0
read_count = 0

mutex  = threading.Lock()
rw_mutex = threading.Lock()

# Reader Function
def reader(reader_id):
    global read_count
    while True:
        time.sleep(random.uniform(0.5,2))

        #Entry Section
        mutex.acquire()
        read_count += 1
        if read_count == 1:
            rw_mutex.acquire()
        mutex.release()

        # Critical section
        print(f"Reader {reader_id} is reading data: {data} ")
        time.sleep(random.uniform(0.5,1.5))

        # Exit Section
        mutex.acquire()
        read_count-=1
        if read_count==0:
            rw_mutex.release()
        mutex.release()
    

# Writer Function
def writer(writer_id):
    global data
    while True:
        time.sleep(random.uniform(1,3))

        #Entry Section
        rw_mutex.acquire()

        #Critical Section 
        data +=1
        print(f"Writer {writer_id} is writing data: {data}")
        time.sleep(random.uniform(0.5,1.5))

        rw_mutex.release()



num_readers = 2
num_writers = 1

for i in range(num_readers):
    threading.Thread(target=reader, args=(i+1,)).start()


for i in range(num_writers):
    threading.Thread(target=writer,args=(i+1,)).start()
   
 












# Second Reader Writer 


mutex = threading.Lock()           
rw_mutex = threading.Lock()       
write_priority = threading.Semaphore(1)  
# Reader function (Writer Priority)
def reader(reader_id):
    global read_count
    while True:
        time.sleep(random.uniform(0.5, 2)) 

        # Entry section
        write_priority.acquire()
        mutex.acquire()
        read_count += 1
        if read_count == 1:  
            rw_mutex.acquire()
        mutex.release()
        write_priority.release()

        # Critical section (Reading)
        print(f"Reader {reader_id} is reading data: {data}")
        time.sleep(random.uniform(0.5, 1.5))  

        # Exit section
        mutex.acquire()
        read_count -= 1
        if read_count == 0:  
            rw_mutex.release()
        mutex.release()


#writer function

def writer(writer_id):
    global data
    while True:
        time.sleep(random.uniform(1,3))


        #entry section
        write_priority.acquire()
        rw_mutex.acquire()

        #critical section
        data+=1
        print(f"Writer {writer_id} is writing data: {data}")
        time.sleep(random.uniform(0.5,1.5))

        #exit section
        rw_mutex.release()
        write_priority.release()

num_readers = 3
num_writers = 2


for i in range(num_readers):
    threading.Thread(target=reader, args=(i+1,)).start()

for i in range(num_writers):
    threading.Thread(target=writer, args=(i+1,)).start()