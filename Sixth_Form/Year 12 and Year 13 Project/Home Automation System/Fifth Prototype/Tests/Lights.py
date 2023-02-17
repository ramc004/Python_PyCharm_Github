import tinytuya

Bananas = tinytuya.BulbDevice(dev_id='bf8e3b5d5202077a15d42q',
                                                  address='192.168.1.129',
                                                  local_key='9d8233fcceacb8e6',
                                                  version=3.3)

data = Bananas.status()
print(data)
