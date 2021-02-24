import mp3play

arquivo = r'C:\music.mp3'
clip = mp3play.load(arquivo)

clip.play()

import time
time.sleep(min(30, clip.seconds()))
clip.stop()