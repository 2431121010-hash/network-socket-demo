# echo_server.py
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 12346))
server.listen()
print("Echo Server đang chờ kết nối...")

conn, addr = server.accept()
print(f"Client kết nối từ: {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Nhận:", data.decode())
    conn.sendall(data)  # Gửi lại dữ liệu cho client

conn.close()
