# An Educator's Guide to WAVE Format Files

- [An Educator's Guide to WAVE Format Files](#an-educators-guide-to-wave-format-files)
  - [Summary](#summary)
  - [Prerequisite Knowledge](#prerequisite-knowledge)
  - [Programming Concepts and Methods](#programming-concepts-and-methods)
    - [Writing a WAVE File](#writing-a-wave-file)
    - [Suggestions for Customizing and Expanding](#suggestions-for-customizing-and-expanding)
      - [Library Functionality](#library-functionality)
      - [Audio Editing](#audio-editing)
  - [Teaching Note](#teaching-note)


## Summary

This resource introduces basic programming concepts using music as a vehicle. Students will learn by creating and manipulating audio data, which provides an engaging and tangible way to explore programming.

## Prerequisite Knowledge
No prior knowledge is required. If you are teaching this resource to students, it is recommended to familiarize yourself by following along. While the examples are in Python, the concepts are language-agnostic.  

For some languages, these resources may overcomplicate simple audio playback. Examples include [MATLAB](https://www.mathworks.com/help/matlab/ref/soundsc.html), [Octave](https://octave.sourceforge.io/octave/function/soundsc.html), or [Jupyter/IPython](https://ipython.org/ipython-doc/3/api/generated/IPython.display.html), which already provide array playback functions.

For other languages, these examples may under-simplify the problem. To address this, minimal WAVE file writing examples are provided in C++, Rust, and Python. These can serve as blueprints for implementing similar functionality in other languages.  

External libraries or packages should initially be avoided, as they may introduce operating system-specific behavior, package manager issues, or other problems unrelated to learning programming fundamentals.  

For example, teaching Python audio and [list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) is not improved by issues with outdated `pip` versions or `PATH` configurations when installing [PyAudio](https://pypi.org/project/PyAudio/), which could disproportionately affect students without prior setup experience.

---

## Programming Concepts and Methods

### Writing a WAVE File
The WAVE format is one of the simplest media file types to create and is widely supported, making it ideal for cross-platform programming courses. Most modern operating systems provide native playback for WAVE files.  

From a student perspective, WAVE files are complex enough to be interesting but simple enough to be digestible. Programming a WAVE file write has been a [common introductory assignment](https://www.cs.utahtech.edu/cs/3005/assignments.wav_wizard/assignment_07_wav_file_part1/) in computer science courses for decades, including [CS101](https://www.danielzingaro.com/sound_proc2/assignment.html) and [Stanford CCRMA](https://ccrma.stanford.edu/courses/422-winter-2014/projects/WaveFormat/).

Creating WAVE files allows students to:
- Sonify data
- Learn computer science memory concepts, such as endianness, data types, file streams, headers, and memory management  

The provided `wav_library/` files are simplified to allow educators to gradually introduce more advanced interventions. Initially, educators may abstract library use to a single line to avoid overwhelming students.

---

### Suggestions for Customizing and Expanding

#### Library Functionality
- **Bit Depth:** Add functionality to configure file bit depth. This can also serve as a "bit-crushing" exercise.  
- **Sample Rate:** Add functionality to configure the sample rate. This could also introduce time-stretching or pitch-shifting concepts.  
- **Multi-Channel:** PCM in WAVE files is interleaved. Increasing to stereo or multichannel is achievable by combining multiple arrays (e.g., using `zip`). This can also be an opportunity for parsing more complex audio formats.  
- **Metadata:** The simplest WAVE standard is used here, but metadata can be added for cue points, playlists, or other features. This can serve as an exercise in data structures or object-oriented programming. Students exploring systems like FMOD or Wwise can use metadata for cueing and looping audio.

#### Audio Editing
- **Editing Algorithms:** Implement audio processing routines such as silence removal, gating, or limiting. These can form the basis of algorithmic composition exercises.  
- **DSP Algorithms:** Any signal processing algorithm can be prototyped in this workflow by reading audio, processing it, and writing 'wet' and 'dry' versions.

For courses using Git, students could implement these expansions in feature branches to practice version control.  

Finally, collaborating on building a simple library gives students a reusable resource, providing a canvas to explore creating custom audio tools.

---

## Teaching Note
By starting with Python examples and gradually expanding functionality, students can learn programming fundamentals while engaging in creative, tangible tasks. The approach encourages experimentation, iterative learning, and understanding of both programming and digital audio principles.