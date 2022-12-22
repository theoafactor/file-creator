def saveData(data):
    #save the data
    file = open("users.txt", "a")
    file.write("\n")  
    file.write(data)
    print("Data has been saved as " + data)