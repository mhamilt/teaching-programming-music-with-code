//
//  main.c
//  wav_library
//
//  Created by admin on 25/07/25.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "wav_library.h"


int main(int argc, const char * argv[]) 
{    
    int numSamples = 44100;
    float sampleRate = 44100.0f;
    float* sineWave = (float*)malloc(numSamples * sizeof(float));
    float frequency = 440.0f;
    
    float radsPerSamp = 2.0f * 3.1415926536f * frequency / sampleRate;
    
    for (unsigned long i = 0; i < numSamples; i++)
    {
        sineWave[i] = sinf(radsPerSamp * (float) i) * 0.707f;
    }
    
    writeWavFile(sineWave, numSamples, "a440.wav");
    
    uint32_t numberOfFrames;
    float* readAudio = readWavFile(&numberOfFrames, "a440.wav");
    
    writeWavFile(readAudio, numberOfFrames, "a440_read_test.wav");
    
    return 0;
}


