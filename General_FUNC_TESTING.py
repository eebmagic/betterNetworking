testMAC = "? (192.168.0.24) at 0:15:e9:4c:2:61 on en0 ifscope [ethernet]"

#Returns the mac address in the line
def getMAC(inputString):
	try:
		firstColon = inputString.index(':')
	except ValueError:
		return None
	start = inputString[firstColon-2:].strip()

	rawMAC = start[:start.index(' ')]

	#Correct spacing issue
	pairList = rawMAC.split(':')
	for i, pair in enumerate(pairList):
		if len(pair) < 2:
			pairList[i] = '0' + pair
	newMAC = ':'.join(pairList)

	return newMAC


print(getMAC(testMAC))