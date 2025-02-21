import socket
import torch
import time
import numpy as np

# UDP_IP = "169.254.138.50"
UDP_IP = "localhost"
# UDP_IP = "134.69.65.224"
# UDP_PORT = 2000
UDP_PORT = 9090



grid = np.load('grid.npy')
# data = grid.tobytes()
shape = grid.shape
# dtype = str(grid.dtype)

udp_socket = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP

server_address = (UDP_IP, UDP_PORT)


#################################################################################################################

# # print(shape[0], shape[1], dtype)
# rows = torch.tensor([shape[0]], dtype=torch.float32).numpy().tobytes()
# cols = torch.tensor([shape[1]], dtype=torch.float32).numpy().tobytes()
# # dtype = torch.tensor([dtype], dtype=torch.float32).numpy().tobytes()

# udp_socket.sendto(rows, server_address)
# time.sleep(5)
# udp_socket.sendto(cols, server_address)
# time.sleep(5)

#######################################################################################################################
# udp_socket.sendto(dtype, server_address)

# metadata = f"{shape[0]},{shape[1]},{dtype}".encode('utf-8')


# udp_socket.sendto(shape[0], server_address)
# time.sleep(5)
# udp_socket.sendto(shape[1], server_address)
# time.sleep(5)
# udp_socket.sendto(dtype, server_address)



# # Create a small 2x3 grid with ascending values
rows = torch.tensor([2], dtype=torch.float32).numpy().tobytes()
cols = torch.tensor([3], dtype=torch.float32).numpy().tobytes()
grid = np.array([[1, 2, 50], [4, 5, 20]])

# print(grid[0, :])
# for i in grid[0, :]:
#     print(i)
#     time.sleep(5)


# Send metadata (shape and dtype)
# metadata = f"{shape[0]},{shape[1]},{dtype}".encode('utf-8')
# udp_socket.sendto(metadata, server_address)

udp_socket.sendto(rows, server_address)
print(f"Sent rows = {rows}")
# time.sleep(5)
print(f"Sent cols = {cols}")
udp_socket.sendto(cols, server_address)
# time.sleep(5)


# Loop through the grid column-wise and send each column
for row in range(grid.shape[0]):
    row_data = grid[row, :]
    for i in row_data:
        print(i)
        i = torch.tensor([i], dtype=torch.float32).numpy().tobytes()
        # time.sleep(5)
    # print(f"Sending column {column_data}")
        udp_socket.sendto(i, server_address)
        # time.sleep(1)
    # time.sleep(5)  # Optional: add a small delay between sends

# # Send the serialized data
# udp_socket.sendto(data, server_address)
# udp_socket.close()

# print(shape, dtype)


# for i in range(10):
    # MESSAGE = torch.tensor([i, i+1, i+2], dtype=torch.float32).numpy().tobytes()

#     print("UDP target IP: %s" % UDP_IP)
#     print("UDP target port: %s" % UDP_PORT)
#     print("message: %s" % MESSAGE)

#     sock = socket.socket(socket.AF_INET, # Internet
#                         socket.SOCK_DGRAM) # UDP
#     sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
#     time.sleep(5)