# wav_library
#
# To import, all students should have to type is 
#
# ```py
# from wav_library import *
# ```
#
# After which they will have access to the `write_wav_file` and `read_wav_file` functions
#
import struct
import wave
from math import sin, pi

def write_wav_file(float_data, filename, nchannels=1, bit_depth=16, sample_rate=44100):
    
    normalisation = 1 / max([abs(x) for x in float_data])
    
    float_data = [sample * normalisation for sample in float_data]
    
    if not filename.endswith('.wav'):
        filename += '.wav'
        
    with wave.open(filename, 'wb') as wave_file:
        wave_file.setnchannels(nchannels)
        wave_file.setsampwidth(bit_depth // 8)
        wave_file.setframerate(sample_rate)
                
        max_amplitude = (2 ** (bit_depth - 1) - 1)
        byte_data = b''.join([struct.pack('<h', int(sample * max_amplitude)) for sample in float_data])
        
        wave_file.writeframesraw(byte_data)

def read_wav_file(filename, return_params=False):

    if not filename.endswith('.wav'):
        filename += '.wav'
                
    with wave.open(filename, 'rb') as wave_file:
        p = wave_file.getparams()
        
        assert p.sampwidth == 2, f"{filename} file is not a 16-bit"
        
        frames = wave_file.readframes(p.nframes)
        
    bit_depth = 8 * p.sampwidth    
    max_amplitude = 2**(bit_depth-1) - 1
    audio_samples = [sample[0] / max_amplitude for sample in struct.iter_unpack('<h',frames)]

    if return_params:
        return audio_samples if p.nchannels == 1 else [audio_samples[channel::p.nchannels] for channel in range(p.nchannels)], p.framerate, bit_depth
    else:
        return audio_samples if p.nchannels == 1 else [audio_samples[channel::p.nchannels] for channel in range(p.nchannels)]
    
if __name__ == "__main__":
    fs       = 44100.0   # Sampling Rate 
    f0       = 440.0     # Fundamental frequency
    duration = 1.0       # in seconds

    delta    = 2.0 * pi * f0 / fs # how much does the phase change between samples
    sine_wave = [sin(delta * i) for i in range(int(duration*fs))]
    write_wav_file(sine_wave, "a440hz.wav")
    read_wav = read_wav_file("a440hz.wav")
    write_wav_file(read_wav, "a440hz_from_read.wav")    
