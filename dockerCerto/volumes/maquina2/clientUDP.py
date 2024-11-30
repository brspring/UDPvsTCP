import socket
import os
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "192.168.1.2"
porta = 1500
buffer = 2048
timeout = 5.0  # 5 segundos
pacotes_perdidos = 0

fileName = input("Insira o nome do arquivo para enviar: ")

try:
    # Para enviar um único arquivo, não é necessário o loop infinito
    filesize = os.path.getsize(fileName)
    print(f"Enviando arquivo: {fileName} ({filesize} bytes)")

    # Manda nome e tamanho do arquivo
    client.sendto(f"{fileName}_{filesize}".encode(), (ip, porta))

    # Envia o arquivo em pedaços
    with open(fileName, "rb") as file:
        total_enviados = 0
        inicio_tempo = time.time()
        client.settimeout(timeout)
        while chunk := file.read(buffer - 10):  # Reserve espaço para cabeçalhos
            total_enviados += 1
            
            client.sendto(chunk, (ip, porta))
            try:
                ack, _ = client.recvfrom(buffer)
                
            except socket.timeout:
                pacotes_perdidos += 1
                print("Timeout: reenviando pacote...")

    # Mensagem de fim
    client.sendto(b"FIM", (ip, porta))

    fim_tempo = time.time()
    print(f"Arquivo enviado com sucesso.")
    print(f"(RTT estimado: {(fim_tempo - inicio_tempo) * 1000:.2f} ms)")
    print(f"Pacotes perdidos: {pacotes_perdidos}")

except IOError:
    print("Erro ao abrir ou enviar o arquivo.")
finally:
    client.close()
