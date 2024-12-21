import os
import random
import pyttsx3
import speech_recognition as sc
import datetime
import cv2
from requests import get
from wikipedia import summary
import webbrowser
import pywhatkit as kit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[1].id)

def spk(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def tc():
    i = sc.Recognizer()
    with sc.Microphone() as src:
        print("listening")
        i.pause_threshold = 0.5
        audio=i.listen(src,timeout=10,phrase_time_limit=10)
    try:
        print("Recognizing")
        query = i.recognize_google(audio, language='en-in')
        print(f"Boss Said:{query}")
        #spk(query)


    except Exception as e:
        spk("Say that Again Boss")
        return"none"
    return query

def wish():
    hr=datetime.datetime.now().hour

    if hr>=0 and hr<=12:
        spk("Good morning Boss")
    elif hr>12 and hr<=18:
        spk("good Afternoon Boss")
    else:
        spk("Good Evening Boss")
    spk("I am, Devil, how can i help you ?")


if __name__=="__main__":
    wish()
    #tc()
    #spk("Hi Boss")
    #while True:
    if 1:

        query = tc().lower()

        if "open notepad" in query:
            pth="C:\\Windows\\System32\\notepad.exe"
            os.startfile(pth)

        elif "open cmd"in query:
            os.system("start cmd")

        elif "open camera" in query:
            cp = cv2.VideoCapture(0)
            while True:
                ret, img = cp.read()
                cv2.imshow('webcam', img)
                k=cv2.waitKey(50)
                if k==27:
                    break
            cp.release()
            cv2.destroyAllWindows()

        elif"play song" in query or "play music" in query:
            music_dir="C:\\Users\\SHIVASAI\\Downloads\\songs"
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith(".mp3"):
                    os.startfile(os.path.join(music_dir,songs[0]))

        elif "play video" in query or "play movie" in query:
            vid_dir="C:\\Users\\SHIVASAI\\Downloads\\video"
            video = os.listdir(vid_dir)
            rd = random.choice(video)
            os.startfile(os.path.join(vid_dir,video[0]))

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            spk(f"your ip address is {ip}")

        elif "wikipedia" in query:
            spk("searching wikipedia...")
            query=query.replace("wikipedia","")
            results = summary(query, sentences=1)
            spk("According to wikipedia")
            spk(results)
            print(results)

        elif "youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "linkedin" in query:
            webbrowser.open("linkedin.com")

        elif "stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "google" in query:
                   spk("What do you need Boss")
                   goo = tc().lower()
                   webbrowser.open(f"'{goo}'")

        elif "send message" in query or "text" in query:
            kit.sendwhatmsg("+919113516754","HI AMMA",12,30)

