import sys

import numpy as np
import matplotlib.pyplot as plt

import librosa
import librosa.display

"""
display spectrogram using librosa library
https://librosa.org/doc/main/auto_examples/plot_display.html
"""
 
if len(sys.argv) < 2:
    print('Usage: display_spectrogram.py myaudio\nPlease provide an audio as argument')
    sys.exit()

y, sr = librosa.load(sys.argv[1])

D = librosa.stft(y)  # STFT of y
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

plt.figure()
librosa.display.specshow(S_db, cmap='gray_r')
plt.show()
