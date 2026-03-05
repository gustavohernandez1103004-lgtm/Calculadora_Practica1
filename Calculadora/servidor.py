import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

def manejar_cliente(conn, addr):
    print(f"Cliente conectando desde {addr}")
    
    try:
        mensaje = conn.recv(1024).decode()
        print(f"Operacion recibida: {mensaje}")
        
        partes = mensaje.split()
        
        if len(partes) != 3:
            conn.send("ERROR: Formato incorrecto".encode())
            return
        
        num1 = float(partes[0])
        operacion = partes[1]
        num2 = float(partes[2])
        
        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            if num2 == 0:
                conn.send("ERROR: La divicion no es posible de hacer".encode())
                return
            resultado = num1 / num2
        else:
            conn.send("ERROR: Operacion no valida".encode())
            return
        
        print(f"Resultado calculado: {resultado}")
        conn.send(str(resultado).encode())
        
    except ValueError:
        conn.send("Error: Los valores deben ser numericos".encode())
        
    except Exception as e:
        conn.send(f"Error: {str(e)}".encode())
        
    finally:
        conn.close()
        print(f"Cliente {addr} desconectado")
        
def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()
    
    print("Servidor de calculadora iniciando...")
    print(f"Esperando conexiones en {HOST}:{PORT}")
    
    while True:
        conn, addr = servidor.accept()
        hilo = threading.Thread(target=manejar_cliente, args=(conn, addr))
        hilo.start()
        
if __name__ == "__main__":
    iniciar_servidor()            