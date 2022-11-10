import sys
import os
import time

import numpy as np
import matplotlib.pyplot as plt
import soundfile as snd

import librosa
import librosa.display

from PIL import Image

"""
generate audio from image taken as the spectrogram, inversion using Griffin Lim algorithm
"""

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description="generate audio from image taken as the spectrogram, inversion using Griffin Lim algorithm")
    parser.add_argument('--img', type=str,
                        required=True, help='filename of the input image')
    parser.add_argument('--wav', type=str,
                        required=True, help='filename of the output audio (wav)')
    parser.add_argument('--inv', action='store_false', help='swap gray image scale')
    parser.add_argument('--custom', action='store_true', help='custom settings for GL')

    args = parser.parse_args()

    # input image
    print('image to sound\n\n')
    image_path = args.img
    print(f'input image {image_path}')
    # output audio
    output_audio_path = args.wav
    print(f'output audio : {output_audio_path}')
    # audio sampling rate
    
    sr = 22050
    print(f'sampling rate : {sr} (preset)\n\n')

    # open image, transpose
    print('Image loading and pre-processing')
    tic = time.time()
    img = Image.open(image_path)
    img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    width, height = img.size
    print(f'original image size {width}, {height}')
    new_height = 1025  # 2048 fft window length = 93 ms, hop length 1024 = 46 ms
    new_width = int(round(width/height*new_height))
    # reshape
    D = np.array(img.resize((new_width, new_height), Image.Resampling.LANCZOS), dtype='float32')
    # print(D.shape)
    if D.ndim == 3:
        print(f'resampled image size {D.shape[0]}, {D.shape[1]}, {D.shape[2]}')
        # rgb => grayscale
        D = np.mean(D, axis=2)
    else:
        print(f'resampled image size {D.shape[0]}, {D.shape[1]}')
    # normalize, , small cst
    D /= 255.
    if args.inv:
        # invert black/white
        D = 1.-D + 1e-5
    print('')
    print(f'Elapsed time : {(time.time()-tic):.1f} sec')
    tic = time.time()
    print('compute audio signal from spectrogram image using Griffin-Lim algorithm')
    # compute audio signal from spectrogram using Griffin-Lim algorithm
    if args.custom:
        print('custom GL parameters')
        y_inv = librosa.griffinlim(D, n_iter=100, momentum=0.8)
    else:
        y_inv = librosa.griffinlim(D)  # default parameters
    # librosa.display.waveshow(y_inv, sr=sr)
    print(f'Elapsed time : {(time.time()-tic):.1f} sec')
    # save normalized audio
    tic = time.time()
    print(f'write audio : {output_audio_path}')
    snd.write(output_audio_path, y_inv/(np.max(np.abs(y_inv))+1e-5), sr)
    print(f'Elapsed time : {(time.time()-tic):.3f} sec')
