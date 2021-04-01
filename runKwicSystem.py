from Event import Event
import Constants
from time import time
from time import sleep

def runKwicSystem(form, lines, noiseWords):

	form.addEvent(Event(Constants.EVT_KWIC_STARTED))

	kwicLines = lines

	print('BEGAN')
	start = time()
	while time() - start <= 3:
		sleep(0)
		pass

	form.addEvent(Event(Constants.EVT_KWIC_DONE, kwicLines))

	print('ENDED')
