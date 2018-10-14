import serial
import os

def get_serial_port():
    return "/dev/"+os.popen("dmesg | egrep ttyACM | cut -f3 -d: | tail -n1").read().strip()

ser = serial.Serial(get_serial_port(), 9600)
fire_state = '0'

while fire_state == '0':
   fire_state = ser.readline().decode("utf-8")

print(fire_state)
