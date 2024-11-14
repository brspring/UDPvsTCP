import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "127.0.0.1"  # IP do servidor
porta = 1500
buffer = 2048

while True:
    mensagem_envio = input("Digite a mensagem a ser enviada: ")
    client.sendto(mensagem_envio.encode(), (ip, porta))
    mensagem_bytes, endereco_ip_servidor = client.recvfrom(buffer)
    print("Resposta do servidor:", mensagem_bytes.decode())
