from gtts import gTTS
import os
te = open('file.txt','r').read()
langauge = 'en'
output = gTTS(text = te,lang = langauge,slow = False)
output.save('p.mp3')
os.system('start p.mp3')
