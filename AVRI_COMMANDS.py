import subprocess
import os
import re
import win32api
import sqlite3
'''
Function called when user wants to open a program.
msg = What AVRI will output to the console
location = where the executable is in the users computer.
'''
def openprogram(msg, location, alias="none"):
    command = '"' + alias + '" "'  + location + '"'
    print(command)
    if(alias == "none"):
        subprocess.call(['cmd.exe', '/c', location])




'''
Calls methods needed to find the executables for AVRI's program
opening commands

programName = The executable name of the program, to be passed in as,
for example "Spotify.exe"
'''
def findProgram(programName):
    #find_file_in_all_drives('notepad\+\+.exe')
    fileFound = find_file_in_all_drives(programName)
    return fileFound
'''
searches for the file given the root folder (C:\, D:\)
 and a file name as a regular expression

root_folder = the root directory such as c or d
rex = the file name as a regular expression
'''
def find_file(root_folder, rex):
    #Loop through all the directories and files in the root folder using walk
    for root,dirs,files in os.walk(root_folder):
        #Checks all the files within the list of files
        for f in files:
            #Check to see if the file is the same as the regex of the executable
            #We're looking for
            result = rex.search(f)
            #If we found it, print it out
            #Couldn't we just use "if rex.search(f):"?
            if result:
                #Output the path of the file
                return os.path.join(root,f)

'''
compiles the file name as a regex, and loops
through all the drives searching for the file

file_name = which file we're looking for
'''
def find_file_in_all_drives(file_name):
    #create a regular expression for the file
    rex = re.compile(file_name)
    #loops through the list of every drive the user has
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        fileDirectory = find_file( drive, rex )
        if(not fileDirectory is None):
            return fileDirectory



