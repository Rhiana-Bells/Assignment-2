import socket

HOST = "127.0.0.1"
PORT = 12345

def run_client():
   
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")

        # Send the message (must be encoded to bytes)
        message = "Hello from client!"
        client_socket.sendall(message.encode("utf-8"))
        print(f"Sent: {message}")

    except socket.error as e:
        print(f"Socket error: {e} — is the server running?")
    except TimeoutError:
        print("Connection timed out.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        client_socket.close()
        print("Client closed.")


if __name__ == "__main__":
    run_client()