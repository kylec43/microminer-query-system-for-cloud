from Event import Event
import Constants
from time import time
from time import sleep
import socket
from DatabaseController import DatabaseController

def fetchQueryResults(parent, inputData):

	databaseController = DatabaseController()
	queryResults = ""
	try:
		parent.addEvent(Event(Constants.EVT_SEARCH_STARTED))
		queryResults = databaseController.getQueryResults(inputData)
	except:
		parent.addEvent(Event(Constants.EVT_SEARCH_FAILURE))
		return
	
	parent.addEvent(Event(Constants.EVT_SEARCH_SUCCESS, queryResults))



