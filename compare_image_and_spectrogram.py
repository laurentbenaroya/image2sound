import sys

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use( 'tkagg')

import librosa
import librosa.display

from PIL import Image

"""
compare original image and the spectrogram of the generated audio
https://librosa.org/doc/main/auto_examples/plot_display.html
"""
 
if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description="compare original image and the spectrogram of the generated audio")
    parser.add_argument('--img', type=str,
                        required=True, help='filename of the input image')
    parser.add_argument('--wav', type=str,
                        required=True, help='filename of the output audio')

    args = parser.parse_args()
    img = Image.open(args.img)
    y, sr = librosa.load(args.wav)

    D = librosa.stft(y)  # STFT of y
    S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

    # plt.figure()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True)

    ax1.imshow(img)
    ax1.get_xaxis().set_visible(False)
    ax1.get_yaxis().set_visible(False)

    librosa.display.specshow(S_db, cmap='gray_r', ax=ax2, x_axis='time', y_axis='linear')

    ax1.set_title('original image')
    ax2.set_title('spectrogram of the audio')
    plt.show()
