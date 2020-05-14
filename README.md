# Precision Learning Video Feature Extraction
+ Executive Summary
+ How to use this repo
  + code: contains code that extracts 2 sets of features: visual and audio features
    + for audio features script to run, you need audio files, we suggest go to the below link to download:
      + https://drive.google.com/open?id=1Ur__yHJafwUdpH4z9FPoCjbxblmIoiBB
    + for object detection script to run, you will need video and frames files, please use below link to download:
      + https://drive.google.com/open?id=1SJVvQ2n0Aa_5UFlzRc3YKD5JlhWzDYnK
      + https://drive.google.com/open?id=19blkP9GpsNYl94JRcYkBI9jO-XD20mDn
      + note that you can also use the video/frame download script to generate videos yourself
  + data: contain all the separate video feature files
    + the '185_row' folder contains files that shares the 'Video id' key
    + 'video_objects.csv' needs to be joined after mergining all the files from '185_row' with key 'Video title'
    
  + the 'all_features_cleaned.csv' file is the final with all the features merged before training for models
