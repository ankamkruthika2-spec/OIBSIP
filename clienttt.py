import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 5000))

print("Connected to server!")

while True:
    message = input("You: ")

    client.send(message.encode())

    reply = client.recv(1024).decode()

    print("Server:", reply)

client.close()
