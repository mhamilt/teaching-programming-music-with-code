// wav_library example
//
// Build and run in terminal with:
//
// javac WavFile.java Main.java && java Main

import java.io.*;

public class Main {    
    public static void main(String[] args)
    {
        int numSamples = 44100;
        float sampleRate = 44100.0f;
        float[] sineWave = new float[numSamples];
        float frequency = 440.0f;

        float radsPerSamp = 2.0f * 3.1415926536f * frequency / sampleRate;

        for (int i = 0; i < numSamples; i++)
        {            
            sineWave[i] = (float)(Math.sin (radsPerSamp * (float)i)) * 0.707f;
        }
    
        WavFile wavFile = new WavFile();
        try {
            wavFile.write(sineWave, "a440");
        }
        catch(IOException e) {
            e .printStackTrace();
        }
        
    }
}