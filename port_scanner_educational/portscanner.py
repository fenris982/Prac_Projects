import socket
import threading
from queue import Queue

target = '192.168.0.1' #<<< Target IP Address
queue = Queue() #<<< Variable to define an empty Queue
open_ports = [] #<<< Empty list to append open ports

#Port Scan function takes in port as an argument. Creats a INTERNET socket with and connects to the target IP defined above and the port passed as an arg.
def port_scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

#Fills a list for the queue fucntion to take in a list of all the ports you want to scan. Linked to the port list at line 31
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

#Worker function is our scanner. It checks if the queue is empty and if it isnt will scan the port, append it a list and print the formatted string to the output.        
def worker():
    while not queue.empty():
        port = queue.get()
        if port_scan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)
            
#Port list for the ports i want to scan. fill_queue adds this to the queue = Queue() at line 6            
port_list = range (1, 65536)
fill_queue(port_list)

#empty thread list so that i can "join" threads to ensure that all threads are complete before print is done. Links to the for loop at line 45
thread_list = []

#for loop defines how many threads will be operating. In this case "100".It targets the worker function but does not call it.
#It then adds them to the thread_list empty list at line 36
for t in range(500):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

#Starts all of the threads that are in the thread list at line 36
for thread in thread_list:
    thread.start()

# joins the threads so that all threads start and finish at the same time.    
for thread in thread_list:
    thread.join()
    
print("Open ports are: ", open_ports)