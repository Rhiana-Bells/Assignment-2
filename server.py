import socket

HOST = "127.0.0.1"   # Localhost — only reachable on this machine
PORT = 12345         
BUFFER_SIZE = 1024   # Maximum bytes to receive at once

def run_server():
   
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
      
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server listening on {HOST}:{PORT}...")

        # Accept a single incoming connection (blocks until a client connects)
        client_socket, client_address = server_socket.accept()
        print(f"Connected by {client_address}")

        
        data = client_socket.recv(BUFFER_SIZE).decode("utf-8")
        print(f"Received: {data}")

    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        # Always clean up, even if an error occurred
        client_socket.close()
        server_socket.close()
        print("Server closed.")


if __name__ == "__main__":
    run_server()