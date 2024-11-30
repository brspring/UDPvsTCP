import socket
import os
import time

host = input("Insira o IP do servidor: ")
port = int(input("Insira a porta do servidor: "))
fileName = input("Insira o nome do arquivo para enviar: ")
buffer_size = 2048

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cria socket tcp
s.connect((host, port))

try:
    # Lendo o arquivo e enviando os dados ao servidor
    filesize = os.path.getsize(fileName)
    s.send(f"{fileName}_{filesize}".encode())  # Enviando nome e tamanho do arquivo
    response = s.recv(buffer_size).decode() # recebe mensagem dizenddo que o servidor recebeu o nome e tamanho
    print(f"[+] {response}")
    if response != "Nome e tamanho do arquivo recebidos": # encerra conexão caso server não tenha recebido nome e tamanho
        print("[Erro] Não foi possível enviar o arquivo.")
        s.close()
        exit()
        
    with open(fileName, "rb") as file:  # Abrir em modo binário
        inicio_tempo = time.time() # inicia timer para contar o tempo de enviar o arquivo
        while chunk := file.read(buffer_size):  # Ler em pedaços
            s.send(chunk)  # Enviar pedaço ao servidor
        # arquivo é fechado pelo bloco with
        
    response = s.recv(buffer_size).decode()
    if response != "Arquivo recebido com sucesso": # confirma que o server recebeu o arquivo
        print("[+] Erro ao receber arquivo")
    else:
        print("[+] Arquivo recebido com sucesso")
        
    fim_tempo = time.time() # encerra timer
    tempo_total = (fim_tempo - inicio_tempo) * 1000 # x1000 para ser em ms
    print(f"(Tempo de envio do arquivo: {tempo_total:.2f} ms)")
    s.close()
except IOError:
        print('Arquivo inválido ou erro ao abrir o arquivo.')
