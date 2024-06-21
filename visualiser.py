import os
import sys
from os import listdir
from os.path import isfile, join
import wave
import inquirer
import numpy as np
import matplotlib.pyplot as plt

DEBUG = True

def dprint(*args, **kwargs):
    """ Debug print """
    if DEBUG:
        print(*args, **kwargs)



# mypath = os.path.dirname(os.path.realpath(__file__))
path = os.getcwd() + "/audio"

files = [f for f in listdir(path) if isfile(join(path, f))]

# dprint(files)

sys.path.append(os.path.realpath("."))

questions = [
    inquirer.List(
        "file",
        message="Which file should be used?",
        choices=files,
    ),
]

answers = inquirer.prompt(questions)

# dprint(answers)

wav_obj = wave.open(fr"audio\{answers['file']}", 'rb')

sample_freq = wav_obj.getframerate()
n_samples = wav_obj.getnframes()
signal_wave = wav_obj.readframes(n_samples)
signal_array = np.frombuffer(signal_wave, dtype=np.int16)
l_channel = signal_array[0::2]
r_channel = signal_array[1::2]
t_audio = n_samples/sample_freq
signal_wave = wav_obj.readframes(n_samples)

times = np.linspace(0, n_samples/sample_freq, num=n_samples)
plt.figure(figsize=(15, 5))
plt.plot(times, l_channel)
plt.title('Left Channel')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()

plt.figure(figsize=(15, 5))
plt.plot(times, r_channel)
plt.title('Right Channel')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()
