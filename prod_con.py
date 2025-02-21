import threading
import time
import random
from queue import Queue

BUFFER_SIZE = 5


buffer = Queue(BUFFER_SIZE)

# Producer function
def producer(id):
    while True:
        item = random.randint(1, 100)  
        buffer.put(item)  
        print(f"Producer {id} produced item: {item}")
        time.sleep(random.uniform(0.5, 1.5))  

# Consumer function
def consumer(id):
    while True:
        item = buffer.get()  
        print(f"Consumer {id} consumed item: {item}")
        buffer.task_done()  
        time.sleep(random.uniform(0.5, 2.0))  

num_producers = 2
producer_threads = []

for i in range(num_producers):
    t = threading.Thread(target=producer, args=(i+1,))
    t.start()
    producer_threads.append(t)
   
    
    


num_consumers = 3
consumer_threads = []

for i in range(num_consumers):
    t = threading.Thread(target=consumer, args=(i+1,))
    t.start()
    consumer_threads.append(t)
    
    

for t in producer_threads + consumer_threads:
    t.join()
    




import threading
import time
import random
from queue import Queue

BUFFER_SIZE = 5
PRODUCE_LIMIT = 10  # Number of items to produce before stopping

buffer = Queue(BUFFER_SIZE)

# Producer function
def producer(id):
    for _ in range(PRODUCE_LIMIT):
        item = random.randint(1, 100)  
        buffer.put(item)
        print(f"Producer {id} produced item: {item}")
        time.sleep(random.uniform(0.5, 1.5))
    buffer.put(None)  # Send poison pill to stop consumers

# Consumer function
def consumer(id):
    while True:
        item = buffer.get()
        if item is None:  # Check for poison pill
            buffer.put(None)  # Pass poison pill to other consumers
            break
        print(f"Consumer {id} consumed item: {item}")
        buffer.task_done()
        time.sleep(random.uniform(0.5, 2.0))

num_producers = 2
producer_threads = []

for i in range(num_producers):
    t = threading.Thread(target=producer, args=(i+1,))
    t.start()
    producer_threads.append(t)

num_consumers = 3
consumer_threads = []

for i in range(num_consumers):
    t = threading.Thread(target=consumer, args=(i+1,))
    t.start()
    consumer_threads.append(t)

# Optional: Wait for producers to finish
for t in producer_threads:
    t.join()

# Optional: Wait for consumers to finish
for t in consumer_threads:
    t.join()
