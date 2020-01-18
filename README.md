# Quran-Reciter-Classifier
Classifying audio segments of four Quran reciters using fastai and pre-trained Resnet34 model

## Audio Processing & Dataset
The dataset consists of 4 mp3 files each file for a different reciter reciting the same Surah, each MP3 file is coverted to a mono-WAV audio file, and using librosa each audio file is segmented to 10-seconds segments and each segment is converted to a mel-spectogram image:

![Alt text](mp3/show_batch.png?raw=true "Title")

The file `dataset.py` creates the dataset using the above explained process in folder `dataset`

## Resnet34 Classifier
The classifier is created using pre-trained Resnet34 model (using fastai)

## Issues to check
Classifier is yielding 100% validation accuracy so I might have missed up somewhere.
