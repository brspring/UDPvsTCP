import socket
import os
import time

host = "192.168.1.2"
port = 65432
fileName = input("Insira o nome do arquivo para enviar: ")
buffer_size = 2048

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

try:
    # Lendo o arquivo e enviando os dados ao servidor
    filesize = os.path.getsize(fileName)
    s.send(f"{fileName}_{filesize}".encode())  # Enviando nome e tamanho do arquivo
    response = s.recv(buffer_size).decode()
    print(f"[+] {response}")
    if response != "Nome e tamanho do arquivo recebidos":
        print("[Erro] Não foi possível enviar o arquivo.")
        s.close()
        exit()
        
    with open(fileName, "rb") as file:  # Abrir em modo binário
        inicio_tempo = time.time()
        while chunk := file.read(buffer_size):  # Ler em pedaços
            s.send(chunk)  # Enviar pedaço ao servidor
    
    response = s.recv(buffer_size).decode()
    if response != "Arquivo recebido com sucesso":
        print("[+] Erro ao receber arquivo")
    else:
        print("[+] Arquivo recebido com sucesso")
        
    fim_tempo = time.time()
    rtt = (fim_tempo - inicio_tempo) * 1000 # x1000 para ser em ms
    print(f"(Tempo de envio do arquivo: {rtt:.2f} ms)")
    s.close()
except IOError:
        print('Arquivo inválido ou erro ao abrir o arquivo.')
