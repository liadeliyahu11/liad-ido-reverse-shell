import socket
import threading


def send_command_from_user(cs):
	cmd = raw_input("")
	cs.send(cmd)
	
def recv_print(cs):
	while True:
		print cs.recv(1024)
	
def main():
	try:
		sock = socket.socket()
		sock.bind(("0.0.0.0", 1234))
		sock.listen(1)
		client_sock, client_addr = sock.accept()		
		t = threading.Thread(target=recv_print, args = (client_sock,))
		t.start()
		print "Enter commands: "
		while True:
			send_command_from_user(client_sock)
			
	except Exception as ex:
		print ex
		pass

if __name__ == "__main__":
	main()