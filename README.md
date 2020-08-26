# Precision Learning Video Feature Extraction
+ **Executive Summary**
  + **The precision learning project is a collaborative effort among Penn State, University of Arkansas and Worcester Polytechnic Institute to deliver data-driven personalization solutions for math students using Internet-of-Videos. Penn State is tasked to extract video data and features for a causal awareness model to recommend personalized instructional videos**. The complete feature list can be viewed [here](https://docs.google.com/spreadsheets/d/15s320NfZuvPCBP2C8vm3HOuZnYAsJ-RErjmI8-0wgY0/edit#gid=0) together with all the descriptions of the features. Access will be granted when requested. 
    + Penn State has also built a prediting model to detect a video relevance to the skill code based on the extracted videos. Currently, the model has achieved the performance of 0.92 ROC-AUC. 
  + We targeted 185 videos based on the ASSISTments Grade 7 Math common core codes using youtube using API endpoints and have human annotaters verify them with binary labels 'Relevant' or 'Not Relevant'(ratio is 152:33 ). 
  + Based on video id or link, we extracted 14 meta features as below: 
    + 'Video id','cc_skill_code', 'code_desc', 'video_link', 'published_at', 'video_title','video_desc','channel_title','transcript',   'Views', 'Likes', 'Dislikes', 'Favorites', 'Comments'
   + Based on the transcript we extracted, we extracted 72 liguistic inquiry and word count features (LIWC) using the software [LIWC](https://liwcsoftware.onfastspring.com/). Please refer the detailed features and meanings to its website [LIWC dictionary ](http://liwc.wpengine.com/compare-dictionaries/).
  + Based on video id or link, we use Azure Face detection API to extract 44 visual features. They are below:
    + 'Profile faces','Front faces', 'blondVal','brownVal','redVal','blackVal','grayVal','otherVal','Smile','Headpose - Pitch',
        'Headpose - Roll','Headpose - Yaw','Gender','Age','Facialhair - Moustache','Facialhair - Beard','Facialhair - Sideburns','Glasses',
        'Emotion - Anger','Emotion - Contempt','Emotion - Disgust','Emotion - Fear','Emotion - Happiness','Emotion - Neutral','Emotion - Sadness','Emotion - Surprise','Blur - Blurlevel','Blur - Value','Exposure - Exposurelevel','Exposure - Value','Occlusion - Foreheadoccluded', 'Occlusion - Eyeoccluded', 'Occlusion - Mouthoccluded','Noise - Noiselevel','Noise - Value','Makeup - Eyemakeup','Makeup - Lipmakeup','Accessories - Type', 'Accessories - Confidence','Hair - Bald','Hair - Invisible','Front face','Side profile','Voice only'
  + Based on video id or link, we used 'pydub','librosa', 'speechRecognition' audio-specific packages to extract 4 5 audio features. They are 'median_flatness','count of number of 1s/total windows', 'pitch_tuning','wpm','Number of speakers'.
  + Based on video links, we downloaded all the 185 videos via package 'pytube3' and extracted frames per 30 seconds using 'csv2' package. Using Amazon Rekognition APIs, we detected the below top 20 objects from the frames of each video.
    + 'Text','Plot','Number','Symbol','Page','Word','Person','Diagram','Human','White Board','Document','Paper', 'Handwriting', 'Plan', 'Face','Driving License','Electronics','Flyer','Measurements','Alphabet'
  + We also created 25 derived features to better feature engineering for the detection model:
    + 'word_count_code_desc','char_count_code_desc','avg_word_code_desc','uppercase_code_desc','lowercase_code_desc','word_count_video_desc','char_count_video_desc','avg_word_video_desc','uppercase_video_desc','lowercase_video_desc','word_count_video_title','char_count_video_title','avg_word_video_title','uppercase_video_title','lowercase_video_title','codeVideoDesc_WC_dif','codeVideoDesc_CC_dif','codeVideoDesc_AvgW_dif','codeVideoDesc_UC_dif','codeVideoDesc_LC_dif','codeTitle_WC_dif','codeTitle_CC_dif','codeTitle_AvgW_dif','codeTitle_UC_dif','codeTitle_LC_dif'
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
