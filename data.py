import requests
import time
import RPi.GPIO as io 

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
    
    displayOptionLight(displayOption)
   
    requestURL = sources[displayOption][2]
    
    response = requests.get(requestURL)
    
    print response
    
    numEvents = response.sources[displayOption][3]
    
    limit = response.sources[displayOption][4]
    
    displayStatus(numEvents, limit)
    
    
    
    #display light for correstonsing label for displayOption
    displayOptionLight(displayOption, sources)
    
    #code to cycle through the diferent display options (GA, Keen, etc). Reset after each loop
    if (displayOption == len(sources)): 
        displayOption = 0
    else: displayOption+=1
    
    #wait for 5 minutes to rerun the code
    time.sleep(300)

#disyplay traffic data using relay
def displayStatus(numEvents, limit):
    print "The number of events is: " + numEvents + " of limit " + limit
    
    #if the traffic is less than 50% of limit 
    if (numEvents < (limit/2)):
        print("Switching Relay 0 On")
        relays[0].status = True
        io.output(relays[0].pin, True)
        relays[1].status = False
        io.output(relays[1].pin, False)
        relays[2].status = False
        io.output(relays[2].pin, False)
        
    elif (numEvents < (3*limit/4)):
        print("Switching Relay 1 On")
        relays[0].status = False
        io.output(relays[0].pin, False)
        relays[1].status = True
        io.output(relays[1].pin, True)
        relays[2].status = False
        io.output(relays[2].pin, False)
    
    elif (numEvents >= (3*limit/4)):
        print("Switching Relay 2 On")
        relays[0].status = False
        io.output(relays[0].pin, False)
        relays[1].status = False
        io.output(relays[1].pin, False)
        relays[2].status = True
        io.output(relays[2].pin, True)
		
    else: print "numEvents is out of bounds"
    
#display led indicating which type of data is being displayed
def displayOptionLight(displayOption, sources):
    #set GPIO pin attached to specified pin high based on which option is displayed
    print "the currently selected data type is: " + sources[displayOption][0]
    
    
def getAPIKey(filename):
    #read in API keys from file
    file = open('./' + filename , 'r')
    apikey = file.readline().replace("\n", '')
    file.close()
    return apikey
    
def getData(filename, ):
    temp = []
    sources = []
    
    count = 0
    
    #read in API keys from file
    #file = open('./data.txt', 'r')
    
    with open('./data.txt', 'r') as openfileobject:
        for line in openfileobject:
            if line == '':
                sources.append(temp)
                count = 0
            else: temp[count] = line
            
            count +=1
    
    
    #while ():
    #    temp[0] = file.readline().replace("\n", '')
    #    temp[1] = file.readline().replace("\n", '')
    #    #read in URL
    #    temp[2] = file.readline().replace("\n", '')
    #    #read in response value being looked for
    #    temp[3] = file.readline().replace("\n", '')
    #    dump = file.readline().replace("\n", '')
    #    sources.append(temp)
    
    file.close()
    return sources

def getSources():
    sources = []
    temp = []
    
    #read in API keys from file
    file = open('./sources.txt', 'r')
    while ():
        temp[0] = file.readline().replace("\n", '')
        temp[1] = file.readline().replace("\n", '')
        #read in URL
        temp[2] = file.readline().replace("\n", '')
        #read in response value being looked for
        temp[3] = file.readline().replace("\n", '')
        dump = file.readline().replace("\n", '')
        sources.append(temp)
    file.close()
    return sources