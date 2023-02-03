import speech_recognition as sr

r = sr.Recognizer()
# variable used to recognise speech

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=0.2)

    audio = r.listen(source)

    speech = r.recognize_google(audio)

    print(speech)
