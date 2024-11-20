import socket

host = input("Insira o IP do servidor: ")
port = int(input("Insira a porta do servidor: "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            
            fo = open("output.txt", "w+")

            fo.write(data)
            fo.close()
            