import socketserver
import os
import random
import threading
# Clears the stuff file
open(os.getcwd() + "/stuff.txt", 'w').close()
f = open(os.getcwd() + "/stuff.txt", 'r+')


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        client, address = self.client_address
        received = self.request.recv(1024).decode('utf-8')

        if received == '0':
            print(address, "Mode 0")
            while True:
                try:
                    data = (self.request.recv(1024)).decode('utf-8')
                    if data:
                        if data == 'break':
                            print(address, 'Connection ended')
                            return False
                        else:
                            f.write('{} {}\n'.format(address, data))
                            response = 'ack'
                            self.request.send(response.encode('utf-8'))
                    else:
                        raise Exception("Client disconnected")
                except Exception as e:
                    self.request.close()
                    return False
        if received == '1':
            print(address, "Mode 1")
            hidden = random.randint(0, 10)
            while True:
                try:
                    data = (self.request.recv(1024)).decode('utf-8')
                    if data:
                        if data == 'break':
                            print(address, 'Connection ended')
                            return False
                        else:
                            if data == str(hidden):
                                self.request.send('Won'.encode('utf-8'))
                                print(address, "Got it. Ending Connection")
                                break
                            else:
                                self.request.send("Fail".encode('utf-8'))
                except Exception as e:
                    self.request.close()
                    return False


if __name__ == "__main__":
    host, port = "localhost", 9998

    # Create the server, binding to localhost on port 9999
    with socketserver.ThreadingTCPServer((host, port), ThreadedTCPRequestHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        server.serve_forever()

