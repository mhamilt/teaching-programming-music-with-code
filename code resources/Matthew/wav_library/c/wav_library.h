//
//  wav_library.h
//  C-Playground
//
//  Created by admin on 25/07/25.
//

#ifndef wav_library_h
#define wav_library_h

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

struct WaveHeader
{
    /** waveFormatHeader: The first 4 bytes of a wav file should be the characters "RIFF" */
    char chunkID[4];
    /** waveFormatHeader: This is the size of the entire file in bytes minus 8 bytes */
    uint32_t chunkSize;
    /** waveFormatHeader" The should be characters "WAVE" */
    char format[4];
    /** waveFormatHeader" This should be the letters "fmt ", note the space character */
    char subChunk1ID[4];
    /**waveFormatHeader: For PCM == 16, since audioFormat == uint16_t */
    uint32_t subChunk1Size;
    /**waveFormatHeader: For PCM this is 1, other values indicate compression */
    uint16_t audioFormat;
    /**waveFormatHeader: Mono = 1, Stereo = 2, etc. */
    uint16_t numChannels;
    /**waveFormatHeader: Sample Rate of file */
    uint32_t sampleRate;
    /**waveFormatHeader: SampleRate * NumChannels * BitsPerSample/8 */
    uint32_t byteRate;
    /**waveFormatHeader: The number of bytes for one sample including all channels */
    uint16_t blockAlign;
    /**waveFormatHeader: 8 bits = 8, 16 bits = 16 */
    uint16_t bitsPerSample;
    /**waveFormatHeader: Contains the letters "data" */
    char     subChunk2ID[4];
    /**waveFormatHeader: == NumSamples * NumChannels * BitsPerSample/8
     This is the number of bytes in the data.
     */
    uint32_t subChunk2Size;
};


void writeWavFile(float* audio, uint32_t numberOfFrames, const char* filename)
{
    struct WaveHeader wavHeader;
    
    uint16_t numChannels = 1;
    uint16_t bitsPerSample = 16;
    uint32_t sampleRate = 44100;
    
    FILE* wavFile = fopen(filename, "w");
    
    if (!wavFile)
    {
        printf("Could not open file to write: check file path\n");
        return;
    }
    
    memcpy(wavHeader.chunkID, &"RIFF", 4);
    memcpy(wavHeader.format, &"WAVE", 4);
    memcpy(wavHeader.subChunk1ID, &"fmt ", 4); //notice the space at the end!
    wavHeader.subChunk1Size = 16;
    wavHeader.audioFormat = 1;
    wavHeader.numChannels = numChannels;
    wavHeader.sampleRate = sampleRate;
    wavHeader.byteRate   = (uint32_t)numChannels * sampleRate * (uint32_t)bitsPerSample / 8;
    wavHeader.blockAlign = numChannels * bitsPerSample / 8;
    wavHeader.bitsPerSample = bitsPerSample;
    memcpy(wavHeader.subChunk2ID, &"data", 4);
    wavHeader.subChunk2Size = numberOfFrames * (uint32_t)numChannels * (uint32_t)bitsPerSample / 8;
    wavHeader.chunkSize = 36 + wavHeader.subChunk2Size;
    
    fwrite(&wavHeader, sizeof(wavHeader), 1, wavFile);
    
    const float max16BitValue = 32767.0f;
    
    for(int i = 0;i < numberOfFrames; ++i)
    {
        int16_t pcm_sample = (int16_t)(audio[i] * max16BitValue);  //set sdata to PCM 16-bit
        fwrite(&pcm_sample, sizeof(int16_t), 1, wavFile);
    }
    
    fclose(wavFile);
}

float* readWavFile(uint32_t* numberOfFrames, const char* filename)
{
    struct WaveHeader wavHeader;
    
    FILE *f = fopen(filename, "rb");
    if (!f)
    {
        return NULL;
    }
    
    fread(&wavHeader, 1, sizeof(wavHeader), f);
    
    *numberOfFrames = wavHeader.subChunk2Size * 8 /(wavHeader.bitsPerSample);
    
    uint32_t dataSize = wavHeader.subChunk2Size;
    void* data = malloc(dataSize);
    
    for (int sample = 0; sample < dataSize; ++sample)
    {
        fread(&data[sample], 1, 1, f);
    }
    
    fclose(f);
    
    uint16_t* pcm = (uint16_t*)data;
    float* audio = malloc(dataSize * sizeof(float));
    
    const float max16BitValue = 32767.0f;
    
    for (int i = 0; i < *numberOfFrames; ++i)
    {
        audio[i] = pcm[i] / max16BitValue;
    }
    
    return audio;
}

#endif /* wav_library_h */
