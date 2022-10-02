from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
import moviepy.editor as mp
import os
import math


def audio_duration(length):
    hours = length // 3600  # calculate in hours
    length %= 3600
    mins = length // 60  # calculate in minutes
    length %= 60
    seconds = length  # calculate in seconds
    return [hours, mins, seconds]  # returns the duration


def createNewVideoNote(pathVideoIn:str,pathVideoOut:str,pathAudio:str):
    mov = VideoFileClip(pathVideoIn)
    aud = AudioFileClip(pathAudio)
    timeVid = mov.duration
    timeAud = aud.duration

    print(f"{timeVid}==={timeAud}")

    if(timeAud<=timeVid):
        mov = mov.subclip(0, timeAud)
    elif (timeAud>timeVid):
        final = mov
        for i in range(math.ceil(timeAud/timeVid)):
            mov = mp.concatenate_videoclips([final,mov])
        mov = mov.subclip(0, timeAud)

    mov.audio = aud
    mov.write_videofile(pathVideoOut)


def gifToMP4(path:str):
    name = path[path.find("/")+1:path.find(".")]
    clip = VideoFileClip(path)

    clip.write_videofile(f"video/{name}.mp4")
    clip.close()

    clip = mp.VideoFileClip(f"video/{name}.mp4")
    # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
    clip_resized = clip.resize( height=340)
    clip_resized.write_videofile(f"video/{name}.mp4")


def resize(path:str):
    for file in os.listdir(path):
        clip = mp.VideoFileClip(f"EmojiMp4/{file}")
        clip_resized = clip.resize(
            height=340)  # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
        clip_resized.write_videofile(f"OutEmojiMp4/{file}",fps=120)

    #gifToMP4(f"GIF/{str(file)}")
