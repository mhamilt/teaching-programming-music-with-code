use std::fs::File;
use std::io::{self, Read, Write, BufReader, BufWriter};
use std::path::Path;

pub fn write_wav_file(
    float_data: &[f32],
    filename: &str,
    nchannels: u16,
    bit_depth: u16,
    sample_rate: u32,
) -> io::Result<()> {
    let path = if filename.ends_with(".wav") {
        filename.to_string()
    } else {
        format!("{}.wav", filename)
    };

    let max_sample = float_data.iter().cloned().map(f32::abs).fold(0.0, f32::max);
    let normalization = if max_sample != 0.0 { 1.0 / max_sample } else { 1.0 };
    let scaled_data: Vec<i16> = float_data
        .iter()
        .map(|s| (s * normalization * i16::MAX as f32) as i16)
        .collect();

    let byte_rate = sample_rate * nchannels as u32 * (bit_depth as u32 / 8);
    let block_align = nchannels * (bit_depth / 8);
    let subchunk2_size = scaled_data.len() as u32 * (bit_depth as u32 / 8);
    let chunk_size = 36 + subchunk2_size;

    let mut writer = BufWriter::new(File::create(Path::new(&path))?);

    // Write RIFF header
    writer.write_all(b"RIFF")?;
    writer.write_all(&(chunk_size).to_le_bytes())?;
    writer.write_all(b"WAVE")?;

    // fmt subchunk
    writer.write_all(b"fmt ")?;
    writer.write_all(&16u32.to_le_bytes())?; // Subchunk1Size for PCM
    writer.write_all(&1u16.to_le_bytes())?;  // AudioFormat PCM = 1
    writer.write_all(&nchannels.to_le_bytes())?;
    writer.write_all(&sample_rate.to_le_bytes())?;
    writer.write_all(&byte_rate.to_le_bytes())?;
    writer.write_all(&block_align.to_le_bytes())?;
    writer.write_all(&bit_depth.to_le_bytes())?;

    // data subchunk
    writer.write_all(b"data")?;
    writer.write_all(&subchunk2_size.to_le_bytes())?;

    for sample in scaled_data {
        writer.write_all(&sample.to_le_bytes())?;
    }

    Ok(())
}

pub fn read_wav_file(filename: &str) -> io::Result<Vec<f32>> {
    let path = if filename.ends_with(".wav") {
        filename.to_string()
    } else {
        format!("{}.wav", filename)
    };

    let mut reader = BufReader::new(File::open(Path::new(&path))?);
    let mut header = [0u8; 44];
    reader.read_exact(&mut header)?;

    if &header[0..4] != b"RIFF" || &header[8..12] != b"WAVE" {
        return Err(io::Error::new(io::ErrorKind::InvalidData, "Invalid WAV header"));
    }

    // let nchannels = u16::from_le_bytes([header[22], header[23]]);
    // let sample_rate = u32::from_le_bytes([header[24], header[25], header[26], header[27]]);
    let bits_per_sample = u16::from_le_bytes([header[34], header[35]]);
    let data_chunk_size = u32::from_le_bytes([header[40], header[41], header[42], header[43]]);
    let num_samples = data_chunk_size as usize / (bits_per_sample as usize / 8);

    if bits_per_sample != 16 {
        return Err(io::Error::new(io::ErrorKind::InvalidData, "Only 16-bit WAV supported"));
    }

    let mut pcm_data = vec![0u8; num_samples * 2];
    reader.read_exact(&mut pcm_data)?;

    let mut float_data = Vec::with_capacity(num_samples);
    for chunk in pcm_data.chunks(2) {
        let sample = i16::from_le_bytes([chunk[0], chunk[1]]);
        float_data.push(sample as f32 / i16::MAX as f32);
    }

    Ok(float_data)
}

