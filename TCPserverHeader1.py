
#Import the socket library
from struct import *
import socket
from _thread import *

def threaded_client(conn, addr):
    #Print info: Connected address, Server IP & Port, Client IP & Port
    print("Thread to handle connection by:", addr)
    print("Server Socket port: ", conn.getsockname())
    print("Client Socket port: ", conn.getpeername())

    while(1):
       
        message = conn.recv(1024)
        n1,n2,cal= unpack('HHH',message)
        

        if cal == 1:
            if n1 >= 0 and n1 <=60000 and n2 >= 0 and n2 <= 60000 :
                final = n1+n2 
            else:
             final=123456
             print("Type numbers inbound")
        elif cal == 2:
            if n1 >= 0 and n1 <=30000 and n2 >= 0 and n2 <= 30000 :
                final = n1-n2 
            else:
             final=123456
             print("Type numbers inbound")
        elif cal == 3:
            if n1 >= 0 and n1 <=60000 and n2 > 0 and n2 <= 60000 :
                final = int(n1/n2)
            else:
             final=123456
             print("Type numbers inbound")
        elif cal == 4:
            if n1 >= 0 and n1 <=60000 and n2 >= 0 and n2 <= 60000 :
                final = n1*n2 
            else:
             final=123456
             print("Type numbers inbound")
        elif cal == 5:
            if n1 >= 0 and n1 <=10 and n2 >= 0 and n2 <= 6 :
                final = pow(n1,n2)
            else:
             final=123456
             print("Type numbers inbound")
        else:
            print("You have to choose calulating method from 1 to 5")

        if cal == 1:
            print("The first number is: ", n1,)
            print("The second number is: ", n2)
            print("The result is: ",final)
            print("The calcuting method you chose is addition!")
        elif cal == 2:
            print("The first number is: ", n1,)
            print("The second number is: ", n2)
            print("The result is: ",final)
            print("The calcuting method you chose is substraction!")
        elif cal == 3:
            print("The first number is: ", n1,)
            print("The second number is: ", n2)
            print("The result is: ",final)
            print("The calcuting method you chose is division!")
        elif cal == 4:
            print("The first number is: ", n1,)
            print("The second number is: ", n2)
            print("The result is: ",final)
            print("The calcuting method you chose is multiplication!")
        elif cal == 5:
            print("The first number is: ", n1,)
            print("The second number is: ", n2)
            print("The result is: ",final)
            print("The calcuting method you chose is power!")
        else:
            print("You have to do the Action correctly")


        #Now it's time to pack our response.
        message = pack('I', final,)
        #Send the message through the same connection
        try:
            conn.sendall(message)
        except:
            print("error")

#Host IP to listen to
serverIP = '127.0.0.1'
#Port to listen to
serverPort = 12345

close = False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    #Bind the socket
    serverSocket.bind((serverIP, serverPort))
    print ("The server is ready to receive at port", str(serverPort))
    #Listen for connections
    serverSocket.listen()
    
    ThreadCount=0
    while not close:
        #Listen and wait for connection
        #Once a connection is made it returns two values, the conn will have the connection socket and the addr will have the address
        conn, addr = serverSocket.accept()

        #Print info: Connected address, Server IP & Port, Client IP & Port
        start_new_thread(threaded_client, (conn, addr))
        ThreadCount+=1
        print('Thread Number: ' + str(ThreadCount))
       
           
