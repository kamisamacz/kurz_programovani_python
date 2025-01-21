import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect(('localhost', 12388))
        print("Připojeno k serveru na adrese localhost:12388")

        while True:
            message = input("Zadejte zprávu pro server (nebo 'exit' pro ukončení): ")
            if message.lower() == 'exit':
                print("Ukončuji spojení se serverem.")
                break

            client_socket.sendall(message.encode())
            response = client_socket.recv(8888).decode()
            print(f"Odpověď ze serveru: {response}")

    except ConnectionRefusedError:
        print("Nelze se připojit k serveru. Ujistěte se, že server běží.")

    except Exception as e:
        print(f"Došlo k chybě: {e}")

    finally:
        client_socket.close()
        print("Spojení bylo uzavřeno.")

if __name__ == "__main__":
    main()
