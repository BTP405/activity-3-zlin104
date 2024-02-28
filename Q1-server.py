#Implement a client-server file transfer application where the client sends a file to the server using sockets. 
#Before transmitting the file, pickle the file object on the client side. On the server side, receive the pickled file object, unpickle it, and save it to disk.


#Requirements:
#The client should provide the file path of the file to be transferred.
#The server should specify the directory where the received file will be saved.
#Ensure error handling for file I/O operations, socket connections, and pickling/unpickling.

import socket
import pickle

def run_server(save_dir):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.0.20', 12345) 
    server_socket.bind(server_address)
    server_socket.listen(1)

    print("Server is listening for incoming connections...")
    
    try: 
        client_socket, client_address = server_socket.accept()
        print("Connected to", client_address)

        # Receive pickled file from the client 
        pickled_file = client_socket.recv(1024) 
        file_content = pickle.loads(pickled_file)


        # Save the received file to the specified directory
        with open(save_dir, 'wb') as f:
            f.write(file_content)
            print("File received successfully and saved to:", save_dir)

            
            # Send an acknowledgment back to the client 
            message = "File received and saved by the server!" 
            client_socket.sendall(message.encode())

    except Exception as e:
        print(f"Failed to save the file: {e}")
            
    finally: 
        # clean up the connection 
        client_socket.close()
            
if __name__ == "__main__":
    run_server('D:/zoeyA/S4/activity-3-zlin104/receiveFile.txt')
