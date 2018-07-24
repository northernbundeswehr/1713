# restarts the ACTIVE server only

import os
import psutil
import subprocess
import signal

#pid2cpu = dict()
pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

for pid in pids:
	try:
		name = open(os.path.join('/proc', pid, 'cmdline'), 'r').read()
		if "1713.dmb" in name:
			if not "sudo" in name:

				# main server logic: for some reason I could get a valid string/int for port so we're just using "in"
				
				# 1713-1 is the active server; restart 1713-1
				if "12000" in name:
					if os.path.isfile("/home/customer/1713/1713-1/serverdata.txt"):
						process = psutil.Process(int(pid))
						if process != None:
							os.kill(int(pid), signal.SIGUSR1)
							print("Restarted ACTIVE server on port 12000.")
							
				# 1713-2 is the active server; restart 1713-2
				elif "12001" in name:
					if os.path.isfile("/home/customer/1713/1713-2/serverdata.txt"):
						process = psutil.Process(int(pid))
						if process != None:
							os.kill(int(pid), signal.SIGUSR1)
							print("Restarted ACTIVE server on port 12001.")
						
			 		  
	except IOError: # proc has already terminated
		continue

# what name ends up being, for reference - Kachnov 

#sudo1713.dmb12000-trusted-logself
#DreamDaemon1713.dmb12000-trusted-logself
#sudoDreamDaemon1713.dmb12001-trusted-logself
#DreamDaemon1713.dmb12001-trusted-logself

# also note os.getpid() to get our pid