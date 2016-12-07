import requests
import time
import RPi.GPIO as io
import json

#set pin numbering to Broadcom internal numbering
io.setmode(io.BCM)

class Relay(object):
    pin = 0
    state = 0

    # The class "constructor" - It's actually an initializer 
    def __init__(self, pin, state):
        self.pin = pin
        self.state = state

relays = [None, None, None, None]

for relay in relays:
    relay = Relay(0,False)

#use software pin numbering
relays[0].pin = 17
relays[1].pin = 18
relays[2].pin = 21
relays[3].pin = 22

for relay in relays:
    #configure the pins to be used as outputs
    io.setup(relay.pin, io.OUT)
    #set inital pin states to off
    io.output(relay.pin, False)

displayOption = 0

#ready display options in from file

sources = getSources()

while():
    getData(sources[displayOption])
    
    #display LED for correstonsing label for displayOption
    displayOptionLED()
    
    #wait for 5 minutes to rerun the code
    time.sleep(300)

#Selecting which relay to turn on based on the limits
def displayStatus(numEvents, limit):
    print "The number of events is: " + numEvents + " of limit " + limit
    
    #if the traffic is less than 50% of limit 
    if (numEvents < (limit/2)):
        setRelays(0)
        
    elif (numEvents < (3*limit/4)):
        setRelays(1)
    
    elif (numEvents >= (3*limit/4)):
        setRelays(2)
		
    else: print "numEvents is out of bounds"

#turn on only the indicated relay
def setRelays(toggleRelay):
    for idx, relay in enumerate(relays):
        print(idx, relay)
        
        if idx == toggleRelay:
            print "Switching Relay " + toggleRelay + " On"
            relay.status = True
            io.output(relay.pin, True)
        else:
            print "Switching Relay " + toggleRelay + " Off"
            relay.status = False
            io.output(relay.pin, False)
    
#display led indicating which type of data is being displayed
def displayOptionLED():
    #set GPIO pin attached to specified pin high based on which option is displayed
    print "the currently selected data type is: " + sources[displayOption]['name']
    
    #code to cycle through the diferent display options (GA, Keen, etc). Reset after each loop
    if (displayOption == len(sources)): 
        displayOption = 0
    else: displayOption+=1
    
def getSources():
    with open('/home/pi/web-traffic-status-lights/sources.json') as sources_file:    
        sources = json.load(sources_file)
    
    print sources['sources']
    
    return sources['sources']
    
def getData(source):
    requestURL = source['requestURL']
    
    response = requests.get(requestURL)
    
    print response
    
    numEvents = response.source['payloadValue']
    
    limit = response.source['threshold']
    
    displayStatus(numEvents, limit)