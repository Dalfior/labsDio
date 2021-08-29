import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

code = client.connect_ex(("google.com", 80))

print(code)
