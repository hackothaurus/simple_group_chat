# Python program to implement client side of chat room. 
import socket 
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

s.connect(("127.0.0.1", 1234)) 


while True:
	str = input("user1: ");
	s.send(str.encode());
	if(str == "Bye" or str == "bye"):
		break;
	print ("N:",s.recv(1024).decode())
s.close();
