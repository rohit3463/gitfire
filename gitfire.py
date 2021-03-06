import os
import sys
import configparser
import git
from datetime import datetime
from getpass import getuser
from serial import Serial
from serial.serialutil import SerialException

def get_serial_port():
    return "/dev/"+os.popen("dmesg | egrep ttyACM | cut -f3 -d: | tail -n1").read().strip()

def getGitRepo():
    config = configparser.ConfigParser()
    config.read("/home/{0}/.config/gitfire.conf".format(getuser()))

    return config['DEFAULT']['GIT_FIRE_REPO']

def FireInTheHole():
    try:
        gitRepo = getGitRepo()
        sys.stdout.write(gitRepo)

        repo = git.Repo(gitRepo)
        branch = 'fire' + str(datetime.now())

        branch = branch.replace(" ", "+")
        branch = branch.replace(":", "-")

        repo.git.checkout('-b', branch)
        repo.git.add('-A')
        repo.git.commit('-m', 'Fire! Adding commiting all files')
        repo.git.push('origin', branch)

        sys.stdout.write("Pushed to remote branch: {0}".format(branch))

    except KeyError:
        sys.stderr.write("Error in reading config file, Please Check")
    
    else:
        repo.close()

try:
    with Serial(get_serial_port(), 9600) as ser:
        fire_state = '0'
        fire_state = ser.readline().decode("utf-8")

        if fire_state != '0':
            ser.write(b'1')
            sys.stdout.write("FIRE!!")
            FireInTheHole()

except SerialException:
    sys.stderr.write("Arduino not connected to serial port")