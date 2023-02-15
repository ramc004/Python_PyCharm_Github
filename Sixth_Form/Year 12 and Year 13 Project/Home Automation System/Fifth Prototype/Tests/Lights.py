import tinytuya

study_light_2 = tinytuya.BulbDevice(
      dev_id='bf57d83388422ac905nl4q',
      address='192.168.1.147',
      local_key='ed75d11af9d56a62',
      version=3.3)

study_light_2.set_colour(0, 255, 0)

