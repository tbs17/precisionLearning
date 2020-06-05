import myprosody as mysp
import pickle
import soundfile as sf
from soundfile import SoundFile
from pathlib import Path
import os
from os import path
import re
import glob
import pandas as pd
import parselmouth
import numpy as np
import csv
# path = '/gpfs/scratch/rfn5089/myprosody-master/myprosody/dataset/audioFiles' #Set path to audioFiles
path = '/gpfs/group/dul13/default/plearn/myprosody-master/myprosody/dataset/audioFiles'
audiodir= path
print(audiodir)

audioFiles=[]
for file in os.listdir(audiodir):
    if file.endswith('.wav'):
        afile=os.path.join(audiodir,file)
        audioFiles.append(file)
print(len(audioFiles))
audioFiles[:3]

# path='/gpfs/scratch/rfn5089/myprosody-master/myprosody' 
path = '/gpfs/group/dul13/default/plearn/myprosody-master/myprosody/'
os.chdir(path)
output = []

df = pd.DataFrame(data = output,columns = ['Video ids','Pronunciation score'])
#Outputs the values in the audio
df.to_csv('myprosody_features_pronunciation.csv')

with open('myprosody_features_pronunciation.csv', 'w', newline='') as csvfile:
  fieldnames = ['Video ids','Pronunciation score']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  # os.chdir('/gpfs/scratch/rfn5089/myprosody-master/myprosody/dataset/audioFiles')
  os.chdir('/gpfs/group/dul13/default/plearn/myprosody-master/myprosody/dataset/audioFiles')
  for i in range(len(audioFiles)): 
    p = audioFiles[i][:-4]
    temp = []
    c=r"/gpfs/group/dul13/default/plearn/myprosody-master/myprosody/" #an example of path to directory "myprosody" 
    if i%10==0:
        print(len(audioFiles)-i,'to go')
    score = mysp.mysppron(p,c)
    
    name = audioFiles[i][len(audioFiles[i])-15:-4]
    writer.writerow({'Video ids':name,'Pronunciation score':score})
