import tinytuya

Transformer = tinytuya.BulbDevice(dev_id='bf95a987949dd79c645dw7',
                                  address='192.168.1.155',
                                  local_key='021d37949f73862e',
                                  version=3.3)

data = Transformer.status()
print(data)
