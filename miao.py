import mp3play
import time

while True:
    filename = r'D:\Documents\Videos\1504.mp3'
    clip = mp3play.load(filename)

    clip.play()

    time.sleep(30)
    clip.stop()
