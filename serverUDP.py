import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "127.0.0.1"
porta = 1500
buffer = 2048

server.bind((ip, porta))
print(f"Servidor UDP rodando na porta {porta} e aguardando arquivos...")

try:
    while True:
        # recebe nome e tamanho do arquivo
        print("[*] Aguardando informações do arquivo...")
        file_info, client_address = server.recvfrom(buffer)
        file_info = file_info.decode()
        filename, filesize = file_info.split("_")
        filesize = int(filesize)
        
        print(f"[+] Informações do arquivo recebidas: {filename} ({filesize} bytes)")
        server.sendto("Nome e tamanho do arquivo recebidos".encode(), client_address)
        
        # rcebendo o arquivo
        total_received = 0
        with open(f"output_{filename}", "wb") as fo:
            while total_received < filesize:
                data, client_address = server.recvfrom(buffer)
                fo.write(data)
                total_received += len(data)
        
        print(f"[+] Arquivo {filename} recebido com sucesso e salvo como output_{filename}.")
        server.sendto("Arquivo recebido com sucesso".encode(), client_address)

except KeyboardInterrupt:
    print("\nEncerrando o servidor.")
finally:
    server.close()
