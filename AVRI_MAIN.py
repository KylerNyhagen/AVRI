import speech_recognition as sr
import pyowm as weather
from avri_commands import *
import avri_db

#DATABASE TESTS
avri_db.connect_database()


# Silence feature - If this is false, AVRI will not speak.
avri_version = "0.2 Alpha"
canSpeak = False
r = sr.Recognizer()
m = sr.Microphone()
owm = weather.OWM('c7bd9556b293d6b216a295062fdbb2dc')
# TODO populate these lists with a database instead
# All commands to open various programs
notepad_list = ["let's take some notes", "give me some paper"]
spotify_list = ["give me a beat", "let's listen to music"]
steam_list = ["let's play some games", "open steam"]
try:

    print("Initializing AVRI_Main V%s" % avri_version)
    print("==============================")
    print("AVRI_Main commands developed by: Kyler Nyhagen")
    print("AVRI_Main Recognition based on: Google Speech Recognition")
    print("==============================")
    with m as source: r.adjust_for_ambient_noise(source)
    # What is this? print("Set minimum energy threshold to {}".format(r.energy_threshold))
    print("I'm online now sir, what do you require?")
    while True:
        #print("Say something!")
        with m as source: audio = r.listen(source)
        #print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            val = format(value).lower()


            print(val)

            if(val == "good morning avery"):
                observation = owm.weather_at_place('Saskatoon, CA')
                w = observation.get_weather()
                if(canSpeak):
                    speak("Good morning sir, it is currently %s degrees in Saskatoon right now." % (
                    w.get_temperature('celsius').get("temp")))
                print("Good morning sir, it is currently %s degrees in Saskatoon right now." % (
                    w.get_temperature('celsius').get("temp")))

            #Checks if the user said anything in the note pad list, so it still let's them say "Hey Avery, Let's
            #Take some notes" instead of just saying "take some notes"
            elif(any(substring in val for substring in notepad_list)):
                print("Opening notepad for you, sir.")
                #subprocess.call(['cmd.exe', '/c', 'start notepad++'])
                #os.startfile(r'notepad++')
            elif(any(substring in val for substring in spotify_list)):
                openprogram("Opening Spotify for you, sir.", '%appdata%\Spotify\Spotify.exe')
            elif(any(substring in val for substring in steam_list)):
                #TODO Get path for Steam
                openprogram("Opening Steam for you, sir.", "STEAM_LOCATION")
            #TODO Launch Chrome

            #TODO Learn Commands

            #TODO Sleep command

        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))

except KeyboardInterrupt:
    pass


