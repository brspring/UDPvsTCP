import socket
import time
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "127.0.0.1"

porta = 1500
buffer = 2048

total_enviados = 0
total_recebidos = 0

while True:
    mensagem_envio = input("Digite a mensagem a ser enviada: ")
    if mensagem_envio.lower() == "sair":
        break

    total_enviados += 1

    inicio_tempo = time.time()

    client.sendto(mensagem_envio.encode(), (ip, porta))
    try:
        client.settimeout(2)
        mensagem_bytes, endereco_ip_servidor = client.recvfrom(buffer)
        fim_tempo = time.time()

        total_recebidos += 1
        rtt = (fim_tempo - inicio_tempo) * 1000 # x1000 para ser em ms
        print(f"Resposta do servidor: {mensagem_bytes.decode()} (RTT: {rtt:.2f} ms)")
    except socket.timeout:
        print("Timeout: Servidor não respondeu a tempo.")

print("\n--- Estatísticas ---")
print(f"Pacotes enviados: {total_enviados}")
print(f"Pacotes recebidos: {total_recebidos}")
print(f"Perda de pacotes: {((total_enviados - total_recebidos) / total_enviados) * 100:.2f}%")
