import socket
import time
import matplotlib.pyplot as plt

def send_file(ip_address, file_path, delay, packet_size, latency_file_path):
    latencies = []
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the remote device
    sock.connect((ip_address, 1024))

    # Send an intial message with the desired packet size
    sock.sendall(packet_size)

    # Open the file in binary mode
    with open(file_path, "rb") as f:
        # Read the file in chunks and send each chunk over the socket
        data = f.read(packet_size)
        while data:
            start_time = time.time()
            sock.sendall(data)
            end_time = time.time()
            # Calculate the latency in milliseconds
            latency = (end_time - start_time) * 1000
            latencies.append(latency)
            print(f"Latency: {latency} ms")
            time.sleep(delay / 1000)
            data = f.read(packet_size)
    sock.close()
    # Save the latencies to a text file
    with open(latency_file_path, "w") as f:
        for latency in latencies:
            f.write(f"{latency}\n")
    return latencies

# Example usage
latencies = send_file("192.168.200.17", "test.DZT", 0.5, 8, "latenciestest3.txt")

# Plot the latencies
plt.plot(latencies)
plt.xlabel("Time")
plt.ylabel("Latency (ms)")
plt.show()
