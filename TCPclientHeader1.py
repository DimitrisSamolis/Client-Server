# -*- coding: utf-8 -*-
from struct import *
import socket
from threading import ThreadError 

#Host IP to send to.
serverIP = '127.0.0.1'

#Port to send to
serverPort = 12345
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connect. The server socket should be listening.
clientSocket.connect((serverIP, serverPort))

#Create the data for the header
count=0
while(count<5):
    n1 = int(input("Insert your first number:  ") )
    n2 = int(input("Insert your second number:  "))
    cal = int(input("Choose your calculating method by number: 1=Add, 2=Substraction, 3=Division, 4=Multiplication, 5=Power: "))

    packString = 'HHH'
    #Pack the message
    message = pack(packString, n1,n2,cal )

    #Send the message through the socket 
    clientSocket.sendall(message)

     #APANTHSH
    modifiedMessage = clientSocket.recv(1024)

    #Unpack the message
    msg1 = unpack('I', modifiedMessage)
    print(int(msg1[0]))
    if int(msg1[0]) == 123456 :
       print("The numbers are out of bounds")

    count=+1
clientSocket.close()

     

