import socket
import ssl
import os



class Server:
    
    def __init__(self) -> None:
        self.ip_address = '127.0.0.1'
        self.port = 40000
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    
    def run(self):
        """Establish and wrap a socket object in TLS."""        
        
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain('.\\Certs\\certificate.pem', '.\\Certs\\privkey.pem')
        connection = context.wrap_socket(self.server_socket, server_side = True)
        connection.bind((self.ip_address, self.port))
        connection.listen(5)
        print(f"[+] Listening on {self.ip_address}:{self.port}")
        
        while True:
            client_socket, client_address = connection.accept()
            print(f"[+] Connection received from {client_address}")
            print('''Enter one of the following commands to continue: 
                  filesend - To send a file
                  enter_shell - To enter a shell
                  exit - To close the connection to the client''')
                        
            self.handle_user_input(client_socket)
            self.send_file(client_address)
        
    def handle_user_input(self, client_socket):
        """Take user input, encode and send to client for use.
        Currently using commands that would work on cmd but not
        all work. Implementation will come soon.

        Args:
            client_socket (_type_): Takes in the socket 
            provided by the client once it connects
        """        
        
        while True:
            try:
                command = input("Enter your command: ")
                
                if command.lower() == 'exit':
                    client_socket.send(b'exit')
                    client_socket.close()
                    print(f"[+] The client closed the connection")
                    print(f"[+] Listening on {self.ip_address}:{self.port}")
                    break
                
                if command.lower() == 'filesend':
                    chosen_file = input("[+] Enter the filepath of the file you wish to send: ")
                    self.send_file(chosen_file, client_socket)
                
                if command:
                    client_socket.send(command.encode('utf-8'))
                    response = client_socket.recv(4096).decode('utf-8')
                    print(response)
            
            except Exception as e:
                print(e)
            
    def send_file(self, file_path, client_address):
        
        client_socket = client_address
        
        try:
            if not os.path.exists(file_path):
                client_socket.send(b"[+] ERROR: File does not exist!")
                return
            
            filename = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            client_socket.send(f"{filename}, {file_size}".encode('utf-8'))
            
            client_ack = client_socket.recv(1024).decode('utf-8')
            if client_ack != "READY":
                print("[+] Client not ready to receive the file!")
                return
            
            with open(file_path, "rb") as f:
                print(f"[+] Sending {filename}...")
                while True:
                    file_data = f.read(4096)
                    if not file_data:
                        break
                    
                    client_socket.send(file_data)
                    
            client_socket.send(b"DONE")            
        
        except Exception as e:
            print(f"[+] Error while sending the file: {e}")
                    
    
    def receive_file(self):
        pass
        
if __name__ == "__main__":
    serverobject = Server()
    serverobject.run()