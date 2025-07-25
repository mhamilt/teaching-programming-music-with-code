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

def write_wav_file(audio, filename):
    num_channels = 1
    bits_per_sample = 16
    sample_rate = 44100
    number_of_frames = len(audio)
    byte_rate = num_channels * sample_rate * bits_per_sample // 8
    block_align = num_channels * bits_per_sample // 8
    subchunk2_size = number_of_frames * num_channels * bits_per_sample // 8
    chunk_size = 36 + subchunk2_size

    if not filename.endswith('.wav'):
        filename += '.wav'

    with open(filename, 'wb') as wav_file:
        # Write WAV header
        wav_file.write(b'RIFF')
        wav_file.write(struct.pack('<I', chunk_size))
        wav_file.write(b'WAVE')
        wav_file.write(b'fmt ')
        wav_file.write(struct.pack('<I', 16,))
        wav_file.write(struct.pack('<H', 1,))
        wav_file.write(struct.pack('<H', num_channels,))
        wav_file.write(struct.pack('<I', sample_rate,))
        wav_file.write(struct.pack('<I', byte_rate,))
        wav_file.write(struct.pack('<H', block_align,))
        wav_file.write(struct.pack('<H', bits_per_sample))
        wav_file.write(b'data')
        wav_file.write(struct.pack('<I', subchunk2_size))

        # Write PCM data
        max_amplitude = 32767.0
        for sample in audio:
            pcm_sample = int(sample * max_amplitude)
            pcm_sample = max(-32768, min(32767, pcm_sample))  # Clamp to valid range
            wav_file.write(struct.pack('<h', pcm_sample))


def read_wav_file(filename):
    with open(filename, 'rb') as f:                
        (chunk_id,)        = struct.unpack('<4s', f.read(4))
        (chunk_size,)      = struct.unpack('<I' , f.read(4))
        (format,)          = struct.unpack('<4s', f.read(4))
        (subchunk1_id,)    = struct.unpack('<4s', f.read(4))
        (subchunk1_size,)  = struct.unpack('<I' , f.read(4))
        (audio_format,)    = struct.unpack('<H' , f.read(2))
        (num_channels,)    = struct.unpack('<H' , f.read(2))
        (sample_rate,)     = struct.unpack('<I' , f.read(4))
        (byte_rate,)       = struct.unpack('<I' , f.read(4))
        (block_align,)     = struct.unpack('<H' , f.read(2))
        (bits_per_sample,) = struct.unpack('<H' , f.read(2))
        (subchunk2_id,)    = struct.unpack('<4s', f.read(4))
        (subchunk2_size,)  = struct.unpack('<I' , f.read(4))
            
        number_of_frames = subchunk2_size // (bits_per_sample // 8)

        audio = []
        max_amplitude = 32767.0
        for _ in range(number_of_frames):
            pcm_sample_bytes = f.read(2)
            if not pcm_sample_bytes:
                break
            (pcm_sample,) = struct.unpack('<h', pcm_sample_bytes)
            audio.append(pcm_sample / max_amplitude)

    return audio