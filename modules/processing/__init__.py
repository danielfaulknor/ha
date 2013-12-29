import sensors
import actuators
from multiprocessing import Process
import time

def signal_handler(signal, frame):
	print "Got CTL+C"
	time.sleep(1)
        for job in jobs:
        	job.terminate()
                job.join()
        sys.exit(0)

def main():
	try:
		jobs = []
		p = Process(target=sensors.main)
		p2 = Process(target=actuators.main)
	        jobs.append(p)
	        jobs.append(p2)
	        p.start()
        	p2.start()
		signal.signal(signal.SIGINT, signal_handler)
	except KeyboardInterrupt:
		pass



