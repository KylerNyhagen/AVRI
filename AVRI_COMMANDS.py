import subprocess
import os
import re
import win32api
'''
Function called when user wants to open a program.
msg = What AVRI will output to the console
location = where the executable is in the users computer.
'''
def openprogram(msg, location):
    print(msg)
    subprocess.call(['cmd.exe', '/c', 'start notepad++'])

def findNotepad():
    #find_file_in_all_drives('notepad\+\+.exe')
    find_file_in_all_drives('Spotify.exe')


def find_file(root_folder, rex):
    for root,dirs,files in os.walk(root_folder):
        for f in files:

            result = rex.search(f)
            if result:
                print (os.path.join(root,f))
                break                         #if you want to find only one


def find_file_in_all_drives(file_name):
    #create a regular expression for the file
    rex = re.compile(file_name)
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        find_file( drive, rex )


