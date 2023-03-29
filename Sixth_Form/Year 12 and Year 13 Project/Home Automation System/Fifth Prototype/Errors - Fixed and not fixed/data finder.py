import tinytuya
# allows the library to be used to connect and pair the lights
Transformer = tinytuya.BulbDevice(dev_id='bf95a987949dd79c645dw7',
                                  address='192.168.1.155',
                                  local_key='021d37949f73862e',
                                  version=3.3)
# creates a new variable with the same name as the device being controlled for simplicity
# connects this variable to the tinytuya python library and works with the bulb device function
# passes through the dev id, the address, the local key and the version
# the dev id is found on the website
# the address, local key and version are found from terminal command
data = Transformer.status()
# calling a new variable using the variable just created for the light using the status function
print(data)
# data found for the lights status is shown in python console
