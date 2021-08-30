#implementar range de portas
#FastyScan

import socket


ip = input("Digite o host ou IP: ") 
ports = int(input("Digite a ultima porta: "))
lista = []
count = 0
ultimo = 0


while count < ports+1:
	lista.append(count)
	count += 1
	ultimo = len(lista) - 1
	
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(0.02)
	code = client.connect_ex((ip, ultimo))
	
	if code == 0:
		print(str(ultimo), " -> Porta aberta.")
	
	else:
		print(str(ultimo), " -> Porta fechada.")
