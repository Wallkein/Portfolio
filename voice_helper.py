
import pyaudio
import speech_recognition as sr
import os
import pyttsx3
import random
import webbrowser


r = sr.Recognizer()
voice = pyttsx3.init()
voice.say("Здравствуйте, я ваш голосовой помощник")
voice.runAndWait()
mood = ["отлично", "хорошо", "нормально" , "плохо" , "не очень"]
films = ["Бойцовский клуб", "Джон Уик", "Назад в будущее", "Джон Картер", "Бэтмен"]

while True:
    with sr.Microphone() as source:
        print("Скажите что-нибудь...")
        audio = r.listen(source)

        speech = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали:", speech)

    if "привет" in speech:
        voice.say("И тебе привет")
        voice.runAndWait()
    elif "открой файл" in speech:
        voice.say("Хорошо, игра запущена")
        voice.runAndWait()
        os.startfile("E:/Riot Games/League of Legends/LeagueClient.exe")
    elif "как дела" in speech:
        voice.say(random.choice(mood))
        voice.runAndWait()    
    elif "посоветуй фильм" in speech:
        voice.say(random.choice(films))
        voice.runAndWait()
    elif "вконтакте" in speech:
        webbrowser.open_new("https://vk.com/im")
        voice.say("Хорошо, вконтакте запущен")
        voice.runAndWait()
    elif "youtube" in speech:
        webbrowser.open_new("https://www.youtube.com")
        voice.say("Хорошо, ютуб запущен")
        voice.runAndWait()
    elif "пока" in speech:
        voice.say("До свидания")
        voice.runAndWait()
        quit()
    else:
        voice.say("Я вас не понимаю, повторите пожалуйста")
        voice.runAndWait()
