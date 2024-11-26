import socket
import os
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "127.0.0.1"
porta = 1500
buffer = 2048

fileName = input("Insira o nome do arquivo para enviar: ")

try:
    # para enviar um unico arquivo nao eh necessario o loop infinito
    filesize = os.path.getsize(fileName)
    print(f"Enviando arquivo: {fileName} ({filesize} bytes)")

    # manda nome e tamanho
    client.sendto(f"{fileName}_{filesize}".encode(), (ip, porta))

    # envia o arquivo em pedacos
    with open(fileName, "rb") as file:
        total_enviados = 0
        inicio_tempo = time.time()
        
        while chunk := file.read(buffer - 10):
            total_enviados += 1
            client.sendto(chunk, (ip, porta))

    # mensagem fim
    client.sendto(b"FIM", (ip, porta))
    
    fim_tempo = time.time()
    print(f"Arquivo enviado com sucesso.")
    print(f"(RTT estimado: {(fim_tempo - inicio_tempo) * 1000:.2f} ms)")

except IOError:
    print("Erro ao abrir ou enviar o arquivo.")
finally:
    client.close()
