# Programming Fundamentals with Music

## Summary
Getting materials together and dealing with the first few basic of concepts of programmming through music.

## Prerequisite Knowledge
No pre-requisite knowledge is required. If you intend on teaching this resource to other students it is recommended to familiarise yourself well by following along. The resources here are presented in Python, but the intention is that they are language agnostic. For some langauges, these resources may be a huge over complication, in which case take them at their spirit and not at their word.

For other languages, it these resources may be an over simplification. As such, some examples of wav file writing have been provided in (currently) C++, Rust as well as Python and can hopefully be used as a blueprint for implementations in other language. 

## Programming concepts and methods

### Writing WAVE file

The WAVE is one of the simplest media files you can create and is so widely supported, it makes the perfect output for cross-platform compatible programming courses.  Most modern operating systems will provide some means of playback for a WAVE file.

From a student perspective WAVE file is also complex enough to be interesting, but simple enough to be digestable. This is one of the reasons that programming a WAVE file write has been the [goto assignment for 101 computer science courses](https://ccrma.stanford.edu/courses/422-winter-2014/projects/WaveFormat/) for decades.

Not only does the WAVE file allow for easy data sonification, but it helps to teach general computer science memory concepts like endianess, data type, file streams, file headers and standards, and memory management.

The WAVE file library resources here are provided as example as to how much code will be necessary to sonifying data. For educators, it is suggested that you begin by abstracting away the library to a single line inclusion so as not to overload students with information. Over time it is recommended to introduce problems that require direct intervention in the library itself. The file format cases considered in the `wav_library/` files are the simplest, partly to fascilitate this need for intervention.

Some customisations to collaborate with students might be:

- Bit depth
- Sample Rate
- Multi-channel (interlaced) audio
- Audio Editing
- DSP algorithms

If you are teaching a course on git version control, you might try having groups implement all of the above to feature branches.

Finally, by collaborating on building a simple library you provide a great resource to pass on to students at the end of a course, which provides a canvas for them to explore making their own tools.

## How this resource could be used


## How could this be taken further


## Technical Resources or Requirements
