from Event import Event
import Constants
from time import time
from time import sleep
import socket

def fetchQueryResults(parent, inputData):

	queryResults = ""
	success = True
	try:
		parent.addEvent(Event(Constants.EVT_SEARCH_STARTED))


		inputData = inputData.encode('utf-8')


		SERVER_IP = 'localhost'  
		PORT = 12001

		#Create Client Socket
		client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print('created')
		client_socket.settimeout(10)

		#Connect to Server Socket
		client_socket.connect((SERVER_IP, PORT))
		client_socket.settimeout(10)

		#Send Message to Server
		client_socket.sendall(Constants.REQUEST_TYPE_QUERY)
		queryResults = client_socket.recv(100)
		client_socket.sendall(inputData)

		#Recieve a response from the Server
		client_socket.settimeout(120)
		queryResults = client_socket.recv(500000)
		print('Received:')
		if queryResults == Constants.SERVER_RESPONSE_QUERY_FAILURE:
			raise Exception('SEARCH FAILURE')

	except Exception as e:
		success = False
		print(e)
	finally:
		if success:
			parent.addEvent(Event(Constants.EVT_SEARCH_SUCCESS, queryResults.decode('utf-8')))
		else:
			parent.addEvent(Event(Constants.EVT_SEARCH_FAILURE))

		client_socket.close()

