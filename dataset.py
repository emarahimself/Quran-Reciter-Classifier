import glob
import math
import os
import pydub
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt


def spectogram(audio_path):
    qari = os.path.basename(path).replace('.wav', '')
    samples, sample_rate = librosa.load(audio_path)
    duration = math.floor(librosa.core.get_duration(samples, sample_rate))
    duration -= duration % 10
    offset = 0
    while offset < duration:
        samples, sample_rate = librosa.load(audio_path, offset=offset, duration=10)
        S = librosa.feature.melspectrogram(samples, sample_rate)
        librosa.display.specshow(librosa.power_to_db(S, ref=np.max), fmax=np.max, fmin=0)
        offset += 10
        filename = 'dataset/'+qari+'_{}.png'.format(offset)
        plt.savefig(filename, dpi=75, bbox_inches='tight', pad_inches=0)
        print('File {} has been saved.'.format(filename))
        plt.close('all')


# Get list of files in 'quran` folders, each file represent the Qare'
print('Reading MP3 Files')
mp3_files = glob.glob('.\mp3\*.mp3')

# Convert each file from mp3 to Mono WAV
for path in mp3_files:
    fullpath = os.path.abspath(path)
    print('converting {}'.format(fullpath))
    qari = os.path.basename(path).replace('.mp3', '')

    sound = pydub.AudioSegment.from_mp3(fullpath)
    # Stereo to Mono
    sound.set_channels(1)
    sound.export(r'dataset/{}.wav'.format(qari))


# Get list of all WAV files
wav_files = glob.glob('.\dataset\*.wav')

# For each file create the 10-seconds spectogram images
print('Creating 10-second Spectograms')
for path in wav_files:
    spectogram(path)
