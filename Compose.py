import smtplib
from email.message import EmailMessage
import speech_recognition as sr
import pyaudio
import sys
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time
print("-" * 60)
print("  Project: Voice based Email for Visually Challenged People")
print("-" * 60)
tts = gTTS(text=" Voice based Email for Visually Challenged People", lang='en')
ttsname = ("name.mp3")
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)
print("Compose a mail.")
tts = gTTS(text="Compose a mail.", lang='en')
ttsname = ("hello.mp3")
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)

smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.starttls()
senderemail_id="sangeethasangee1907@gmail.com"
senderemail_id_password="tnwhvjnthuvnnlep"
receiveremail_id="sangeechokki19300@gmail.com"
em=EmailMessage()
r = sr.Recognizer()  
with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        print("Your Subject :")
        tts = gTTS(text="Your Subject ", lang='en')
        ttsname = ("hello.mp3")
        tts.save(ttsname)

        music = pyglet.media.load(ttsname, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        audio = r.listen(source)
        print("ok done!!")
        tts = gTTS(text="ok done ", lang='en')
        ttsname = ("hello.mp3")
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
try:
        text1 = r.recognize_google(audio)
        print("Your Subject: " + text1)
        tts = gTTS(text=" Your Subject is"+text1, lang='en')
        ttsname = ("hello.mp3")
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        subject= text1
        em['subject']=subject
except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        tts = gTTS(text="Google Speech Recognition could not understand audio. ", lang='en')
        ttsname = ("hello.mp3")
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)

r = sr.Recognizer()  
with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        print("Your message :")
        tts = gTTS(text=" your message ", lang='en')
        ttsname = ("hello.mp3")
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        audio = r.listen(source)
        print("ok done!!")
        tts = gTTS(text="ok done ", lang='en')
        ttsname = ("hello.mp3")
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
try:
        text1 = r.recognize_google(audio)
        print("Your Message: " + text1)
        tts = gTTS(text=" Your Message is"+text1, lang='en')
        ttsname = ("hello.mp3")
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
        msg = text1
except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        tts = gTTS(text="Google Speech Recognition could not understand audio. ", lang='en')
        ttsname = ("hello.mp3")
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
em['From']=senderemail_id
em['To']=receiveremail_id
em.set_content(msg)
smtpobj.login(senderemail_id, senderemail_id_password)
smtpobj.sendmail(senderemail_id,receiveremail_id, em.as_string())
smtpobj.quit()
print ("Congratulation Your Mail send - Using simple text message")
tts = gTTS(text="Your Mail has been sent Successfully", lang='en')
ttsname = ("hello.mp3")
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)









