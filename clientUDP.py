import socket
import os
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # cria o socket udp
ip = input("Insira o IP do servidor: ")
porta = int(input("Insira a porta do servidor: "))
buffer = 2048
timeout = 5.0  # 5 segundos
pacotes_perdidos = 0

fileName = input("Insira o nome do arquivo para enviar: ")

try:

    filesize = os.path.getsize(fileName) # pega o tamanho do arquivo
    print(f"Enviando arquivo: {fileName} ({filesize} bytes)")

    # Manda nome e tamanho do arquivo
    client.sendto(f"{fileName}_{filesize}".encode(), (ip, porta))

    # Envia o arquivo em pedaços
    with open(fileName, "rb") as file:
        total_enviados = 0
        client.settimeout(timeout) # seta timeout para as chamadas bloqueantes do socket do cliente (ex: recv)
                                    # serve para identificar se um pacote foi perdido
        
        inicio_tempo = time.time() # inicia timer do tempo para enviar o arquivo
        while chunk := file.read(buffer):  
            total_enviados += 1
            
            client.sendto(chunk, (ip, porta)) # envia pacote para o servidor
            try: # recebe a confirmação de recebimento do servidor a não ser que demore mais que 5 segs
                ack, _ = client.recvfrom(buffer) 
                
            except socket.timeout:
                pacotes_perdidos += 1
                print("Timeout: pacote perdido")

    # Mensagem de fim
    client.sendto(b"FIM", (ip, porta)) 

    fim_tempo = time.time() # finaliza timer
    print(f"Arquivo enviado com sucesso.")
    print(f"(Tempo de envio do arquivo: {(fim_tempo - inicio_tempo) * 1000:.2f} ms)")
    print(f"Pacotes perdidos: {pacotes_perdidos}")

except IOError:
    print("Erro ao abrir ou enviar o arquivo.")
finally:
    client.close()
