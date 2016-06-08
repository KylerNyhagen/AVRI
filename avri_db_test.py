from avri_db import *
from avri_commands import *
#add_program("notepad", "notepad\+\+.exe")
#add_command("notepad", "let's take some notes")
#proglocation = str(get_program_location("let''s take some notes"))
#print(proglocation)
openprogram("Opening notepad", get_program_location("let's take some notes"))
openprogram("Opening Spot-if-fy", '%appdata%\Spotify\Spotify.exe')