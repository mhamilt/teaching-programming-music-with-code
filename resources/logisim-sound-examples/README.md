# Building a digital circuit to play sounds and notes using Logisim Evolution

## Summary
This project is an example showing how to use the buzzer in Logisim evolution to play sounds and notes.

[Logisim Evolution](https://github.com/logisim-evolution/logisim-evolution) is a Free open-source and cross-platform digital logic design tool and simulator.

The project contains 3 main circuits and 1 sub-circuit:
* **buzzer_example:** A minimal example showing how to use the buzzer.
* **buzzer_example_2:** A more advanced example, showing how to use a bit extender and an adder to generate the required frequency input in a more convenient way.
* **scale_example:** A circuit playing the C major scale using a counter and a multiplexer.
* **countupdown:** A sub-circuit used in *scale_example* to count up from 0 to 7 and back down from 7 to 0.

## Prerequisite Knowledge
Basic knowledge of digital logic and how to use Logisim Evolution is required.

Tutorials for Logisim Evolution in various languages can be found here: https://baillifard.com/logisim/index.html

## Programming concepts and methods
This project makes use of the following:

* Digital logic concepts and components:
    * Inputs
    * Outputs
    * Counters
    * D Flip-Flop
    * Bit extenders
    * Adders
    * Binary and hexadecimal representation

* Logisim Evolution features:
    * Buzzers
    * Tunnels
    * Slider inputs
    * Auto-tick mode
    * Sub-circuits

## How this resource could be used
Only minimal knowledge is required to test run the project and it can be used as part of a tutorial on digital logic and Logisim Evolution.

Alternatively, it could be used as an assignment.

It can also be used in music teaching to explain how notes relate to frequencies.

## How could this be taken further

Motivated students/learners could create a complete digital piano keyboard or synthesizer. Or play preset tunes from a digital memory.
Such circuits could then potentially be implemented in real hardware later on.

Examples:
* [My CPU With Improved Sound and MIDI Musical Keyboard Via Logisim](https://www.youtube.com/watch?v=_VW074myq44)
* [Logisim Evolution Zelda Song
](https://www.youtube.com/watch?v=IeLRGjTXq50)

## Technical Resources or Requirements
* [Logisim Evolution](https://github.com/logisim-evolution/logisim-evolution)

This project was last successfully tested on:
```
Product: Logisim-evolution v4.1.0
Runs on: OpenJDK 64-Bit Server VM v21.0.4
Compiled: 2026-02-15T09:15:56+0100
Build ID: main/632d66dc
Built on: OpenJDK 64-Bit Server VM v21.0.4
```

## How to use each example circuit
### buzzer_example
![buzzer_example.png](screenshots/buzzer_example.png?raw=true)
A minimal example showing how to use the buzzer.

1) Select hand tool.
2) Set enable sound to 1.
3) Set frequency to 440 (A4 note: 440 Hz).
4) Increase duty cycle above zero.
5) Increase volume above zero.
6) Try different waveform types in the buzzer properties or different frequencies and duty cycles.

Notes:
* The audible frequency range for humans is approximately 20-20000 Hz.
* 440 Hz is the frequency of the note A4.

### buzzer_example_2
![buzzer_example_2.png](screenshots/buzzer_example_2.png?raw=true)
Same as *buzzer_example*, but here the frequency can be set by using a slider to add an offset to the 440 Hz frequency of the A4 note.

It uses a bit extender and an adder to generate the required frequency input in a more convenient way.

How to use:
1) Select hand tool.
2) Set enable sound to 1.
3) Set frequency_offset to zero (which sets frequency to 440 Hz, i.e. the A4 note).
4) Increase duty cycle above zero.
5) Increase volume above zero.
6) Try different waveform types in the buzzer properties or different frequencies and duty cycles.

### scale_example
![scale_example.png](screenshots/scale_example.png?raw=true)
A circuit playing the C major scale using a counter and a multiplexer.

1) Select hand tool.
2) Set enable sound to 1.
3) Increase volume above zero.
4) Enable auto-tick: Simulate->Auto-tick enabled.

Frequencies of the notes in the C major scale:
* C4: 440*2^(-9/12) ~ 262 Hz
* C4#: skipped (black key)
* D4: 440*2^(-7/12) ~ 294 Hz
* D4#: skipped (black key)
* E4: 440*2^(-5/12) ~ 330 Hz
* F4: 440*2^(-4/12) ~ 349 Hz
* F4#: skipped (black key)
* G4: 440*2^(-2/12) ~ 392 Hz
* G4#: skipped (black key)
* A4: 440 Hz
* A4#: skipped (black key)
* B4: 440*2^(2/12) ~ 494 Hz
* C5: 440*2^(3/12) ~ 523 Hz

References:
* [Piano key frequencies
](https://en.wikipedia.org/wiki/Piano_key_frequencies)
* [Scientific pitch notation
](https://en.wikipedia.org/wiki/Scientific_pitch_notation)

### countupdown
![countupdown.png](screenshots/countupdown.png?raw=true)
A sub-circuit used in *scale_example* to count up from 0 to 7 and back down from 7 to 0.
