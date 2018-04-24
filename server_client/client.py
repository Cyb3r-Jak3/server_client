import socket, random
IP = 'localhost'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket Made')

s.connect((IP, PORT))
print ("Established connection with the server.")
def Mode0():
	s.send('0'.encode('utf-8'))
	while True:
		message = input('What would you like to say \n')
		if message == 'break':
			s.send('break'.encode('utf-8'))
			break
		s.send(message.encode('utf-8'))

		if (s.recv(1024)).decode('utf-8'):
			print ('Message Worked')
def Mode1():
	s.send('1'.encode('utf-8'))
	while True:
		message = input('What would you like to guess \n')
		if message == 'break':
			s.send('break'.encode('utf-8'))
			break
		s.send(message.encode('utf-8'))

		if (s.recv(1024)).decode('utf-8') == 'Won':
			print ('You won')
			break

chocie = input('Mode?\n')
if chocie == '0':
	Mode0()
if chocie == '1':
	Mode1()

s.close()