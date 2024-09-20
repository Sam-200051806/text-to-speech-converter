from gtts import gTTS
import os
from tkinter import *
te = open('file.txt','r').read()
langauge = 'en'
output = gTTS(text = te,lang = langauge,slow = False)
output.save('pagal.mp3')
os.system('start pagal.mp3')
