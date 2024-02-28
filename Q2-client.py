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


def send_task(task_info, worder_nodes):
    try:
        for node in worder_nodes:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            client_socket.connect(node)

            # Pickle the task dictionary
            pickled_task = pickle.dumps(task_info)

            # Send the pickled task
            client_socket.sendall(pickled_task)
            print("Task sent successfully to:", node)

            # Receive the acknowledgment from the server
            receive_data = client_socket.recv(1024)
            print(f"Result received from {node}: {receive_data.decode()}", )

    except Exception as e:
        print(f"Failed to send the task: {e}")

    finally:
        # Clean up the connection
        client_socket.close()

def main():
    # Define the task by using dictionary, so the function and args can be stored separately
    task_info = {'function': calculation, 'args': (3,)}

    # Define a list of worder nodes
    worker_nodes = [('192.168.0.20', 12345), ('192.168.0.20', 12346)]

    send_task(task_info, worker_nodes)

if __name__ == "__main__":
    main()
