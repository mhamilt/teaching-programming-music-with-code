# wav_library python example
# 
# run in terminal with:
# python main.py

from math import sin, pi
from wav_library_raw import *


if __name__ == "__main__":
    
    fs       = 44100.0   # Sampling Rate 
    f0       = 440.0     # Fundamental frequency
    duration = 1.0       # in seconds
    delta    = 2.0 * pi * f0 / fs # how much does the phase change between samples

    sine_wave = [sin(delta * i) for i in range(int(duration*fs))]
    
    write_wav_file(sine_wave, "a440")    
    audio = read_wav_file("a440.wav")
    write_wav_file(audio, "a440_read_test")