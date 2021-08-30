#PortScan com range de portas
import socket


ip = input("Digite o host ou IP: ")
port1 = int(input("Digite a primeira porta: "))
port2 = int(input("Digite a ultima porta: "))

for x in range (port1, port2):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.02)
        code = client.connect_ex((ip, x))

        if code == 0:
                print(str(x), " -> Porta aberta.")

        else:
                print(str(x), " -> Porta fechada.")
