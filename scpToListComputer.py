import json
from pathlib import Path
import sys
import os
from subprocess import check_call, DEVNULL, STDOUT

if len(sys.argv) < 3:
	quit("Not enough input:\n\tsend filepath destination")

user_PATH = str(Path.home())
JSON_PATH = user_PATH + "/pythonTools/betterNetworking/sources/data.json"

with open(JSON_PATH) as file:
	currentIpData = json.load(file)

if 'to' in sys.argv:
	sys.argv.remove('to')

file_to_send = sys.argv[1]
destination = sys.argv[2]


if destination in currentIpData:
	### Ping to test connction ###
	try:
		response = check_call(['ping', '-c', '1', currentIpData[destination]['ip']], stdout=DEVNULL, stderr=STDOUT)
	except:
		response = 1
	if response == 0:
		print("Sending...")
	else:
		quit(f"###ERROR: Connection to {destination} at {currentIpData[destination]['ip']} failed.")

	### RUN SCP COMMAND ###
	sendCommand = "scp -r '" + file_to_send + "' " + currentIpData[destination]['user'] + "@" + currentIpData[destination]["ip"] + ":" + currentIpData[destination]['folder']

	# print(f"SCP COMMAND: {sendCommand}")
	os.system(sendCommand)

elif destination == 'google':
    sendCommand = "rclone copy " + file_to_send + " Drive:/fromRclone/"
    os.system(sendCommand)

else:
	print("###ERROR: Desination not found")
	print("Desination options are: \n\t\t\t" + '\n\t\t\t'.join(currentIpData) + '\n\t\t\tgoogle')
	quit("")
