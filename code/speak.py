#this contains fxn that converts text  into audio and play it 


from gtts import gTTS
import pyglet
import time, os

def tts(text, lang):
    file = gTTS(text = text, lang = lang)
    filename = '/tmp/temp.mp3'
    file.save(filename)

	mixer.init()
    music = mixer.music.load(filename)#play audio
    mixer.music.play()


    #music = pyglet.media.load(filename, streaming = False)
    #music.play()

    #time.sleep(music.duration)
    #os.remove(filename)
