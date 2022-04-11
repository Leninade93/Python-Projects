# https://askubuntu.com/questions/663187/how-can-i-run-a-program-on-startup-minimized
# <script_filename> <command_to_run_the_application> <window_name>
# arg0 = path to script
# arg1 = application to run
# arg2 = window name

# Creating a flexible script that can be run at stratup to execute programs
# and minimize them based upon window name retrieved from wmctrl and minimized
# with xdotool

from curses import window
import subprocess, sys, time

# bash option -c will execute a command from a string, in this case string
# from sys.arg[1]
# this runs the program passed as an argument passed from CLI
subprocess.Popen(['/bin/bash', '-c', sys.argv[1]])


def parse_runningProcesses(window_name):
    try:
        # using checkoutput to run a command and return it's output
        # using wmctrl to list running windows with the -l option
        running_programs = subprocess.check_output(['wmctrl', '-l']).decode('utf-8').splitlines()
        # decode and splits lines are used for formatting the list
        for windows in running_programs:
            if window_name in windows:
                return running_programs[windows].split()
            else:
                print('ERROR! the provided window name is not listed as running')
                return None

    except(IndexError, subprocess.CalledProcessError):
        return None
        

# need to create a loop that will run the above function while giving some time
# for it execute successfully before searching for the window name through the list
# provided by wmctrl. xdotool will be called with subprocess to minimise this window
# one properly located

window_title = sys.argv[2]
time_measurement = 0
while time_measurement <= 30:
    program_name = parse_runningProcesses(window_title)
    time.sleep(0.1)
    if program_name != None:
        #subprocess.Popen(['xdotool', 'windowminmized', program_name])
        break # if successful while loop will exit here
    else:
        print('Time elapsed: ' + str(time_measurement))
    time.sleep(.9)
    time_measurement = time_measurement + 1
print('Timeout reached')

    

