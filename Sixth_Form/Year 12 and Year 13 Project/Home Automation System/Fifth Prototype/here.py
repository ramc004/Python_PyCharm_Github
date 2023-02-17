
study_light_2.set_socketPersistent(True)

print(" > Send Request for Status < ")
payload = study_light_2.generate_payload(tinytuya.DP_QUERY)
study_light_2.send(payload)

print(" > Begin Monitor Loop <")
while True:
    # See if any data is available
    data = study_light_2.receive()
    print('Received Payload: %r' % data)