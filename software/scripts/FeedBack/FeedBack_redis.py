from Adafruit_BBIO import ADC
from time import sleep
from redis import *
import socket, sys

ADC.setup()
client = StrictRedis(host = "127.0.0.1")

proportional = 12.2/2.2

VoltageFactor_ip = {
	'10.128.170.107': 100,
	'10.128.170.108': 1000,
	'10.128.170.109': 100,
	'10.128.170.110': 100,
	'10.128.170.111': 100,
	'10.128.170.112': 3000,
	'10.128.170.113': 1500,
	'10.128.170.116': 1500,
	'10.128.180.107': 1000,
	'10.128.180.108': 100,
	'10.128.180.109': 100,
	'10.128.180.110': 3000
}

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

my_ip = get_ip()

if my_ip == '127.0.0.1' or not(my_ip in VoltageFactor_ip):
    sys.exit()

else:
    voltage_factor = VoltageFactor_ip[my_ip]

while(True):
    analogInput = ADC.read("P9_39")*1.8
    
    client.set("AnalogVoltage:AN0", analogInput*proportional)
    sleep(2)

    client.set("SetPointVoltage:AN0", analogInput*proportional*voltage_factor)
    sleep(2)
