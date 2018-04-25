import socketserver


class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).decode("utf-8")
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.send(self.data.upper().encode("utf-8"))


if __name__ == "__main__":
    host, port = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((host, port), TCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
