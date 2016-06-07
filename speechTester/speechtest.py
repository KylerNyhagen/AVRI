import subprocess

#p = subprocess.Popen(["SpeakEasy.exe"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
#p.communicate(str.encode('\nTest\n'))
#p.communicate(str.encode('\nEXIT\n'))



#p = subprocess.Popen(["SpeakEasy.exe"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
#p.communicate(str.encode('\nSecond Test\n'))
#p.kill()

def speak(*commands):
    p = subprocess.Popen(["SpeakEasy.exe"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    p.communicate(str.encode('\n'.join(commands) + '\n'))

speak("test", "EXIT")

print("dsfsdafdsafsdfsadf")
print("dsfsdafdsafsdfsadf")
print("dsfsdafdsafsdfsadf")
print("dsfsdafdsafsdfsadf")
print("dsfsdafdsafsdfsadf")
print("dsfsdafdsafsdfsadf")
print("dsfsdafdsafsdfsadf")

speak("second test", "EXIT")