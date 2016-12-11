# Import library and create instance of REST client.
from Adafruit_IO import Client

apikey = readAdafruitKey()
aio = Client(apikey)

def getSourceOption():
    
    ioOption = aio.receive('feed')
    sourceOption = float(ioOption.value)
    
    return sourceOption

def readAdafruitKey():
    #Read the Adafruit API key in from file /home/pi/apikey.txt.
    file = open('./adafruitKey.txt', 'r')
    apikey = file.readline().replace("\n", '')
    file.close()
    
    return apikey