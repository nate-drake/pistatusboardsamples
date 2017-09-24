from gpiozero import PingServer, StatusBoard
from time import sleep

device = PingServer('192.168.1.29')
google = PingServer('google.com')

sb = StatusBoard('google', 'device')

while True:
    if google.is_active:
        sb.google.lights.green.blink()
    else:
        sb.google.lights.green.off()

    if device.is_active:
        sb.device.lights.green.on()
        sb.device.lights.red.off()
    else:
        sb.device.lights.green.off()
        sb.device.lights.red.on()
    sleep(3)
	
