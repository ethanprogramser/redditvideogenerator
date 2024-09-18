from moviepy.editor import *
import moviepy
import keyer
import random
from gtts import gTTS

ras = random.randint(0, 10)
random_file = "/videos/file" + str(ras)

li = keyer.get()


def create_audio_and_list():
    lisa = []
    for i in range(len(li)):
        ob = gTTS(text=li[i], lang='en', slow=False)
        ob.save(f"audio/texter{i}.mp3")
        lisa.append(f"audio/texter{i}.mp3")
    c1 = AudioFileClip(lisa[0])
    c2 = AudioFileClip(lisa[1])
    c3 = AudioFileClip(lisa[2])
    final = concatenate_audioclips([c1, c2, c3])
    final.write_audiofile("audio/complete.mp3")

create_audio_and_list()







