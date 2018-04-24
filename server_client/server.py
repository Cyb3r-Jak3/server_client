import socket, threading, os, random

open(os.getcwd() + "/stuff.txt", 'w').close()
f = open(os.getcwd() + "/stuff.txt", 'r+')


class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        print("Server Up")
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            print(address[1], "Connected")
            threading.Thread(target=self.listen_to_client, args=(client, address)).start()

    def listen_to_client(self, client, address):
        received = client.recv(1024).decode('utf-8')
        print(type(received))
        print(received)

        if received== '0':
            print(address[1], "Mode 0")
            while True:
                try:
                    data = (client.recv(1024)).decode('utf-8')
                    if data:
                        if data == 'break':
                            print (address[1], 'Connection ended')
                            return False
                        else:
                            f.write('%s %s\n' % (str(address[1]), data))
                            response = 'ack'
                            client.send(response.encode('utf-8'))
                    else:
                        raise error('Client disconnected')
                except:
                    client.close()
                    return False
        if received == '1':
            print(address[1], "Mode 1")
            hidden = random.randint(0,10)
            print(hidden)
            while True:
                try:
                    data = (client.recv(1024)).decode('utf-8')
                    if data:
                        if data == 'break':
                            print (address[1], 'Connection ended')
                            return False
                        else:
                            if data == str(hidden):
                                client.send('Won'.encode('utf-8'))
                                print(address[1], "Got it Ending Connection")
                                break
                            else:
                                client.send("Fail".encode('utf-8'))
                except:
                    client.close()
                    return False


if __name__ == "__main__":
    port_num = 5000
    ThreadedServer('', port_num).listen()
