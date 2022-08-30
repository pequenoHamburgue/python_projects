import os

os.system('cls')
from moviepy.editor import *
username = os.getlogin()
path = os.chdir(f'C:\\Users\\{username}\\Desktop\\videos')#local automatico
videonome = str(input("Nome do VIDEO: "))
audionome = str(input("Nome do AUDIO: "))
video = VideoFileClip(videonome + ".mp4" )
video.audio.write_audiofile(audionome + ".mp3")

