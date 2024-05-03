import socket
import threading

# Ask user to choose a nickname
nickname = input("Choose a nickname: ")

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 50123))

# Function to receive messages from the server
def receive():
    while True:
        try:
            # Receive message from server
            message = client.recv(1024).decode('ascii')
            # If server requests nickname, send it
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                # Print the received message
                print(message)
        except:
            # If an error occurs, close the connection
            print("An error occurred!")
            client.close()
            break

# Function to send messages to the server
def write():
    while True:
        # Construct message with nickname
        message = f'{nickname}: {input("")}'
        # Send the message to the server
        client.send(message.encode('ascii'))

# Create a thread to receive messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Create a thread to send messages
write_thread = threading.Thread(target=write)
write_thread.start()
