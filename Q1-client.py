#Implement a client-server file transfer application where the client sends a file to the server using sockets. 
#Before transmitting the file, pickle the file object on the client side. On the server side, receive the pickled file object, unpickle it, and save it to disk.


#Requirements:
#The client should provide the file path of the file to be transferred.
#The server should specify the directory where the received file will be saved.
#Ensure error handling for file I/O operations, socket connections, and pickling/unpickling.

import socket
import pickle

def run_client(file_path):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server_address = ('192.168.0.20', 12345) 
    client_socket.connect(server_address)
    
    try: 
        # Read and pickle the file
        with open(file_path, 'rb') as f:
            file_content = f.read()
            pickled_file = pickle.dumps(file_content)

            # Send the pickled file to the server
            client_socket.sendall(pickled_file)
            print("File sent successfully!")

        
        # Receive the acknowledgment from the server
        receive_data = client_socket.recv(1024)
        print("Received acknowledgment:", receive_data.decode())
        
    except Exception as e:
        print(f"Failed to send the file: {e}")
  
    finally:
        # Clean up the connection
        client_socket.close()
        
if __name__ == "__main__":
    run_client('D:/zoeyA/S4/btp425/sendFile.txt')
