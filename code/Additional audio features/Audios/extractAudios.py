# 7.NS.A.1b / 7.NS.A.1c - Addition and Subtraction of Rational Numbers (Part 1 of 2) is repeated twice
# Hence you get only 184 videos

from __future__ import unicode_literals
import youtube_dl
import csv

ydl_opts = {
    
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '288'
    }],
    'postprocessor_args': [
        '-ar', '48000'
    ],
    'prefer_ffmpeg': True,
    'keepvideo': True
}

with open('./videoFiles.csv','r') as csvfile:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        readCSV = csv.reader(csvfile, delimiter=',')
        for videoStr in readCSV:
            videoFile = str(videoStr[0])
            print(videoFile)
            ydl.download([videoFile])