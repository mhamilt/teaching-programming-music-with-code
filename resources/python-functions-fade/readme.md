# Functions in Python

## Summary

This is a notebook to introduce or consolidate the concept of functions and modularity to beginner programming students, using fade-ins and fade-outs on audio files as motivating examples.


## Prerequisite Knowledge

The key prerequisite is a basic knowledge of Python: variables, lists, and loops (and optionally, plotting). Exercise solutions are given with list comprehensions, but can also be done with loops if students are not familiar with comprehensions. Note that if students are familiar with Numpy arrays, this resource can be adapted to replace loops with vectorised operations on Numpy arrays instead.

This resource is probably best suited to students with a bit of a quantitative background, as it refers to some (fairly simple) mathematical notions to contextualise the problem.


## Programming concepts and methods

This introduces functions by motivating them as a way to reuse code and to make programs modular. Throughout the activity, students are encouraged to iterate on their function structure and choice of input/output values, to help them take ownership of their program design, to better understand how and why these choices are made, and to internalise that one-shot perfect code structure isn't necessarily achievable (or even a goal that one should aim for).

### Learning objectives

After going through this notebook, students will be able to:

- Understand the concept and advantages of modularity in programming.
- Define and use basic functions in Python to structure their code, and understand the difference between _defining_ and _calling_ a function.
- Define and use functions with multiple input arguments and return values.
- Recognise when it's useful to provide default values for input arguments.
- Write functions to fade-in, fade-out, and cross-fade audio files.


## How this resource could be used

This could be a teacher-led session, a self-study notebook, or a classroom activity where students follow written instructions with support from a teaching assistant. This could also be split into a taught or self-study part, then students working on the final exercises during a tutorial.


## How could this be taken further

- Expand on positional vs. keyword arguments
- Writing modules and packages (instead of defining functions in the notebook)
- Input argument checking and raising appropriate exceptions for invalid input values
- Docstrings, and generally documentation
- Numpy arrays for efficiency (to replace lists and loops)
- Conditional statements (starting from e.g. the last exercise)


## Technical Resources or Requirements

- Python 3.
- `jupyter-notebook` or `jupyter-lab` to run the notebook.
- `ipywidgets`, for the audio playback widgets.
- `wav_library.py`, provided with this resource as a utility. Note that the construction of this module constitutes [one of the other learning resources provided with this book chapter](), and could be a good follow-up to the activity presented here.
- Two copyright-free mono audio WAVE files. [Freesound](https://freesound.org/) is a great resource to find these. `piano.wav`, `synth.wav`, and `guitar.wav` are provided as examples.
- Optionally, `matplotlib` for plotting waveforms. The plotting sections can be useful to provide another way to visualise the effect of the student's functions, but they can be removed if you have not covered this in your course.
