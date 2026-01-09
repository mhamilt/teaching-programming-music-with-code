---
title: "Practical approaches to using sound and music in programming pedagogy"
bibliography: references.bib
---

## Introduction

This chapter is designed to serve as a brief tour of connections between
sound, music, programming and pedagogy. In particular, it is aimed at
educators who want to explore sound and music in their programming
pedagogy. The chapter presents motivations for connecting these domains,
introduces prior work in this area, and presents a range of
[accompanying resources]() that can be taken up or adapted to bring
sound and music into coding education.

Making code that makes sound and music can be fun, even with only a very
basic understanding of programming concepts, and regardless of any prior
music education. There are many ways in which sound and music may
connect with programming. For example:

-   composing with code: using code to write pieces of music,

-   performing with code: writing code in a performance to make music,

-   creating instruments: building software tools for personal music
    making or for others to use,

-   understanding sound: coding to analyse and explore representations
    of sound and/or music,

-   data sonification: representing existing data as sound or music,
    either in real-time or with historical data,

-   coding responsive sound and music to games or other interactive
    programs.

Section [2](#sec:why){reference-type="ref" reference="sec:why"} explores
motivations for connecting music with programming. A brief overview of
the rich existing work in this domain is presented in Section
[3](#sec:literature){reference-type="ref" reference="sec:literature"}.
The set of practical accompanying resources that can serve as starting
points into different kinds of music/coding projects are then introduced
in Section [4](#sec:resources){reference-type="ref"
reference="sec:resources"}.

## Why combine programming with sound and music? {#sec:why}

Music and programming have a rich intertwined history. Simple but
effective connections can be found between programming concepts --- such
as iteration, abstraction, conditionals, loops --- and musical concepts
such as rhythm, timing, harmony, pattern and so on. Writing a program
that generates sound provides an immediate, engaging way to manifest
abstract processes. In a pedagogical sense, the sound output is a form
of feedback. Programs don't have to be complicated or sophisticated in
terms of the coding to be musically satisfying. Students can create
sound and music that they can share with friends and relatives, who may
not know the first thing about programming but can nonetheless engage
with the creative outcomes.

Programming concepts can be playfully explored in musical contexts. For
example, an integer array can be rendered as a piano melody, a drum
rhythm, or directly as a sound file (see Figure
[1](#fig:arrays-as-music){reference-type="ref"
reference="fig:arrays-as-music"}). This gives an immediate meaning to
the output data, motivating students to care about the specific values
in the array, the length of the array, the range of data in the array,
different ways of reading and writing values to and from the array and
so on. Operations on that array take on musical meanings: ordering an
array provides a scale; reversing an array reverses musical material.
Meaningful data that students care about can motivate students to find
things out for themselves, and provides a scope for the kind of creative
explorations that are often lacking on introductory programming courses
[@sharmin_creativity_2021].

Sound and music can also be used to present and experience data in
different ways. Data sonification has a long history [@worrall_2019],
from giving a constant awareness of something otherwise invisible with
geiger counters or medical monitoring devices, to hearing emergent
behaviours in dynamical systems, providing auditory graphs for the
visually impaired [@walker_mauney_2010], or creative projects that use
the data for musical ends [@bulley_jones_2011; @barrett_mair_2014].

![Two examples of arrays becoming sound and music. On the left, the
array is translated into note values. On the right, the array is
translated directly to an audio
file.](images/fig1_arrays_as_sound_and_music.pdf){#fig:arrays-as-music
width="100%"}

There are obvious parallels here with coding and visual art.
Environments such as Processing [@reas2006processing] connect
programming with image and animation to motivate learning and
exploration (CITE). As explored in the following section, there is a
similarly rich history of music making in programming pedagogy. To mix
music, art, computers and coding therefore continues a long and fruitful
tradition [@reichardt1971; @Dreher2014; @wang17], and can serve as a
reminder to both students and educators that coding is fundamentally
about making things and is a creative act.

## Overview of what exists already {#sec:literature}

Music and programming have been connected in a wide variety of ways,
sometimes through the addition of libraries for integrating musical
inputs and outputs with existing languages, and sometimes through the
development of specifically designed languages or environments. As this
is a very short chapter, it only scratches the surface of many of the
interesting work done in this domain, and the focus is on music/code
projects with explicitpedagogical elements aims.

Most mainstream programming languages are able to work with sound and
music as outputs. This could be achieved by writing data to a file, e.g.
an audio file \[INSERT NOD TO RESOURCES\] or a MIDI file (a common
musical data format that can be used to synthesise sound). The program
could also transmit real-time messages to an audio engine that runs
separately, e.g. a standalone synthesiser or sampler [^1], a digital
audio workstation, or frameworks such as
[SuperDirt](https://github.com/musikinformatik/SuperDirt). Most
mainstream programming languages will have libraries available for these
purposes, making it relatively easy to adapt any simple programming
exercise into a sonic/musical exercise.

The Scratch programming language[^2] is a well established starting
point for young people to engage with coding. While sound and music are
not usually the primary focus for students, there is still considerable
scope for creativity and experimentation. Brown and Ruthman present a
useful range of project types in their *Scratch Music Projects* book
[@brown20], from simple theremin-like interactive instruments, through
playing simple riffs, up to thinking about loops, musical structures,
generative music, and live coding performance. As Scratch is used more
generally for creating games, stories or animations, students can be
motivated to explore sound and music as one component in wider creative
projects.

Sonic Pi[^3] is a popular example of a language specifically designed
for music. It is a simple but flexible environment that aims to support
school-age students to learn to code by making music
[@aaron_sonic_2016]. As with Scratch, the focus on play and having fun
with Sonic Pi can foster a more positive attitude towards programming
[@petri_sonicpi_2022], and can provide a starting point for moving from
simple programming concepts to more involved topics such as concurrency
[@traversaro_hearplay_2024]. Sound-making programs can start off very
simple with basic commands such as \"play 60\", but can be built into
entire pieces or performances [^4].

Sonic Pi is rooted in practices of live coding for music, a substantial
community that serves as an access point to programming for many
musicians, as well as an access point for music for some programmers.
The movement has engaged closely with programming pedagogy from
different perspectives; Blackwell et al [@blackwell_livecoding_2022]
provide a useful overview. The proceedings of the International
Conference on Live Coding[^5] also present a broader repository of
topics, many of which cover music in programming education (GIVE
EXAMPLES). Live musical coding is also notable as a community that has
attempted to push back against coding as a male-dominated space
[@blackwell_livecoding_2022], with all-women and non-binary workshops
being a regular occurrence. Armitage [@armitage_spaces_2018] points to
the domain as being a "a space in which to fail constructively".

The EarSketch[^6] [@engelman_earsketch_2017] and TunePad[^7] projects
are similar to Sonic Pi in their pedagogical aims, in that they seek to
broaden participation in computing by demystifying coding and relating
it to a domain of interest to students. The projects embed coding
elements alongside more conventional music-making tools such as tracks,
instruments, timeline, mixer, etc. This provides a familiar workspace
for those with musical backgrounds and means that the code doesn't need
to cover all aspects of the music making, but can be written in snippets
with very particular goals, such as making a drum loop, or a bass riff.
Both projects run in the browser and use Python (although EarSketch has
a JavaScript option). They are designed specifically with sharing in
mind: both code sharing and collaborative editing, further motivating
students to engage with the coding [@freeman_earsketch_2019]. Petrie
[@petrie_ct_2024] studied the potential for both projects to support
computational thinking in 11-12 year old students who had no prior
school experience of either programming or music making. Petrie notes
that students benefit from the fact that the kinds of musical tasks
supported by these projects are naturally incremental and iterative.

A key concern across all the above projects is that there should be room
for musical variety and expression; although they may present simple
entry points to engaging with programming, it is possible to create rich
and interesting creative work that students will be proud of.

## Overview of our online resources \[rename this\] {#sec:resources}

Perhaps a quick note towards the many many things that are important,
but perhaps out of scope here.

Five example resources accompany this chapter that reflect some of the
different approaches to combining aspects of sound, music and
programming in the different authors' pedagogical work. Each example
resource comes with a readme that gives a sense of how the resource
might be used, who might find it valuable, what prior knowledge the
students may need, and what technologies will be needed.

### Python piano piece

This resource is aimed at students who have started on Python quite
recently. It attempts to make musical output as simple and accessible as
possible. Students are shown how to generate piano pieces as MIDI data
which can be played back directly within a Python notebook. Students can
develop their understanding of fundamental concepts programming concepts
such as lists, loops and conditionals. The ability to directly hear the
results is intended to motivate students to think about how they can
develop the code by themselves to try to explore how they can start to
tailor the musical output towards something they find sonically
interesting or satisfying.

### Strudel drum patterns

This resource is both similar and different to the piano example.
Students engage with *Strudel*[^8], a browser-based JavaScript port of
the popular *TidalCycles*[^9] live coding language. The language has
been particularly popular for exploring algorithmic approaches to beat
making[^10]. The editor provides useful visual feedback to show how the
code relates to the unfolding beats. It has been a popular way to engage
with code for the first time for many
[\[CITATION\]](#CITATION){reference-type="ref" reference="CITATION"}, as
well as being an useful introduction to Haskell and functional
programming for others [@CITATION]. Unlike the Python example above, it
may not be so straightforward to map programming insights directly to
other domains such as data science or INSERT ANOTHER DOMAIN HERE.

### \[Charlotte\]

### \[Matthew\]

This section focusses on educators directly and the ground work needed
to make the most portable and technologically accessible lessons. No
prior knowledge is assumed and as the resource is intended to guide the
reader through the process of WAVE file creation. The ultimate goal
being a simple library ripe for customisation and intimately understood
for easy dissemination to students.

All data can be a sound and the WAVE file is the simplest means of data
sonification and music creation. Most modern operating systems (and many
older ones) will support WAVE file playback through a media player,
browser or command line tool. The resource emphasises the use of
standard libraries to improve portability and providing a means of
quickly beginning music-based programming lessons without burdening
students with language-specific ancillary concepts that can potentially
be a demotivating obstacle to new programmers.

The intention is not to be prescriptive, but rather show how malleable
the WAVE format can be for teaching music and programming.

The central lesson is explained in an IPython (Jupyter) notebook, but
there is also companion code in C, C++, Java and Rust to reinforce the
basic elements need to solve the problem.

### \[Mike\]

### \[Yash\]

This demo serves as a template or a starting point to create web-based
responsive musical instruments and/or controllers. The template combines
RNBO (by Cycling '74) (link?), using JavaScript and smartphone sensors,
to build a responsive synthesiser hosted on the web that, when accessed
from a smartphone, utilises the motion sensors to control specific
parameters of the synthesiser. It features a simple RNBO Additive synth
patch with some simple effects like distortion and EQ. The audio engine
is exported from RNBO and embedded into a lightweight HTML/JavaScript
site inspired by Cycling '74's example code, with unnecessary UI
stripped away for clarity. A p5.js-based sequencer for playing notes and
visual feedback. Motion data from a smartphone's orientation sensors is
mapped in real time to RNBO parameters, enabling gestural control over
sound, allowing gestures like tilting or twisting a phone to shape the
sound. Designed as both a learning resource and a creative springboard,
the project can be adapted for musical instruments, live installations,
audience-participation performances, or experimental audio-visual tools.

## Mini summary

This chapter has touched briefly on some of the many connections between
sound, music and programming that exist, and how these can be and have
been productively brought to bear on programming pedagogy.

We close with Rebecca Fiebrink's advice to musical coders [@brown20 p
145], that captures some of the excitement of bringing these two domains
together:

> Have you figured out how to recreate your favorite pop song with code?
> Great! Now try composing a new song that's all your own. Or see if you
> can create new types of music that are easier to make with code than
> without it --- or even types of music that are impossible to create
> without a computer! What do you come up with? Can you make new sounds
> that nobody in the world has ever heard before? Can you make musical
> "instruments" that you can interact with to perform music that you
> could never make with a piano or a violin? What else could you create,
> that nobody before you has ever made?

## Resource List for educators

::: {#tab:placeholder}
|  |  |  |  |  |  |  |
|:---|:---|:---|:---|:---|:---|:---|
| **Name** | **Type** | **Context** | **Open Source** | **Notes** | **Audience** | **URL** |
|  |  |  |  |  |  |  |
| EarSketch | Browser-based | Beginner music making |  | Python or JavaScript |  | earsketch.gatech.edu |
| gm (R) | R music library | Data science |  | R |  | flujoo.github.io/gm |
| JythonMusic | Standalone app | Beginner music making |  | Python |  | jythonmusic.me |
| Mido | Python MIDI library | Beginner music making |  | Python |  | mido.readthedocs.io |
| Max | Standalone app, Visual coding | Music making | X |  | musicians |  |
| PureData | Standalone app, Visual coding |  |  |  |  | puredata.info |
| Scratch | Browser-based visual coding | Beginner music / game / animation |  | Visual coding | young learners | scratch.mit.edu |
| Sonic Pi | Standalone app |  |  | Ruby | young learners | sonic-pi.net |
| Strudel | Browser-based port of TidalCycles |  |  |  |  | strudel.cc |
| SuperCollider |  |  |  |  |  |  |
| Tau5 | Browser-based or Standalone app |  |  |  |  | tau5.live |
| TidalCycles | live coding environment |  |  | Requires SuperCollider / SuperDirt for sound output |  | tidalcycles.org |
| TunePad | Browser-based |  |  | Python |  | tunepad.com |
| Wav libraries | Libraries for various |  |  |  |  |  |

: An incomplete list of software and software libraries that can be
helpful in exploring music, sound and coding
:::

[^1]: Lots of open source synthesisers are available such as [Surge
    XT](https://surge-synthesizer.github.io/) or
    [Dexed](https://asb2m10.github.io/dexed/)

[^2]: <https://scratch.mit.edu/educators/>

[^3]: <https://sonic-pi.net>

[^4]: e.g. see work by DJ_Dave in Sonic Pi
    <https://www.youtube.com/watch?v=w2s1DK1w3WI>

[^5]: <https://iclc.toplap.org/>

[^6]: <https://earsketch.gatech.edu/>

[^7]: <https://tunepad.com/>

[^8]: <https://strudel.cc/workshop/getting-started/#what-is-strudel>

[^9]: https://tidalcycles.org/

[^10]: see the international Algorave movement for example:
    <https://algorave.com/>
