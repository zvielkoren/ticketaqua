import os.path, os, json

def setvar(var, value, datafile): #defines the variable
    if not os.path.exists("./databases"):
        os.mkdir("./databases")
    if not datafile.endswith(".txt"):
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
    if not os.path.exists("./databases"):
        os.mkdir("./databases")
    if not datafile.endswith(".txt"):
        datafile = f"{datafile}.txt"
    if os.path.isfile(f"databases/{datafile}"):
        with open(f"databases/{datafile}", "r", encoding="UTF-8") as file:
            database=json.load(file)
        if database.get(f"{var}"):
            return database[f"{var}"]
        else:
            return "null"
    else:
        return "null"

def varexists(var, datafile): #checks if a variable exists
    if os.path.exists("./databases"):
        if not datafile.endswith(".txt"):
            datafile = f"{datafile}.txt"
        if os.path.isfile(f"databases/{datafile}"):
            with open(f"databases/{datafile}", "r", encoding="UTF-8") as file:
                database=json.load(file)
            if database[f"{var}"]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def dbexists(datafile): #checks if a database exists
    if not datafile.endswith(".txt"):
        datafile=f"{datafile}.txt"
    if os.path.exists("./databases"):
        if os.path.isfile(f"databases/{datafile}"):
            return True
        else:
            return False
    else:
        return False

def backupcreate(datafile, backupfile=None): #create backup for database
    if backupfile is None:
        backupfile=datafile
    if not os.path.exists("./databases"):
        os.mkdir("./databases")
    if not os.path.exists("./backups"):
        os.mkdir("./backups")
    if not datafile.endswith(".txt"):
        datafile=f"{datafile}.txt"
    if not backupfile.endswith(".txt"):
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
    if not os.path.exists("./databases"):
        os.mkdir("./databases")
    if not os.path.exists("./backups"):
        os.mkdir("./backups")
    if not datafile.endswith(".txt"):
        datafile=f"{datafile}.txt"
    if not backupfile.endswith(".txt"):
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
    if not os.path.exists("./backups"):
        return "backup not found."

    if not backupfile.endswith(".txt"):
        backupfile=f"{backupfile}.txt"

    if os.path.isfile(f"backups/{backupfile}"):
        os.remove(f"backups/{backupfile}")
        return f"{backupfile} was successfully deleted."
    else:
        return "backup not found."

def deletedb(database): #deletes database
    if not os.path.exists("./databases"):
        os.mkdir("./databases")
    if not database.endswith(".txt"):
        database=f"{database}.txt"
    if os.path.isfile(f"databases/{database}"):
        os.remove(f"databases/{database}")
        return f"{database} was deleted successfully."
    else:
        return "null"

def createdb(database): #creates a database
    if not os.path.exists("./databases"):
        os.mkdir("./databases")
    if not database.endswith(".txt"):
        database=f"{database}.txt"
    if os.path.isfile(f"databases/{database}"):
        return f"{database} was already created."
    else:
        with open(f"databases/{database}", "w", encoding="UTF-8") as file:
            file.write("{}")
        return f"{database} was created successfully."

def cleandb(database): #cleans the database
    if not os.path.exists("./databases"):
        os.mkdir("./databases")
    if not database.endswith(".txt"):
        database=f"{database}.txt"
    with open(f"databases/{database}", "w", encoding="UTF-8") as file:
        file.write("{}")
    return f"{database} was cleared successfully."

def dblist(): #returns you all databases
    if os.path.exists("./databases"):
        databases=""
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
    if not os.path.exists("./databases"):
        os.mkdir("./databases")
    if not datafile.endswith(".txt"):
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
    if not os.path.exists("./databases"):
        os.mkdir("./databases")
    if not datafile.endswith(".txt"):
        datafile=f"{datafile}.txt"
    if os.path.isfile(f"databases/{datafile}"):
        with open(f"databases/{datafile}", "r", encoding="UTF-8") as file:
            database=file.read()
        return database
    else:
        return "{}"

def deletevar(var, datafile): #deletes variable
    if os.path.exists("./databases"):
        pass
    else:
        os.mkdir("./databases")
    if not datafile.endswith(".txt"):
        datafile=f"{datafile}.txt"
    if os.path.isfile(f"databases/{datafile}"):
        with open(f"databases/{datafile}", "r", encoding="UTF-8") as file:
            database = json.load(file)
        if database[f"{var}"]:
            database.pop(var)
            database = str(database).replace("'", '"')
            with open(f"databases/{datafile}", "w", encoding="UTF-8") as file:
                file.write(f"{database}")
            return f"{var} was deleted successfully."
        else:
            return "null"
    else:
        return "null"