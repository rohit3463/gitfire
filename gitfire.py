import os
import sys
import configparser
from getpass import getuser
from serial import Serial
from  serial.serialutil import SerialException

def get_serial_port():
    return "/dev/"+os.popen("dmesg | egrep ttyACM | cut -f3 -d: | tail -n1").read().strip()

def getGitRepo():
    config = configparser.ConfigParser()
    config.read("/home/{0}/.config/gitfire.conf".format(getuser()))

    return config['DEFAULT']['yo']

def FireInTheHole():
    try:
        gitRepo = getGitRepo()
        sys.stdout.write(gitRepo)

    except KeyError:
        sys.stderr.write("Error in reading config file, Please Check")

try:
    ser = Serial(get_serial_port(), 9600)
    fire_state = '0'

    fire_state = ser.readline().decode("utf-8")

    if fire_state != '0':
        FireInTheHole()

except SerialException:
    sys.stderr.write("Arduino not connected to serial port")

finally:
    ser.close()