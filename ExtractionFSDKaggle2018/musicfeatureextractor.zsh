#!/bin/zsh
# essentia audio feature extraction for AudioKP
for file in /Users/homestudio/Downloads/EXTRACT_FSDKaggle2018.audio_train/*.wav
do
  ./essentia_streaming_extractor_music "$file" "${file%.wav}.yaml" 
done
