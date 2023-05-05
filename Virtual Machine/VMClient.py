import socket
import ipaddress
import threading
import time
import contextlib
import errno

maxPacketSize = 1024
defaultPort = 1025  # TODO: Change this to your expected port
serverIP = '10.128.0.2'  # TODO: Change this to your instance IP

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
try:
    tcpPort = int(input("Please enter the TCP port of the host..."));
except:
    tcpPort = 0;
if tcpPort == 0:
    tcpPort = defaultPort;
tcpSocket.connect((serverIP, tcpPort));

clientMessage = "";
while clientMessage != "exit":
    clientMessage = input("Please type the message that you'd like to send (Or type \"exit\" to exit):\n>");

    # TODO: Send the message to your server
    tcpSocket.sendall(clientMessage.encode())
    # TODO: Receive a reply from the server for the best highway to take
    serverReply = tcpSocket.recv(maxPacketSize)
    # TODO: Print the best highway to take
    serverReply=serverReply.decode()
    print(f'Best highway to take: {serverReply[12:17]}')

    # tcpSocket.sendall(clientMessage.encode())
    # response = tcpSocket.recv(maxPacketSize).decode()
    # print(response)

tcpSocket.close();
import socket
import ipaddress
import threading
import time
import contextlib
import errno

maxPacketSize = 1024
defaultPort = 1025  # TODO: Change this to your expected port
serverIP = '10.128.0.2'  # TODO: Change this to your instance IP

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
try:
    tcpPort = int(input("Please enter the TCP port of the host..."));
except:
    tcpPort = 0;
if tcpPort == 0:
    tcpPort = defaultPort;
tcpSocket.connect((serverIP, tcpPort));

clientMessage = "";
while clientMessage != "exit":
    clientMessage = input("Please type the message that you'd like to send (Or type \"exit\" to exit):\n>");

    # TODO: Send the message to your server
    tcpSocket.sendall(clientMessage.encode())
    # TODO: Receive a reply from the server for the best highway to take
    serverReply = tcpSocket.recv(maxPacketSize)
    # TODO: Print the best highway to take
    serverReply=serverReply.decode()
    print(f'Best highway to take: {serverReply[12:17]}')

    # tcpSocket.sendall(clientMessage.encode())
    # response = tcpSocket.recv(maxPacketSize).decode()
    # print(response)

tcpSocket.close();
