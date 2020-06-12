This feature extraction part is based on the library MyProsody. 
https://github.com/Shahabks/myprosody
The functions used from the library for this project are:
Gender recognition and mood of speech: Function myspgend(p,c)
Pronunciation posteriori probability score percentage: Function mysppron(p,c) 
eg. 
gender 			male/female
tone 			normal/reading/passionate
pronunciation score  	85.14

Steps: 
>> ssh aci-b.aci.ics.psu.edu
>> cd /gpfs/scratch/<username>/Additional audio features/
>> sh qsub.sh
>> module load python/3.6.3-anaconda5.0.1
>> module load ffmpeg/3.3.3
>> python  /gpfs/scratch/<username>/Additional audio features/Audios/extract_audios.py
>>  python  /gpfs/scratch/<username>/Additional audio features/Audios/new.py
>>  python  /gpfs/scratch/<username>/Additional audio features/myprosody-master/ myprosody_gender_tone.py
>>  python  /gpfs/scratch/<username>/Additional audio features/myprosody-master/ myprosody_pronunciation.py

How it works: 
*Please make the path changes in each of the codes*

In folder Audios, (with videoFiles.csv in the same folder)
1) extract_audios.py : Extract audio from the videoFiles.csv at sample rate 48 kHz and bit depth PCM_16
2) new.py: Convert the bit rate to PCM_32. (Library requirement)
The new audio files are stored in the myprosody audioFiles folder for feature extraction 

In myprosody-master folder, 
3) myprosody_gender_tone.py : Run to get the features in the myprosody_features_gender_tone.csv in the myprosody folder
4) myprosody_pronunciation.py : Run to get the features in the myprosody_features_pronunciation.csv in the myprosody folder

Note: It takes more compute power than the free 12 GB of Google colab. I run it on the PSU ACI Cyberlamp cluster which is our high-performance computing (HPC) infrastructure, with the following argument: Total CPUs = 4, 1 GPU and 8GB memory 
Please find myprosody_gender_tone.py and myprosody_pronunciation.py for the same and make the path changes accordingly. The in-built functions can be edited in the myprosody.py file for these  code files.(They are implemented in the features_extract.ipynb itself) 

