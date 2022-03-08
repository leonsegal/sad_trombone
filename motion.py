import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import glob, sys, vlc, random

pir = 4
led = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pir, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

files = glob.glob("./*.mp3")

if len(files) == 0:
    # todo: flash led
    print("No mp3 files found. Exiting")
    sys.exit(1)

random.shuffle(files)

player = vlc.MediaPlayer()
media_list = vlc.MediaList(files)
media_list_player = vlc.MediaListPlayer()
media_list_player.set_media_player(player)
media_list_player.set_media_list(media_list)


def play_audio(channel):
    if media_list_player.is_playing():
        return
    print("Movement detected: " + str(datetime.now()))
    media_list_player.play()


print("Detecting...")

try:
    GPIO.add_event_detect(pir, GPIO.RISING, callback=play_audio)

    GPIO.output(led, GPIO.HIGH)

    while True:
        sleep(100)
except KeyboardInterrupt:
    print("Exiting...")

GPIO.cleanup()
