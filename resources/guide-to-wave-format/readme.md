# Programming Fundamentals with Music

<!-- - [x] How this resource could be used -->
<!-- - [x] How could this be taken further -->
<!-- - [x] Technical Resources or Requirements -->

## Summary
Getting materials together and dealing with the first few basic of concepts of programmming through music.

## Prerequisite Knowledge
No pre-requisite knowledge is required. If you intend on teaching this resource to other students it is recommended to familiarise yourself well by following along. The resources here are presented in Python, but the intention is that they are language agnostic. For some langauges, these resources may be a huge over complication of what is needed to easily play back audio, in which case take them at their spirit and not at their word. An example of this may be [MATLAB](https://www.mathworks.com/help/matlab/ref/soundsc.html), [Octave](https://octave.sourceforge.io/octave/function/soundsc.html) or [Jupyter/IPython](https://ipython.org/ipython-doc/3/api/generated/IPython.display.html) which already provide means for play back of arrays as audio.

For other languages, it these resources may be an over simplification of the problem. As such, some examples of wav file writing have been provided in (currently) C++, Rust as well as Python and can hopefully be used as a blueprint for implementations in other language. External libraires / packages which solve this problem should be avoided initially as they bring with them all manner of difficulties in the from of operating system specific behaviour, package manager configuration, and problems that are outside of the immdiate task of learning a programming language. These sort of problems need to be addressed, but should be done so delibarately with the explicit understanding by students of the problem at hand.

A python lesson on audio and [list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) is not going to be improved by issues arising from outdate versions of `pip` or problems with `PATH` configurations when trying to install [pyaudio](https://pypi.org/project/PyAudio/). This is especially true when these problems do not affect all students, but only those without the prior knowledge to fix the problem proactively which can lead to them feeling ostracised. 

## Programming concepts and methods

### Writing WAVE file

The WAVE is one of the simplest media files you can create and is so widely supported, it makes the perfect output for cross-platform compatible programming courses.  Most modern operating systems will provide some means of playback for a WAVE file.

From a student perspective WAVE file is also complex enough to be interesting, but simple enough to be digestable. This is one of the reasons that programming a WAVE file write has been the [goto assignment](https://www.cs.utahtech.edu/cs/3005/assignments.wav_wizard/assignment_07_wav_file_part1/) for [101 computer](https://www.danielzingaro.com/sound_proc2/assignment.html) science [courses](https://ccrma.stanford.edu/courses/422-winter-2014/projects/WaveFormat/) [for decades](https://cs50.harvard.edu/x/2023/labs/4/volume/).

Not only does the WAVE file allow for easy data sonification, but it helps to teach general computer science memory concepts like endianess, data type, file streams, file headers and standards, and memory management.

The WAVE file library resources here are provided as example as to how much code will be necessary to sonifying data. For educators, it is suggested that you begin by abstracting away the library to a single line inclusion so as not to overload students with information. Over time it is recommended to introduce problems that require direct intervention in the library itself. The file format cases considered in the `wav_library/` files are the simplest, partly to fascilitate this need for intervention.

Suggestions for customising and expanding this lesson is split into 2 categories, library functaionality and audio editing.

##### Library Functionality

- Bit depth: add functionality to configure the bit-depth of a file. This could also be implemented as part of a "bit-crushing" algorithm.
- Sample Rate: add functionality to configure sample rate. As above, this could be to change bit depth, but can also be used a part of a basic time-stretching / pitch-shifting algorithm.
- Multi-channel: the PCM in WAVE files is interlaced meaning the samples for each channel are grouped together (e.g. Channel 1, Sample 1; Channel 2, Sample 2; Channel 1, Sample 2; Channel 2, Sample 2). Increasing to stereo is achievable simply by taking two arrays and ``zipping'' them together. This can also present a fun challeneg for custom parsing of eigenmike files.
- Metadata: The WAVE standard covered here is its most simplistic, but there is also the ability to add metadata relating to cue points and playlist values. This can be a good vehicle for talking about data structures or even object orientated programming. Cue points are typically used with digital audio workstations. If student groups are also exploring other systems like FMOD and WWise, the metadata can also be used for cue-ing and looping audio.

##### Audio editing 

- Audio Editing: Algorithms around audio editing can be designed, either silence removal or gating / limiting. It can also basis for algorithmic composition practices. 
- DSP algorithms: Any signal processing algorithm can be protyped as part of this work flow, simply by reading audio, processing, and writing out 'wet' and 'dry' versions.

If you are teaching a course on git version control, you might try having groups implement all of the above to feature branches.

Finally, by collaborating on building a simple library you provide a great resource to pass on to students at the end of a course, which provides a canvas for you and your students to explore making your own tools.