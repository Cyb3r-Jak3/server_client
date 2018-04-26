import socket

IP = 'localhost'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Made')

s.connect((IP, PORT))
print("Established connection with the server.")


def mode0():
    s.send('0'.encode('utf-8'))
    while True:
        message = input('What would you like to say \n')
        if message == 'break':
            s.send('break'.encode('utf-8'))
            break
        s.send(message.encode('utf-8'))

        if (s.recv(1024)).decode('utf-8'):
            print('Message Worked')


def mode1():
    s.send('1'.encode('utf-8'))
    while True:
        message = input('What would you like to guess \n')
        if message == 'break':
            s.send('break'.encode('utf-8'))
            break
        s.send(message.encode('utf-8'))

        if (s.recv(1024)).decode('utf-8') == 'Won':
            print('You won')
            break


choice = input('Mode?\n')
if choice == '0':
    mode0()
if choice == '1':
    mode1()

s.close()
