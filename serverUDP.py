import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "127.0.0.1"
porta = 1500
buffer = 2048

server.bind((ip, porta))
print("Servidor UDP rodando e aguardando mensagens...")

while True:
    mensagem_bytes, endereco_ip_client = server.recvfrom(buffer)
    mensagem_resposta = mensagem_bytes.decode().upper()
    server.sendto(mensagem_resposta.encode(), endereco_ip_client)
    print("Mensagem recebida e enviada de volta:", mensagem_resposta)
