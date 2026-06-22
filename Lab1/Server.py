import socket
# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server is waiting for client connection...")
client_socket, addr = server_socket.accept()
print(f"Machine local host {addr}")
# Sending data to client
client_socket.send(b'Distributed systems is the best CS course. Do you find it enjoyful?')
# Closing connection
client_socket.close()
server_socket.close()
