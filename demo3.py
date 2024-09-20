from gtts import gTTS
import os
te = open('file1.txt','r').read()
langauge = 'hi'
output = gTTS(text = te,lang = langauge,slow = False)
output.save('new.mp3')
os.system('start new.mp3')
