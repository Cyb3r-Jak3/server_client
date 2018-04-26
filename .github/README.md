# server_client  
## coolaspie  
#### Written for python 3+
---
This is designed as a demo for using socket in python.  
Both versions allow for multiple clients.  
I am leaving V1 in as I believe that it is easier to understand for starting sockets.  
V2 is the one I will continue to develop

There are currently two modes, the first one is the client sending messages to the server which writes them to stuff.txt. The second mode is a random number guessing game where the client guesses number from 1 to 10.  
To use:  
```
git clone https://github.com/coolaspie/server_client.git
```  
To run:  
``` 
python3 server.py
python3 client.py
``` 
(Quick note: You will two seperate terminals sessions. 1 for server and 1 for client)
  
1. Mode0:  
    -  Send Text: The client connect to the server and sends text to the server which writes it out in stuff.txt. Type "break" to end the session
2. Mode1
    - Random Number Game: Client sends a number (currently between 1 & 10) and when the correct number is guessed the session ends.
