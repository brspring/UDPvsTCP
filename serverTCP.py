import socket

host = input("Insira o IP do servidor: ")
port = int(input("Insira a porta do servidor: "))
buffer_size = 2048

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # cria socket tcp
    s.bind((host, port))
    s.listen()
    while True:
        print("[*] Aguardando conexão...")
        conn, addr = s.accept()
        with conn:
            print(f"[+] Conectado por {addr}")
            file_info = conn.recv(buffer_size).decode() # recebe nome e tamanho do arquivo
            infos = file_info.split("_")
            filename = infos[0]
            filesize = int(infos[1])
            
            print("[+] Nome e tamanho do arquivo recebidos do cliente.")
            conn.send("Nome e tamanho do arquivo recebidos".encode())
            
            # Recebendo e salvando o arquivo
            with open(f"output_{filename}", "wb") as fo:  # Salvar em modo binário
                total_received = 0
                while total_received < filesize: 
                    data = conn.recv(buffer_size)
                    fo.write(data)
                    total_received += len(data)  # Atualizar o progresso

            conn.send("Arquivo recebido com sucesso".encode()) # confirma o recebimento do arquivo
            print(f"[+] Arquivo recebido e salvo com sucesso como output_{filename}.")

# o bloco with do python garante o fechamento do socket e arquivo aberto, por isso não tem close