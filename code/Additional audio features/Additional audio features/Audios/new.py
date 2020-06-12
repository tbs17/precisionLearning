from __future__ import unicode_literals
import pickle
import myprosody as mysp
import soundfile as sf
from soundfile import SoundFile
from pathlib import Path
from os import path
import re
import glob
import youtube_dl
import csv
audioFiles = glob.glob("*.wav")

for i in range(len(audioFiles)): 
    n = audioFiles[i]
    data, samplerate = sf.read(audioFiles[i])
    name = '/gpfs/scratch/rfn5089/myprosody-master/myprosody/dataset/audioFiles/'+ n[:-4] +'.wav'
    sf.write(name, data, samplerate, subtype='PCM_32')
    p=SoundFile(name)
    if i%10==0:
      print(p)
print('Converted number of audios audios: ',i)