import socket
import threading 
import random
def main():
	host = '10.10.9.51'
	port = 4200

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host,port))
	print("server started")
	s.listen(5)
	# while True:
	# 	client,addr = s.accept()
	# 	print("connection from: "+str(addr))
	# 	threading.Thread(target = example, args=(client, )).start()
		
if __name__ =="__main__":
	main()		
