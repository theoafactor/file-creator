def saveData(data):
    from os.path import isfile
    #save the data
    ##check if the file exists
    if isfile("users.csv") == True:
        # the file exists already
        file = open("users.csv", "a")
        file.write("\n"+data["firstname"]+","+data["lastname"])
        file.close()
    else:
        # the file does not exist
        file = open("users.csv", "w")
        file.write("firstname,lastname\n")
        file.write(data["firstname"]+","+data["lastname"])
        file.close()



