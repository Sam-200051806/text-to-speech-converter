from gtts import gTTS
import os
text = "Goodmorning Sir"
output = gTTS(text = text,lang = 'en',slow = True)
output.save('out.mp3')
os.system("start out.mp3")
