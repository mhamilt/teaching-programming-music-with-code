// wav_library example
//
// Build and run in terminal with:
//
// g++ -std=c++11 main.cpp -o main && ./main

#include <iostream>
#include <cmath>
#include "wav_library.h"

int main(int argc, const char * argv[])
{
    
    const int numSamples = 44100;
    float sampleRate = 44100.0f;
    float* sineWave = new float[numSamples];
    float frequency = 440.0f;
    
    float radsPerSamp = 2.0f * 3.1415926536f * frequency / sampleRate;
    
    for (unsigned long i = 0; i < numSamples; i++)
    {
        sineWave[i] = std::sin (radsPerSamp * (float) i) * 0.707f;
    }
    
    writeToWav(sineWave, numSamples, "a440.wav");
    
    return 0;
}