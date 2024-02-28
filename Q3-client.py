#Real-Time Chat Application with Pickling:

#Develop a simple real-time chat application where multiple clients can communicate with each other via a central server using sockets. 
#Messages sent by clients should be pickled before transmission. The server should receive pickled messages, unpickle them, and broadcast them to all connected clients.


#Requirements:
#Implement separate threads for handling client connections and message broadcasting on the server side.
#Ensure proper synchronization to handle concurrent access to shared resources (e.g., the list of connected clients).
#Allow clients to join and leave the chat room dynamically while maintaining active connections with other clients.
#Use pickling to serialize and deserialize messages exchanged between clients and the server.

import socket
import threading
import pickle

def send_message(client_socket):
    try:
        while True:
            message = input("Enter your message: ")
            if message.lower() == 'exit':
                break
            
            pickled_message = pickle.dumps(message)
            client_socket.sendall(pickled_message)
            
    except:
        pass


def receive_message(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            message = pickle.loads(data)
            print(message)

    except:
        pass

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server_address = ('192.168.0.20', 12345) 
    client_socket.connect(server_address)
    print("Connected to the chat server.")
    
    send_thread = threading.Thread(target=send_message, args=(client_socket,))
    receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
    
    receive_thread.start()
    send_thread.start()

    send_thread.join() 
    receive_thread.join() 

    client_socket.close()

if __name__ == "__main__":
    run_client()
