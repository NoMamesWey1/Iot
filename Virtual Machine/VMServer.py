import certifi
import socket
import ipaddress
import threading
import time
import contextlib
import errno
from dataclasses import dataclass
import random
import sys

maxPacketSize = 1024
defaultPort = 1025 #TODO: Set this to your preferred port

def GetFreePort(minPort: int = 1024, maxPort: int = 65535):
    for i in range(minPort, maxPort):
        print("Testing port",i);
        with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as potentialPort:
            try:
                potentialPort.bind(('0.0.0.0', i));
                potentialPort.close();
                print("Server listening on port",i);
                return i
            except socket.error as e:
                if e.errno == errno.EADDRINUSE:
                    print("Port",i,"already in use. Checking next...");
                else:
                    print("An exotic error occurred:",e);

def GetServerData():
    import VMMongoDBConnection as mongo
    return mongo.QueryDatabase();






def ListenOnTCP(tcpSocket: socket.socket, socketAddress):
    # TODO: Implement TCP Code, use GetServerData to query the database.
    print("Accepted connection from", socketAddress)
    with tcpSocket:
        try:
            clientMessage = tcpSocket.recv(maxPacketSize).decode()
            while clientMessage:
                print("Received message:", clientMessage)
                serverData = GetServerData()
                # Here you can process the serverData as needed
                response = str(serverData)
                tcpSocket.sendall(response.encode())
                clientMessage = tcpSocket.recv(maxPacketSize).decode()
        except ConnectionResetError:
            # Connection was reset by client
            pass
        except Exception as e:
            # Handle any other exceptions that might occur
            print("An error occurred:", e)
    print("Closing connection from", socketAddress)
    sys.exit()


def CreateTCPSocket() -> socket.socket:
    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    tcpPort = defaultPort
    print("TCP Port:",tcpPort);
    tcpSocket.bind(('0.0.0.0', tcpPort));
    return tcpSocket;

def LaunchTCPThreads():
    tcpSocket = CreateTCPSocket();
    tcpSocket.listen(5);
    while True:
        connectionSocket, connectionAddress = tcpSocket.accept();
        connectionThread = threading.Thread(target=ListenOnTCP, args=[connectionSocket, connectionAddress]);
        connectionThread.start();

if __name__ == "__main__":
    tcpThread = threading.Thread(target=LaunchTCPThreads);
    tcpThread.start();
    exitSignal = False
    while not exitSignal:
        time.sleep(1);
    print("Ending program by exit signal...");
