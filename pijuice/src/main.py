from time import sleep
import sys, getopt, os

sys.path.append('/usr/lib/python3.5/dist-packages') # temporary hack to import the piJuice module

from pijuice import PiJuice

while not os.path.exists('/dev/i2c-1'):
    print ("Waiting to identify PiJuice")
    time.sleep(0.1)

pijuice = PiJuice(1,0x14)

#while True:
status = pijuice.status.GetStatus()
status = status['data'] if status['error'] == 'NO_ERROR' else status['error']
print (status)

while True:
    print("All good!")
    sleep(10)