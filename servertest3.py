import socket
import time

def start_server(file_path, delay, packet_size):
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the local address and port
    server_address = ("", 1024)
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1)
    print("Server listening on port 1024")
    while True:
        # Wait for a client to connect
        print("Waiting for a connection")
        connection, client_address = sock.accept()
        try:
            print(f"Connection from {client_address}")
            # Open the file in binary mode
            with open(file_path, "wb") as f:
                # Receive and process data from the client
                while True:
                    start_time = time.time()
                    data = connection.recv(packet_size)
                    end_time = time.time()
                    # Calculate the latency
                    latency = end_time - start_time
                    if data:
                        print(f"Received {len(data)} bytes")
                        f.write(data)
                    else:
                        break
        finally:
            # Clean up the connection
            connection.close()

# Example usage
start_server("received_file_test3.DZT", 0.5, 8)
