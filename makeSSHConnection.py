import json
from pathlib import Path
import os
import sys
from subprocess import check_call, DEVNULL, STDOUT

# print(sys.argv)

user_PATH = str(Path.home())
JSON_PATH = user_PATH + "/pythonTools/betterNetworking/sources/data.json"

### Load ip dictionary ###
with open(JSON_PATH) as file:
	currentIpData = json.load(file)

if len(sys.argv) < 2:
	sys.argv.append('NONE')

destination = sys.argv[1]

if destination in currentIpData:
	### Ping to test connction ###
	try:
		response = check_call(['ping', '-c', '1', currentIpData[destination]['ip']], stdout=DEVNULL, stderr=STDOUT)
	except:
		response = 1
	if response == 0:
		print("Sending...")
	else:
		quit(f"###ERROR: Connection to {destination} ({currentIpData[destination]['user']}@{currentIpData[destination]['ip']}) has failed.")

	### RUN SSH COMMAND ###
	sendCommand = "ssh " + currentIpData[destination]['user'] + "@" + currentIpData[destination]["ip"]
	
	# print(f"Command to connect: {sendCommand}")
	
	os.system(sendCommand)


#If user input is not in ip dictionary
else:
	print("###ERROR: Desination not found")
	print("Desination options are: \n\t\t\t" + '\n\t\t\t'.join(currentIpData))
	quit("")