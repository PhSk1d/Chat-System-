#import modules
import socket
import threading

HOST = '127.0.0.1'
PORT = 1234

def main():
	#creating a socket object
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	#connect to the server
	try:
		client.connect((HOST, PORT))
	except:
		print(f"Unable to connect server {HOST} {PORT}")
		
	
	
if __name__ == '__main__':
	main()
	
