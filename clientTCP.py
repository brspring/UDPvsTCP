import socket

host = input("Insira o IP do servidor: ")
port = int(input("Insira a porta do servidor: "))
fileName = input("Insira o nome do arquivo para enviar: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))

    try: 
        # Reading file and sending data to server 
        file = open(fileName, "r") 
        data = file.read() 
        print(data)
        while data: 
            s.send(str(data).encode()) 
            data = file.read() 

    except IOError: 
            print('Arquivo inválido') 

print(f"Received {data!r}")