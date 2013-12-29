import os
import signal
import sys
import time
from multiprocessing import Process

def main():
	jobs = []
	for root, dirs, files in os.walk('modules'):
        	for dir in dirs:
                	print dir
	                module = getattr(__import__("modules." + dir), dir)
        	        func = getattr(module, "main", None)
	                if func:
        	                p = Process(target=func)
	                        jobs.append(p)
	                        p.start()
        	dirs[:] = []  # don't recurse into directories.

	print jobs

	def signal_handler(signal, frame):
        	print "Got CTL+C"
	        for job in jobs:
        	        job.terminate()
        	        job.join()
		time.sleep(1)
	        sys.exit(0)

	signal.signal(signal.SIGINT, signal_handler)

