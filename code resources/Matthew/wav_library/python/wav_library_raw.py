# wav_library_raw
#
# Simple python library for writing wav files without using the wave module
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

def write_wav_file(audio, 
                   filename,
                   num_channels=1,
                   bits_per_sample=16,
                   sample_rate=44100,):
    
    number_of_samples = len(audio)
    chunk_id         = b'RIFF'                                             
    format           = b'WAVE'                                              
    sub_chunk_1_id   = b'fmt '                                             
    sub_chunk_1_size = 16                                                 
    audio_format     = 1                                                  
    sub_chunk_2_id   = b'data'                                             
    byte_rate        = sample_rate * num_channels * bits_per_sample // 8     
    block_align      = num_channels * bits_per_sample // 8                   
    sub_chunk_2_size = num_samples * num_channels * bits_per_sample // 8     
    chunk_size       = 4 + (8 + sub_chunk_1_size) + (8 + sub_chunk_2_size)

    with open(filename, 'wb') as wav_file:
        wav_file.write(struct.pack('4s', chunk_id))
        wav_file.write(struct.pack('<I', chunk_size))
        wav_file.write(struct.pack('4s', format))
        wav_file.write(struct.pack('4s', sub_chunk_1_id))
        wav_file.write(struct.pack('<I', sub_chunk_1_size))
        wav_file.write(struct.pack('<H', audio_format))
        wav_file.write(struct.pack('<H', num_channels))
        wav_file.write(struct.pack('<I', sample_rate))
        wav_file.write(struct.pack('<I', byte_rate))
        wav_file.write(struct.pack('<H', block_align))
        wav_file.write(struct.pack('<H', bits_per_sample))
        wav_file.write(struct.pack('4s', sub_chunk_2_id))
        wav_file.write(struct.pack('<I', sub_chunk_2_size))

        max_val = 2**15
        for sample in sine_wave:
            pcm_sample = int(sample * max_val)
            pcm_sample = max(-max_val, min((max_val-1), pcm_sample))  # Clamp to valid range
            wav_file.write(struct.pack('<h', pcm_sample))


def read_wav_file(filename):
    with open(filename, 'rb') as wav_file:                
        chunk_id,        = struct.unpack('4s', wav_file.read(4))
        chunk_size,      = struct.unpack('<I', wav_file.read(4))
        format,          = struct.unpack('4s', wav_file.read(4))
        subchunk1_id,    = struct.unpack('4s', wav_file.read(4))
        subchunk1_size,  = struct.unpack('<I', wav_file.read(4))
        audio_format,    = struct.unpack('<H', wav_file.read(2))
        num_channels,    = struct.unpack('<H', wav_file.read(2))
        sample_rate,     = struct.unpack('<I', wav_file.read(4))
        byte_rate,       = struct.unpack('<I', wav_file.read(4))
        block_align,     = struct.unpack('<H', wav_file.read(2))
        bits_per_sample, = struct.unpack('<H', wav_file.read(2))
        subchunk2_id,    = struct.unpack('4s', wav_file.read(4))
        subchunk2_size,  = struct.unpack('<I', wav_file.read(4))
            
        number_of_frames = subchunk2_size // (bits_per_sample // 8)

        max_amplitude = 2**15
        pcm = struct.unpack(f'<{subchunk2_size//2}h', wav_file.read())
        audio = [sample / max_value for sample in pcm]

    return audio