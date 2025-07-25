import java.io.*;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.ArrayList;
import java.util.List;

public class WavFile {

    public static void write(float[] floatData, String filename, int nchannels, int bitDepth, int sampleRate) throws IOException {
        // Normalize float data
        float max = 0;
        for (float v : floatData) {
            if (Math.abs(v) > max) max = Math.abs(v);
        }
        float normalization = 1.0f / max;

        for (int i = 0; i < floatData.length; i++) {
            floatData[i] *= normalization;
        }

        if (!filename.endsWith(".wav")) {
            filename += ".wav";
        }

        int bytesPerSample = bitDepth / 8;
        int byteRate = sampleRate * nchannels * bytesPerSample;
        int dataLength = floatData.length * bytesPerSample;

        try (FileOutputStream out = new FileOutputStream(filename)) {
            // Write RIFF header
            out.write("RIFF".getBytes());
            writeLittleEndian(out, 36 + dataLength, 4);  // Chunk size
            out.write("WAVE".getBytes());

            // fmt subchunk
            out.write("fmt ".getBytes());
            writeLittleEndian(out, 16, 4); // Subchunk1Size (16 for PCM)
            writeLittleEndian(out, 1, 2);  // AudioFormat (1 = PCM)
            writeLittleEndian(out, nchannels, 2);
            writeLittleEndian(out, sampleRate, 4);
            writeLittleEndian(out, byteRate, 4);
            writeLittleEndian(out, nchannels * bytesPerSample, 2); // BlockAlign
            writeLittleEndian(out, bitDepth, 2); // BitsPerSample

            // data subchunk
            out.write("data".getBytes());
            writeLittleEndian(out, dataLength, 4);

            int maxAmplitude = (1 << (bitDepth - 1)) - 1;
            for (float sample : floatData) {
                int intSample = (int)(sample * maxAmplitude);
                writeLittleEndian(out, intSample, bytesPerSample);
            }
        }
    }

    public static void write(float[] floatData, String filename) throws IOException {
        write(floatData, filename, 1, 16, 44100);
    }


    public static float[] read(String filename) throws IOException {
        if (!filename.endsWith(".wav")) {
            filename += ".wav";
        }

        try (FileInputStream in = new FileInputStream(filename)) {
            byte[] header = new byte[44];
            if (in.read(header) != 44) {
                throw new IOException("Invalid WAV file header.");
            }

            int bitDepth = ByteBuffer.wrap(header, 34, 2).order(ByteOrder.LITTLE_ENDIAN).getShort();
            int bytesPerSample = bitDepth / 8;

            int dataSize = ByteBuffer.wrap(header, 40, 4).order(ByteOrder.LITTLE_ENDIAN).getInt();
            byte[] data = new byte[dataSize];
            if (in.read(data) != dataSize) {
                throw new IOException("Could not read WAV data.");
            }

            int sampleCount = dataSize / bytesPerSample;
            float[] floatData = new float[sampleCount];
            int maxAmplitude = (1 << (bitDepth - 1)) - 1;

            for (int i = 0; i < sampleCount; i++) {
                int sample = ByteBuffer.wrap(data, i * bytesPerSample, bytesPerSample)
                                       .order(ByteOrder.LITTLE_ENDIAN).getShort();
                floatData[i] = (float) sample / maxAmplitude;
            }

            return floatData;
        }
    }

    // Helper method to write little-endian values
    private static void writeLittleEndian(OutputStream out, int value, int bytes) throws IOException {
        for (int i = 0; i < bytes; i++) {
            out.write(value & 0xFF);
            value >>= 8;
        }
    }
}
