import speech_recognition as sr
import subprocess as subproc
import pyowm as weather

import comtypes as volChange
r = sr.Recognizer()
m = sr.Microphone()
owm = weather.OWM('c7bd9556b293d6b216a295062fdbb2dc')
try:
    print("Initalizing AVRI_Main V0.2 Alpha...")
    print("==============================")
    print("AVRI_Main commands developed by: Kyler Nyhagen")
    print("AVRI_Main Recognition based on: Google Speech Recognition")
    print("==============================")
    with m as source: r.adjust_for_ambient_noise(source)
    # What is this? print("Set minimum energy threshold to {}".format(r.energy_threshold))
    print("I'm online now sir, what do you require?")
    #All commands to open
    notePadList = ["let's take some notes", "give me some paper"]
    spotifyList = ["give me a beat", "let's listen to music"]

    while True:
        #print("Say something!")
        with m as source: audio = r.listen(source)
        #print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            valueAsTextPy2 = format(value).encode("utf-8").lower()
            val = format(value).lower()

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes: # this version of Python uses bytes for strings (Python 2)
                print(valueAsTextPy2)
            else: # this version of Python uses unicode for strings (Python 3+)
                print(val)

                if(val == "good morning avery"):
                    observation = owm.weather_at_place('Saskatoon, CA')
                    w = observation.get_weather()
                    print("Good morning sir, it is currently %s degrees in Saskatoon right now." %(w.get_temperature('celsius').get("temp")))
                #Checks if the user said anything in the note pad list, so it still let's them say "Hey Avery, Let's
                #Take some notes" instead of just saying "take some notes"
                elif(any(substring in val for substring in notePadList)):
                    print("Opening notepad for you, sir.")
                    subproc.call(['cmd.exe', '/c', 'start notepad++'])
                    #os.startfile(r'notepad++')
                elif(any(substring in val for substring in spotifyList)):
                    print("Opening Spotify for you, sir.")
                    subproc.call(["C:\\Users\\Kyler\\AppData\\Roaming\\Spotify\\Spotify.exe"])
                #TODO Launch Steam

                #TODO Launch Chrome

                #TODO Learn Commands

                #TODO Sleep command

        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
