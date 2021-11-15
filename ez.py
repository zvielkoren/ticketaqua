import os.path, os, json, discord

def setvar(var, value, datafile): #defines the variable
    if not os.path.exists('./databases'):
        os.mkdir("./databases")
    if not datafile.endswith('.txt'):
        datafile=f"{datafile}.txt"
    if os.path.isfile(f"databases/{datafile}"):
        with open(f"databases/{datafile}", "r", encoding="UTF-8") as file:
            database = json.load(file)
    else:
        database={}
    database[var]=f"{value}"
    database=str(database).replace("'", '"')
    with open(f"databases/{datafile}", "w", encoding="UTF-8") as file:
        file.write(f"{database}")
    return f"{var} was successfully set to {value}."

def getvar(var, datafile): #returns the value of the variable
    if not os.path.exists('./databases'):
        os.mkdir("./databases")
    if not datafile.endswith('.txt'):
        datafile = f"{datafile}.txt"
    if os.path.isfile(f"databases/{datafile}"):
        with open(f"databases/{datafile}", "r", encoding="UTF-8") as file:
            database=json.load(file)
        if database.get(f"{var}"):
            return database[f"{var}"]
        else:
            return 'null'
    else:
        return 'null'

def varexists(var, datafile): #checks if a variable exists
    if os.path.exists('./databases'):
        if not datafile.endswith('.txt'):
            datafile = f"{datafile}.txt"
        if os.path.isfile(f"databases/{datafile}"):
            with open(f"databases/{datafile}", "r", encoding="UTF-8") as file:
                database=json.load(file)
            if database.get(f"{var}"):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def dbexists(datafile): #checks if a database exists
    if not datafile.endswith('.txt'):
        datafile=f"{datafile}.txt"
    if os.path.exists('./databases'):
        if os.path.isfile(f"databases/{datafile}"):
            return True
        else:
            return False
    else:
        return False

def backupcreate(datafile, backupfile=None): #create backup for database
    if backupfile is None:
        backupfile=datafile
    if not os.path.exists('./databases'):
        os.mkdir("./databases")
    if not os.path.exists('./backups'):
        os.mkdir("./backups")
    if not datafile.endswith('.txt'):
        datafile=f"{datafile}.txt"
    if not backupfile.endswith('.txt'):
         backupfile = f"{backupfile}.txt"
    if os.path.isfile(f"databases/{datafile}"):
        with open(f"databases/{datafile}", "r", encoding="UTF-8") as file:
            database = file.read()
        with open(f"backups/{backupfile}", "w", encoding="UTF-8") as file:
            file.write(database)
        return f"{database}'s backup was successfully created."
    else:
        return "database not found."

def loadbackup(datafile, backupfile=None): #loads backup to file
    if backupfile is None:
        backupfile=datafile
    if not os.path.exists('./databases'):
        os.mkdir("./databases")
    if not os.path.exists('./backups'):
        os.mkdir("./backups")
    if not datafile.endswith('.txt'):
        datafile=f"{datafile}.txt"
    if not backupfile.endswith('.txt'):
        backupfile=f"{backupfile}.txt"
    if os.path.isfile(f"databases/{datafile}"):
        if os.path.isfile(f"backups/{backupfile}"):
            with open(f"backups/{backupfile}", "r", encoding="UTF-8") as file:
                database = file.read()
            with open(f"databases/{datafile}", "w", encoding="UTF-8") as file:
                file.write(database)
            return f"successfully loaded backup to {datafile}."
        else:
            return "backup not found."
    else:
        return "database not found."

def deletebackup(backupfile): #deletes backup
    if not os.path.exists('./backups'):
        return "backup not found."

    if not backupfile.endswith('.txt'):
        backupfile=f"{backupfile}.txt"

    if os.path.isfile(f"backups/{backupfile}"):
        os.remove(f"backups/{backupfile}")
        return f"{backupfile} was successfully deleted."
    else:
        return "backup not found."

def deletedb(database): #deletes database
    if not os.path.exists('./databases'):
        os.mkdir("./databases")
    if not database.endswith('.txt'):
        database=f"{database}.txt"
    if os.path.isfile(f"databases/{database}"):
        os.remove(f"databases/{database}")
        return f"{database} was deleted successfully."
    else:
        return "null"

def createdb(database): #creates a database
    if not os.path.exists('./databases'):
        os.mkdir("./databases")
    if not database.endswith('.txt'):
        database=f"{database}.txt"
    if os.path.isfile(f"databases/{database}"):
        return f"{database} was already created."
    else:
        with open(f"databases/{database}", "w", encoding="UTF-8") as file:
            file.write("{}")
        return f"{database} was created successfully."

def cleandb(database): #cleans the database
    if not os.path.exists('./databases'):
        os.mkdir("./databases")
    if not database.endswith('.txt'):
        database=f"{database}.txt"
    with open(f"databases/{database}", "w", encoding="UTF-8") as file:
        file.write("{}")
    return f"{database} was cleared successfully."

def dblist(): #returns you all databases
    if os.path.exists('./databases'):
        databases=''
        dbnumber=0
        for file in os.listdir("./databases"):
            dbnumber+=1
            databases=f"{databases}\n{file}"
        databases=f"{dbnumber} databases\n{databases}"
    else:
        os.mkdir("./databases")
        databases=f"0 databases"
    return databases

def listdb(datafile): #returns all the variables and their value in the database
    if not os.path.exists('./databases'):
        os.mkdir("./databases")
    if not datafile.endswith('.txt'):
        datafile=f"{datafile}.txt"
    if os.path.isfile(f"databases/{datafile}"):
        with open(f"databases/{datafile}", "r", encoding="UTF-8") as file:
            database=json.load(file)
        variables=""
        variablesnum=0
        for variable in database:
            variables=f"{variables}\n{variable}: {database[variable]}"
            variablesnum+=1
    variables=f"{variablesnum} vriables\n{variables}"
    return variables

def printdb(datafile): #returns you everything in the database
    if not os.path.exists('./databases'):
        os.mkdir("./databases")
    if not datafile.endswith('.txt'):
        datafile=f"{datafile}.txt"
    if os.path.isfile(f"databases/{datafile}"):
        with open(f"databases/{datafile}", "r", encoding="UTF-8") as file:
            database=file.read()
        return database
    else:
        return "{}"

def deletevar(var, datafile): #deletes variable
    if os.path.exists('./databases'):
        pass
    else:
        os.mkdir("./databases")
    if not datafile.endswith('.txt'):
        datafile=f"{datafile}.txt"
    if os.path.isfile(f"databases/{datafile}"):
        with open(f"databases/{datafile}", "r", encoding="UTF-8") as file:
            database = json.load(file)
        if database.get(f"{var}"):
            database.pop(var)
            database = str(database).replace("'", '"')
            with open(f"databases/{datafile}", "w", encoding="UTF-8") as file:
                file.write(f"{database}")
            return f"{var} was deleted successfully."
        else:
            return "null"
    else:
        return "null"

def fileexists(file): #checks if a file exists
    if os.path.isfile(file):
        return True
    else:
        return False

def folderexists(folder): #checks if a folder exists
    if os.path.isdir(folder):
        return True
    else:
        return False

def deletefile(file): #deletes file
    if not file.endswith('.txt'):
        file=f"{file}.txt"
    if os.path.isfile(file):
        os.remove(file)
        return f"{file} was successfully deleted."
    else:
        return "file not found."

def has_perms(user: discord.User, perm):
    if perm=="create_instant_invite":
        if user.guild_permissions.create_instant_invite:
            return True
        else:
            return False
    if perm=="kick_members":
        if user.guild_permissions.kick_members:
            return True
        else:
            return False
    if perm=="ban_members":
        if user.guild_permissions.ban_members:
            return True
        else:
            return False
    if perm=="administrator" or perm=="admin":
        if user.guild_permissions.administrator:
            return True
        else:
            return False
    if perm=="manage_channels":
        if user.guild_permissions.manage_channels:
            return True
        else:
            return False
    if perm=="manage_guild":
        if user.guild_permissions.manage_guild:
            return True
        else:
            return False
    if perm=="add_reactions":
        if user.guild_permissions.add_reactions:
            return True
        else:
            return False
    if perm=="view_audit_log":
        if user.guild_permissions.view_audit_log:
            return True
        else:
            return False
    if perm=="priority_speaker":
        if user.guild_permissions.priority_speaker:
            return True
        else:
            return False
    if perm == "stream":
        if user.guild_permissions.stream:
            return True
        else:
            return False
    if perm == "read_messages":
        if user.guild_permissions.read_messages:
            return True
        else:
            return False
    if perm=="view_channel":
        if user.guild_permissions.view_channel:
            return True
        else:
            return False
    if perm=="send_messages":
        if user.guild_permissions.send_messages:
            return True
        else:
            return False
    if perm=="send_tts_messages":
        if user.guild_permissions.send_tts_messages:
            return True
        else:
            return False
    if perm=="manage_messages":
        if user.guild_permissions.manage_messages:
            return True
        else:
            return False
    if perm=="embed_links":
        if user.guild_permissions.embed_links:
            return True
        else:
            return False
    if perm=="attach_files":
        if user.guild_permissions.attach_files:
            return True
        else:
            return False
    if perm=="read_message_history":
        if user.guild_permissions.read_message_history:
            return True
        else:
            return False
    if perm=="mention_everyone":
        if user.guild_permissions.mention_everyone:
            return True
        else:
            return False
    if perm=="external_emojis":
        if user.guild_permissions.external_emojis:
            return True
        else:
            return False
    if perm=="use_external_emojis":
        if user.guild_permissions.use_external_emojis:
            return True
        else:
            return False
    if perm=="view_guild_insights":
        if user.guild_permissions.view_guild_insights:
            return True
        else:
            return False
    if perm=="connect":
        if user.guild_permissions.connect:
            return True
        else:
            return False
    if perm=="speak":
        if user.guild_permissions.speak:
            return True
        else:
            return False
    if perm=="mute_members":
        if user.guild_permissions.mute_members:
            return True
        else:
            return False
    if perm=="deafen_members":
        if user.guild_permissions.deafen_members:
            return True
        else:
            return False
    if perm=="move_members":
        if user.guild_permissions.move_members:
            return True
        else:
            return False
    if perm=="use_voice_activation":
        if user.guild_permissions.use_voice_activation:
            return True
        else:
            return False
    if perm=="change_nickname":
        if user.guild_permissions.change_nickname:
            return True
        else:
            return False
    if perm=="manage_nicknames":
        if user.guild_permissions.manage_nicknames:
            return True
        else:
            return False
    if perm=="manage_permissions" or perm=="manage_roles":
        if user.guild_permissions.manage_permissions:
            return True
        else:
            return False
    if perm=="manage_webhooks":
        if user.guild_permissions.manage_webhooks:
            return True
        else:
            return False
    if perm=="manage_emojis":
        if user.guild_permissions.manage_emojis:
            return True
        else:
            return False
    if perm=="use_slash_commands":
        if user.guild_permissions.use_slash_commands:
            return True
        else:
            return False
    if perm=="request_to_speak":
        if user.guild_permissions.request_to_speak:
            return True
        else:
            return False