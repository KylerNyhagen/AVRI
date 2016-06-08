import sqlite3
import os
import avri_commands


def create_database():
    database_creation_connection = sqlite3.connect('avri_config.db')
    database_cursor = database_creation_connection.cursor()
    # Creating the programs table in which the programs name and location on the computer are stored
    database_cursor.execute('''CREATE TABLE programs (programname text PRIMARY KEY, location text)''')
    '''
    Creating the commands table in which it stores the program name, and the phrase to open it.
    program name is stored as a foreign key so we can have multiple phrases assigned to one program
    '''
    database_cursor.execute('''CREATE TABLE commands (programname text, phrase text, FOREIGN KEY(programname)
     REFERENCES programs(programname))''')
    database_creation_connection.close()


def connect_database():
    # If there is no database, create one
    if not os.path.isfile("avri_config.db"):
        create_database()
    # Create the connection of the database to be used in other functions as a global variable
    global conn
    conn = sqlite3.connect('avri_config.db')
    # Allow the cursor to be used in other functions as a global variable
    global c
    c = conn.cursor()


def add_program(program_name, program_executable):
    connect_database()
    programs = list(c.execute("SELECT location from programs WHERE programname = '" + program_name + "'"))

    # If it cannot find a program with that name in the database, it needs to find it's location
    if not programs:
        # Find the programs executable on the computer
        program_location = avri_commands.findProgram(program_executable)
        print(program_location)
        # Insert the program and it's location into the database
        c.execute("INSERT INTO programs VALUES('" + program_name + "', '" + program_location + "')")
    # Otherwise, the program already exists in the database, and we don't need to search for it.
    else:
        print('%s already exists in memory!' % program_name)
    print(programs)

    conn.commit()
    conn.close()


def add_command(program_name, command):
    connect_database()
    command = str(command).replace("'", "''")
    command_list = list(c.execute("SELECT phrase from commands WHERE programname = '" + program_name + "'"))
    print(command)
    print(command_list)
    if not command_list:
        c.execute("INSERT INTO commands VALUES('" + program_name + "', '" + command + "')")
    else:
        program_associated = list(c.execute("SELECT programname from commands WHERE phrase = '" + command + "'"))
        print("Command already exists in database. It is linked to the %s program" % program_associated[0])
    conn.commit()
    conn.close()