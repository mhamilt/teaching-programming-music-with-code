mod wav_library;
use std::f32::consts::PI;
use std::io;


fn generate_sine_wave(freq: f32, duration_secs: f32, sample_rate: u32) -> Vec<f32> {
    let samples = (sample_rate as f32 * duration_secs) as usize;
    (0..samples)
        .map(|i| {
            let t = i as f32 / sample_rate as f32;
            (2.0 * PI * freq * t).sin()
        })
        .collect()
}

fn main() -> io::Result<()> {
    let sample_rate = 44100;
    let data = generate_sine_wave(440.0, 1.0, sample_rate);
    wav_library::write_wav_file(&data, "a440", 1, 16, sample_rate)?;

    let loaded = wav_library::read_wav_file("a440.wav")?;
    println!("Loaded {} samples.", loaded.len());
    Ok(())
}