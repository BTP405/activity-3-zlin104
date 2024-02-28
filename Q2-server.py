#Distributed Task Queue with Pickling:

#Create a distributed task queue system where tasks are sent from a client to multiple worker nodes for processing using sockets. 
#Tasks can be any Python function that can be pickled. Implement both the client and worker nodes. 
#The client sends tasks (pickled Python functions and their arguments) to available worker nodes, and each worker node executes the task and returns the result to the client.

#Requirements:
#Implement a protocol for serializing and deserializing tasks using pickling.
#Handle task distribution, execution, and result retrieval in both the client and worker nodes.
#Ensure fault tolerance and scalability by handling connection errors, timeouts, and dynamic addition/removal of worker nodes.

import socket
import pickle

def calculation(x):
    return x*2+1

def execute_task(server_socket):    
    while True: 
        client_socket, client_address = server_socket.accept()

        try:
            print("Connected to", client_address)

            # Receive the pickled task 
            pickled_task = client_socket.recv(1024)
            task = pickle.loads(pickled_task)

            function = task['function']
            args = task['args']
            result = function(*args)
            
            # Send the result back to the client 
            client_socket.sendall(str(result).encode())
            print("Task executed successfully, and result sent to the client.")
            
        except Exception as e:
            print(f"Failed to execute the task: {e}")
        
        finally: 
            # clean up the connection 
            client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # This is only one server, multiple servers(worker nodes) can be started to work with the client
    server_address = ('192.168.0.20', 12345)
    server_socket.bind(server_address)
    server_socket.listen(5)

    print("Server is listening for incoming connections...")
    execute_task(server_socket)
            
if __name__ == "__main__":
    main()
