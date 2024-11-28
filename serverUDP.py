import socket
import os
import time
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "127.0.0.1"
porta = 1500
buffer = 2048
count = 3

server.bind((ip, porta))
print(f"Servidor UDP rodando na porta {porta} e aguardando arquivos...")

try:
    #while True:
        # Recebe nome e tamanho do arquivo
        print("[*] Aguardando informações do arquivo...")
        file_info, client_address = server.recvfrom(buffer)
        file_info = file_info.decode()
        filename, filesize = file_info.split("_")
        filesize = int(filesize)

        print(f"[+] Informações do arquivo recebidas: {filename} ({filesize} bytes)")
        server.sendto("ACK".encode(), client_address)  # Confirma informações

        # Recebendo o arquivo
        total_received = 0
        with open(f"output_{filename}", "wb") as fo:
            while total_received < filesize:
                data, client_address = server.recvfrom(buffer)

                if count != 3:
                    server.sendto("ACK".encode(), client_address)  # Envia confirmação
            
                count += 1
                fo.write(data)
                total_received += len(data)

        print(f"[+] Arquivo {filename} recebido com sucesso e salvo como output_{filename}.")
        server.sendto("Arquivo recebido com sucesso".encode(), client_address)

except KeyboardInterrupt:
    print("\nEncerrando o servidor.")
finally:
    server.close()
