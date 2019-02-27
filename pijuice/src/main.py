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
    charge = pijuice.status.GetChargeLevel()		
    charge = charge['data'] if charge['error'] == 'NO_ERROR' else charge['error']
    print("Charge: %d" % (charge))

    fault =  pijuice.status.GetFaultStatus() 
    fault = fault['data'] if fault['error'] == 'NO_ERROR' else fault['error']
    print("Fault: %s"  % (fault))

    temp =  pijuice.status.GetBatteryTemperature()
    temp = temp['data'] if temp['error'] == 'NO_ERROR' else temp['error']
    print("Temperature: %dC"  % (temp))

    vbat = pijuice.status.GetBatteryVoltage()	        
    vbat = vbat['data'] if vbat['error'] == 'NO_ERROR' else vbat['error'] 
    print("Battery Voltage: %d V" % (vbat/1000))

    ibat = pijuice.status.GetBatteryCurrent()
    ibat = ibat['data'] if ibat['error'] == 'NO_ERROR' else ibat['error']
    print("Battery Current: %d I" % (ibat))
    
    vio =  pijuice.status.GetIoVoltage()
    vio = vio['data'] if vio['error'] == 'NO_ERROR' else vio['error']
    print("IO Voltage: %d I" % (vio))

    iio = pijuice.status.GetIoCurrent()
    iio = iio['data'] if iio['error'] == 'NO_ERROR' else iio['error'] 
    print("IO Current: %d I" % (iio))

    sleep(10)