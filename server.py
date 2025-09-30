# Server đơn giản
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen()

print("Đang chờ kết nối...")
conn, addr = server.accept()
print(f"Kết nối từ {addr}")
data = conn.recv(1024)
print("Dữ liệu nhận được:", data.decode())
conn.close()