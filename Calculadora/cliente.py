import socket

HOST = '127.0.0.1'
PORT = 5000

def iniciar_cliente():
    while True:
        num1 = input("Ingresa el primer numero: ")
        operacion = input("Ingresa la operacion (+, -, *, /): ")
        num2 = input("Ingresa el segundo numero: ")
        mensaje = f"{num1} {operacion} {num2}"
        
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((HOST, PORT))
        cliente.send(mensaje.encode())
        respuesta = cliente.recv(1024).decode()
        
        print("Respuesta del servidor: ", respuesta)
        
        cliente.close()
        
        continuar = input("Deseas realizar otra operacion? (S/N): ")
        if continuar.lower() != 'S':
            break
        
if __name__ == "__main__":
    iniciar_cliente()