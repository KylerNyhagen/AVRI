import sqlite3
import AVRI_COMMANDS
#notepadLocation = AVRI_COMMANDS.findProgram("notepad\+\+.exe")
#print(notepadLocation)
conn = sqlite3.connect('dbtest.db')
notepadLocation = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"

c = conn.cursor()

c.execute('''CREATE TABLE programs (programname text PRIMARY KEY, location text)''')
c.execute("INSERT INTO programs VALUES('spotify', '%appdata%\Spotify\Spotify.exe')")
c.execute("INSERT INTO programs VALUES('notepad', '" + notepadLocation + "')")
c.execute('''CREATE TABLE commands (programname text, phrase text, FOREIGN KEY(programname) REFERENCES programs(programname))''')
c.execute("INSERT INTO commands VALUES('spotify', 'give me a beat')")
c.execute("INSERT INTO commands VALUES('notepad', 'let''s take some notes')")
c.execute("INSERT INTO commands VALUES('notepad', 'write something down')")

spotifyLink = str(c.execute("SELECT location from programs WHERE programname = (SELECT programname from commands WHERE phrase = 'give me a beat')").fetchone())
spotifyLink = spotifyLink.replace(',','').replace("'", "", 2)[1:-1]
notepadLink = str(c.execute("SELECT location from programs WHERE programname = (SELECT programname from commands WHERE phrase = 'let''s take some notes')").fetchone())
notepadLink = notepadLink.replace(',','').replace("'", "", 2)[1:-1]
print(notepadLink)
notepadCommands = list(c.execute("select phrase from commands WHERE programname = 'notepad'"))
AVRI_COMMANDS.openprogram("notepad", notepadLink)

conn.commit()
conn.close()