from data_collection import collect
from greetings import greeting_mod
from user_data import save_data

## call the sayHello method of greeting_mod module
data = greeting_mod.sayHello(collect.username)

# save the data to a file
save_data.saveData(data)



