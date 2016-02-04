'''
Created on Feb 4, 2016

@author: travis elliott
'''
import time
#pass a standard ProXR command as an array to this function and it will return an api wrapped array you can pass to the Fusion Controller
def apiPacket(passedCommand):
    apiPacketReturn = []
    apiPacketReturn.append(170)
    apiPacketReturn.append(len(passedCommand))
    for i in range(0, len(passedCommand)):
        apiPacketReturn.append(passedCommand[i])
    
    checksum = 0
    for i in range(0, len(apiPacketReturn)):
        checksum = checksum + apiPacketReturn[i] 
    apiPacketReturn.append(checksum&255)  
    return apiPacketReturn                                               
    
command = [254, 108, 1]

while True:
    print command
    api = apiPacket(command)
    print api
    time.sleep(2)