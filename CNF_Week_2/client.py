import socket

def main():
    host = '10.10.9.51'
    port = 4200

    s = socket.socket()
    s.connect((host,port))
    print("Enter the roll number: ")
    message = input("roll number: ")
    while True:
        s.send(message.encode())
        data = s.recv(1024).decode()
        print(str(data))
        if len(data.split(':')) == 2:
            break
        message = input("roll number: ")
        
    s.close()
if __name__ == "__main__":
    main()  