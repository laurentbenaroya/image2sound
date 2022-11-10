# image2sound
Encapsulate an image into an audio file.  
It uses the image as the spectrogram of the audio and recover the spectral phases through Griffin-Lim algorithm, using librosa package.

## pipenv installation
```bash
$ sudo apt install pipenv 
```
__OR__ if you don't have root priviledges (see https://pipenv.pypa.io/en/latest/install/)
```bash
$ pip install --user pipx
$ pip install --upgrade pip
$ pipx install pipenv
$ pip install --user pipenv
$ export PATH="/home/benaroya/.local/bin:$PATH"
```
You can add the export PATH in your ~/.bashrc  
*Note : pipenv problem : https://github.com/pypa/pipenv/issues/5052*
## Create project
```bash
$ pipenv --python 3.7
$ pipenv install
$ pipenv shell
```
## Go for it !!!

### audio generation
```bash
$ python image2sound.py -h
```
> usage: image2sound.py [-h] --img IMG --wav WAV [--inv] [--custom]
> generate audio from image taken as the spectrogram, inversion using Griffin-Lim algorithm (see https://librosa.org/doc/latest/generated/librosa.griffinlim.html for references to this algorithm)
> optional arguments:
  -h, --help  show this help message and exit
  --img IMG   filename of the input image
  --wav WAV   filename of the output audio (wav)
  --inv       swap gray image scale
  --custom    custom settings for GL

```bash
$ python image2sound.py --img images/signature_basique.jpg --wav audio/signature_basique.wav
```
try the options *--inv* (usefull when the image is mostly black) and *--custom* (try it for fun)

*play the audio using mplayer or audacity etc !!!*

### visualization and comparison
visualize the original image and the spectrogram from the output audio :
```bash
$ python compare_image_and_spectrogram.py --img images/signature_basique.jpg --wav audio/signature_basique.wav
```
### deactivate from pipenv virtual environment
```bash
deactivate
```
