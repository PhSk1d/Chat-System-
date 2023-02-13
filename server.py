#modules
import socket
import threading

HOST = '127.0.0.1'
PORT = 1234
LISTENER_LIMIT = 5
active_clients = [] #list of currently connected to the server

#Function to listen for upcoming messages
def listen_for_messages(clients):
	while 1:
		response = client.recv(2048).decode('utf=8')

#function to send all new messages to client
#that are currently connected to the server
def send_messages_to_all(from_username, messages):
	
	#server will listen to the client
	#contain the username
	
	while 1:
		username = client.recv(2048).decode('utv=8')
		if username !='':
			active_clients.append((username, clients))
		else:
			print("Client username is empty")

#function handle to client
def client_handle(client):
	pass

def main():
	#creating the socket class object
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	#creating a try catch block
	try:
		server.bind((HOST, PORT))
		print(f"Running the server on {HOST} {PORT}")
	except:
		#provide the server with an adress in the form of
		#host IP and port
		print(f"Unable tk bind host (HOST) and port (PORT)")
		
		#set server limit
		server.listen(LISTENER_LIMIT)
		
		#this is a while loop will keep listening client connection
		while 1:
			
			client, address = server.accept()
			print(f"succesfully connected to client {address[0]} {address[1]}")
			
			threading.thread(target=client_handler, args=(client)).start()
	
if __name__ == '__main__':
	main()
	
