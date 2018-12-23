import socket

def main():
	host = '10.1.132.80'
	port = 4200

	s = socket.socket()
	s.connect((host,port))

	message = input("enter message: ")
	while message!='q':
		s.send(message.encode())
		data = s.recv(1024)
		print("recieved message: "+str(data.decode()))
		message = input("enter message: ")
	s.close()
if __name__ == "__main__":
	main()	

