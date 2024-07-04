import speech_recognition as sr
import smtplib
import pyaudio
import sys
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time

print("2. Check your inbox")
tts = gTTS(text="Check your inbox", lang='en')
ttsname = ("hello.mp3")
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)

mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
unm = ('sangeethasangee1907@gmail.com')  
psw = ('tnwhvjnthuvnnlep')  
mail.login(unm, psw)  
stat, total = mail.select('Inbox')  
print("Number of mails in your inbox :" + str(total))
tts = gTTS(text="Total mails are :" + str(total), lang='en')  
ttsname = ("total.mp3")
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)

unseen = mail.search(None, 'UnSeen')  
print("Number of UnSeen mails :" + str(unseen))
result, data = mail.uid('search', None, "ALL")
inbox_item_list = data[0].split()
new = inbox_item_list[-1]
old = inbox_item_list[0]
result2, email_data = mail.uid('fetch', new, '(RFC822)')
raw_email = email_data[0][1].decode("utf-8")  
email_message = email.message_from_string(raw_email)
print("From: " + email_message['From'])
tts = gTTS(text="From :" + email_message['From'] , lang='en')
ttsname = ("mail.mp3")
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)
print("Subject: " + str(email_message['Subject']))
tts = gTTS(text="And Your subject: " + str(email_message['Subject']), lang='en')
ttsname = ("mail.mp3")
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)

stat, total1 = mail.select('Inbox')
stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
msg = data1[0][1]
soup = BeautifulSoup(msg, "html.parser")
txt = soup.get_text()
print("Body of Your Mail :" + txt)
tts = gTTS(text="Body of Your Mail: " + txt, lang='en')
ttsname = ("body.mp3")
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)
mail.close()
mail.logout()
