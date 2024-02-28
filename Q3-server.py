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

clients = []
lock = threading.Lock()

def handle_client(client_socket, client_address):
    with lock:
        clients.append(client_socket)

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            message = pickle.loads(data)
            print(f"Received message from {client_address}: {message}")
            broadcast(message, client_socket)

    except:
        pass

    finally:
        with lock:
            clients.remove(client_socket)
        client_socket.close()

def broadcast(message, sender_socket):
    with lock:
        for client_socket in clients:
            if client_socket != sender_socket:
                try:
                    client_socket.sendall(pickle.dumps(message))
                except:
                    clients.remove(client_socket)

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.0.20', 12345)
    server_socket.bind(server_address)
    server_socket.listen(5)
    print("Server is listening for incoming connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()


if __name__ == "__main__":
    run_server()
