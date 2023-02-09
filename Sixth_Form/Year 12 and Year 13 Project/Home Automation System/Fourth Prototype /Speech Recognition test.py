import speech_recognition as sr
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def find_weather():
    url = "https://www.google.co.uk/search?q=weather"
    find_weather_result = requests.get(url, headers=headers)

    soup = BeautifulSoup(find_weather_result.text, "html.parser")
    temperature = soup.select("#wob_tm")[0].getText().strip()
    weather_description = soup.select("#wob_dc")[0].getText().strip()
    return temperature, weather_description


def do_maths(maths_question):
    maths_question = maths_question.replace(" ", "+")
    url = "https://www.google.co.uk/search?q=%s" % maths_question
    do_maths_result = requests.get(url, headers=headers)
    soup = BeautifulSoup(do_maths_result.text, "html.parser")
    answer = soup.select("#cwos")[0].getText().strip()
    return answer


r = sr.Recognizer()
# variable used to recognise speech

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=0.2)
    print("Speak now")
    audio = r.listen(source)

    speech = r.recognize_google(audio)

    print("You said: " + speech)
    if "weather" in speech:
        tempValue, description = find_weather()
        print(tempValue + " degree celsius", description)
    if "calculator" in speech:
        r.adjust_for_ambient_noise(source, duration=0.2)
        print("Ask your question")

        questionAudio = r.listen(source)
        question = r.recognize_google(questionAudio)

        result = do_maths(question)
        print(result)

