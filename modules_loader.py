# Singularity
# Copyright (C) 2014 Internet by Design Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
	        sys.exit(0)



	signal.signal(signal.SIGINT, signal_handler)

