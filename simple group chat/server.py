# Harram Khan
#207430, NUST BSCS7C
#Distributef Computing Lab 2

import socket 
import select 
import sys 
from _thread import *
import threading 

s = socket.socket();
port = 1234;
s.bind(('', port));
s.listen(5); 

""" 
listens for 5 active connections.  
"""

clientsL = [] 

def clientthread(conn, addr): 

    # sends a message to the client whose user object is conn
    welcome = "server: Welcome to this chatroom! Wait for next user to type"
    conn.send(welcome.encode()) 

    while True:
        try:
            message = conn.recv(2048).decode()
            print ("total clients: " + str(len(clientsL)))
            print ("<" + addr[0] + ", "+ str(addr[1]) + "> " + message )
            # Calls broadcast function to send message to all 
            message_to_send = "~" + addr[0] + "~ " + message
            automatedresponse = "server response: okay"
            conn.send(automatedresponse.encode())
            broadcast(message_to_send.encode(), conn)
            if(message == "Bye" or message == "bye"):
                break;
        except:
            continue

                



def broadcast(message, connection): 
    for clients in clientsL: 
        if clients!=connection: 
            try: 
                clients.send(message) 
            except: 
                print("weird unknown error") 


def remove(connection): 
    if connection in clientsL: 
        clientsL.remove(connection) 

while True: 

    conn, addr = s.accept() 
    
    #list of clients
    clientsL.append(conn) 

    # prints the address of the user that just connected 
    print( addr[0] + " connected")

    # creates and individual thread for every user 
    # that connects 
    start_new_thread(clientthread,(conn,addr))   

conn.close() 
s.close() 
