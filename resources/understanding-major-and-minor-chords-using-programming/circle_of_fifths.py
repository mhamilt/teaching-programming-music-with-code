#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
https://piano-music-theory.com/2016/05/31/major-scales/
https://12tonemusic.wordpress.com/2014/08/28/12-sounds-21-symbols-and-15-major-keys-by-mike-overly/
https://en.wikipedia.org/wiki/Major_and_minor
https://en.wikipedia.org/wiki/Circle_of_fifths
'''

'''
The 12 notes (cf piano keyboard, white and black keys) in the "chromatic scale":
B#,C,
    C#,Db
D,
    D#,Eb
E,Fb
F,E#
    F#,Gb
G,
    G#,Ab
A,
    A#,Bb
B,Cb
'''
note_name = ['B#,C',
            'C#,Db',
            'D',
            'D#,Eb',
            'E,Fb',
            'F,E#',
            'F#,Gb',
            'G',
            'G#,Ab',
            'A',
            'A#,Bb',
            'B,Cb']

# default values for arguments in functions below
PREFER_SHARP=True
PREFER_NATURAL=True
ALL_NAMES=False

# print(len(note_name))

def getNoteName(idx_in, prefer_sharp=PREFER_SHARP, prefer_natural=PREFER_NATURAL, all_names=ALL_NAMES):
    """
    Return the note letter (i.e. C, C#, Bb, etc) corresponding to idx_in%12 (i.e. idx_in=12 is equivalent to 0, idx_in=13 to 1, etc).
    The value of idx_in%12 is matched to the note letters as follows:
    0 -> B#, C
    1 -> C#, Db
    2 -> D
    3 -> D#, Eb
    4 -> E, Fb
    5 -> F, E#
    6 -> F#, Gb
    7 -> G
    8 -> G#, Ab
    9 -> A
    10 -> A#, Bb
    11 -> B, Cb

    Args:
        idx_in (int): numeric index of the note
        prefer_sharp (bool, optional): Prefer sharp note letters (ex: C# instead of Db). Defaults to True.
        prefer_natural (bool, optional): Prefer natural note letters (ex: F instead of E#).. Defaults to True.
        all_names (bool, optional): Show all note letters (i.e. "F#, Gb" instead of just "F#" or "Gb"). Defaults to False.

    Returns:
        str: Note letter (or letters if all_names=True)
    """

    idx = idx_in%12
    if idx==0:
        if all_names:
            return 'B#/C'
        else:
            if prefer_natural or (not prefer_sharp):
                return 'C'
            else:
                return 'B#'
    elif idx==1:
        if all_names:
            return 'C#/D♭'
        else:
            if prefer_sharp:
                return 'C#'
            else:
                return 'D♭'
    elif idx==2:
        return 'D'
    elif idx==3:
        if all_names:
            return 'D#/E♭'
        else:
            if prefer_sharp:
                return 'D#'
            else:
                return 'E♭'
    elif idx==4:
        if all_names:
            return 'E/F♭'
        else:
            if prefer_natural or prefer_sharp:
                return 'E'
            else:
                return 'F♭'
    elif idx==5:
        if all_names:
            return 'E#/F'
        else:
            if prefer_natural or (not prefer_sharp):
                return 'F'
            else:
                return 'E#'
    elif idx==6:
        if all_names:
            return 'F#/G♭'
        else:
            if prefer_sharp:
                return 'F#'
            else:
                return 'G♭'
    elif idx==7:
        return 'G'
    elif idx==8:
        if all_names:
            return 'G#/A♭'
        else:
            if prefer_sharp:
                return 'G#'
            else:
                return 'A♭'
    elif idx==9:
        return 'A'
    elif idx==10:
        if all_names:
            return 'A#/B♭'
        else:
            if prefer_sharp:
                return 'A#'
            else:
                return 'B♭'
    elif idx==11:
        if all_names:
            return 'B/C♭'
        else:
            if prefer_natural or prefer_sharp:
                return 'B'
            else:
                return 'C♭'

    raise

def getNoteNames(idx_list, prefer_sharp=PREFER_SHARP, prefer_natural=PREFER_NATURAL, all_names=ALL_NAMES):
    """
    Similar to **getNoteName**, but works for a list of numeric index values.

    Args:
        idx_list (int): _description_
        prefer_sharp (bool, optional): Prefer sharp note letters (ex: C# instead of Db). Defaults to True.
        prefer_natural (bool, optional): Prefer natural note letters (ex: F instead of E#).. Defaults to True.
        all_names (bool, optional): Show all note letters (i.e. "F#, Gb" instead of just "F#" or "Gb"). Defaults to False.

    Returns:
        list: list of note letters
    """    
    return [getNoteName(idx, prefer_sharp=prefer_sharp, prefer_natural=prefer_natural, all_names=all_names) for idx in idx_list]

def printCircleOfFifths():
    """
    Prints out the note letters on the circle of fifths in clockwise order.
    First, it prints the note letters on the major circle of fifths, starting from C.
    Second, it prints the note letters on the minor circle of fifths, starting from a.
    """ 
    print('Outer circle')   
    for i in range(12):
        # print(i, 7*i, 7*i/12, (7*i)%12)
        note_idx = (7*i)%12
        print(f'i: {i}, note_idx: (7*{i})%12={note_idx}, note_name[{note_idx}]: {note_name[note_idx]}')
    print('Inner circle')
    for i in range(12):
        # print(i, 7*i, 7*i/12, (7*i)%12)
        note_idx = (9+7*i)%12
        print(f'i: {i}, note_idx: (7*{i})%12={note_idx}, note_name[{note_idx}]: {note_name[note_idx].lower()}')

def printMajorScales():
    """
    Print the 12 major scales corresponding to the 12 semitones in the chromatic scale.
    """
    seq = [0,2,4,5,7,9,11,12]
    for idx in range(12):
        idx_list = [idx+i for i in seq]
        tonic = getNoteName(idx)
        all_names = False
        prefer_natural = True
        prefer_sharp = True
        if '#' in tonic:
            prefer_sharp = True
            prefer_natural = False
        elif 'b' in tonic:
            prefer_sharp = False
            prefer_natural = False
        name = 'unknown'
        if len(tonic)==1:
            name = f'{tonic} Major Scale'
        print(idx, ':', name, ':', ' - '.join(getNoteNames(idx_list, prefer_sharp=prefer_sharp, prefer_natural=prefer_natural, all_names=all_names)))

def printMajorScale(idx_tonic, prefer_sharp=PREFER_SHARP, prefer_natural=PREFER_NATURAL, all_names=ALL_NAMES):
    """
    For a given tonic index

    Args:
        idx_tonic (int): index of the tonic (first note in scale)
        prefer_sharp (bool, optional): Prefer sharp note letters (ex: C# instead of Db). Defaults to True.
        prefer_natural (bool, optional): Prefer natural note letters (ex: F instead of E#).. Defaults to True.
        all_names (bool, optional): Show all note letters (i.e. "F#, Gb" instead of just "F#" or "Gb"). Defaults to False.

    Returns:
        _type_: _description_
    """    
    seq = [0, 2, 4, 5, 7, 9, 11, 12]
    idx_list = [idx_tonic + i for i in seq]
    # tonic = getNoteName(idx_tonic, prefer_sharp=prefer_sharp, prefer_natural=prefer_natural, all_names=all_names)
    note_names = getNoteNames(idx_list, prefer_sharp=prefer_sharp, prefer_natural=prefer_natural, all_names=all_names)
    tonic = note_names[0]
    name = 'unknown'
    if len(tonic) == 1:
        name = f'{tonic} Major Scale'
    elif tonic[1]=='#':
        name = f'{tonic[0]} Sharp Major Scale'
    elif tonic[1]=='♭':
        name = f'{tonic[0]} Flat Major Scale'
    else:
        raise
    scale_str = ' - '.join(note_names)
    # get unique upper case letters
    letters = set()
    for i in scale_str:
        if i in 'CDEFGAB':
            letters.add(i)
    Nletters = len(letters)

    sout = f"{idx_tonic} : {name} : {scale_str} : count(#/♭) = {scale_str[:-1].count('#')}/{scale_str[:-1].count('♭')} : Nletters={Nletters}"
    if Nletters!=7:
        return (sout, False)
    else:
        return (sout, True)

def printMinorScale(idx_tonic, prefer_sharp=PREFER_SHARP, prefer_natural=PREFER_NATURAL, all_names=ALL_NAMES):
    """_summary_

    Args:
        idx_tonic (_type_): _description_
        prefer_sharp (bool, optional): Prefer sharp note letters (ex: C# instead of Db). Defaults to True.
        prefer_natural (bool, optional): Prefer natural note letters (ex: F instead of E#).. Defaults to True.
        all_names (bool, optional): Show all note letters (i.e. "F#, Gb" instead of just "F#" or "Gb"). Defaults to False.

    Returns:
        _type_: _description_
    """
    seq = [0, 2, 3, 5, 7, 8, 10, 12]
    idx_list = [idx_tonic + i for i in seq]
    # tonic = getNoteName(idx_tonic, prefer_sharp=prefer_sharp, prefer_natural=prefer_natural, all_names=all_names)
    note_names = getNoteNames(idx_list, prefer_sharp=prefer_sharp, prefer_natural=prefer_natural, all_names=all_names)
    note_names = [i.lower() for i in note_names]
    tonic = note_names[0]
    name = 'unknown'
    scale_type = 'Minor'
    if len(tonic) == 1:
        name = f'{tonic} {scale_type} Scale'
    elif tonic[1]=='#':
        name = f'{tonic[0]} Sharp {scale_type} Scale'
    elif tonic[1]=='♭':
        name = f'{tonic[0]} Flat {scale_type} Scale'
    else:
        raise
    scale_str = ' - '.join(note_names)
    # get unique upper case letters
    letters = set()
    for i in scale_str:
        if i in 'CDEFGAB'.lower():
            letters.add(i)
    Nletters = len(letters)

    sout = f"{idx_tonic} : {name} : {scale_str} : count(#/♭) = {scale_str[:-1].count('#')}/{scale_str[:-1].count('♭')} : Nletters={Nletters}"
    if Nletters!=7:
        return (sout, False)
    else:
        return (sout, True)

def getScale(idx_tonic, prefer_sharp=PREFER_SHARP, prefer_natural=PREFER_NATURAL, all_names=ALL_NAMES, minor=False):
    """_summary_

    Args:
        idx_tonic (_type_): _description_
        prefer_sharp (bool, optional): Prefer sharp note letters (ex: C# instead of Db). Defaults to True.
        prefer_natural (bool, optional): Prefer natural note letters (ex: F instead of E#).. Defaults to True.
        all_names (bool, optional): Show all note letters (i.e. "F#, Gb" instead of just "F#" or "Gb"). Defaults to False.
        minor (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """    
    if minor:
        scale_type = 'Minor'
        seq = [0, 2, 3, 5, 7, 8, 10, 12]
    else:
        scale_type = 'Major'
        seq = [0, 2, 4, 5, 7, 9, 11, 12]

    idx_list = [idx_tonic + i for i in seq]
    # tonic = getNoteName(idx_tonic, prefer_sharp=prefer_sharp, prefer_natural=prefer_natural, all_names=all_names)
    note_names = getNoteNames(idx_list, prefer_sharp=prefer_sharp, prefer_natural=prefer_natural, all_names=all_names)
    if minor:
        note_names = [i.lower() for i in note_names]
    tonic = note_names[0]
    name = 'unknown'
    if len(tonic) == 1:
        name = f'{tonic} {scale_type} Scale'
    elif tonic[1]=='#':
        name = f'{tonic[0]} Sharp {scale_type} Scale'
    elif tonic[1]=='♭':
        name = f'{tonic[0]} Flat {scale_type} Scale'
    else:
        raise
    scale_str = ' - '.join(note_names)
    # get unique upper case letters
    letters = set()
    letters_valid = 'CDEFGAB'
    if minor:
        letters_valid = letters_valid.lower()
    for i in scale_str:
        if i in letters_valid:
            letters.add(i)
    Nletters = len(letters)

    sharp_count = scale_str[:-1].count('#')
    flat_count = scale_str[:-1].count('♭')
    sout = f"{idx_tonic} : {tonic} : {name} : {scale_str} : count(#/♭) = {sharp_count}/{flat_count} : Nletters={Nletters}"
    if Nletters!=7:
        valid = False
    else:
        valid = True
    return (sout, valid, sharp_count, flat_count)

def printCMajorScale():
    """_summary_
    """    
    print(' - '.join(getNoteNames(range(12))))

def printStandardScale():
    """_summary_
    """    
    for i in range(13):
        print(i, getNoteName(i, all_names=True))

def CountMajorScales():
    """_summary_
    """    
    Nscales = 0
    for i in range(12):
        print(f'===> i={i}')
        valid_str_set = set()
        for prefer_sharp in [True, False]:
            for prefer_natural in [True, False]:
                sout, valid = printMajorScale(i, prefer_sharp=prefer_sharp, prefer_natural=prefer_natural, all_names=False)
                if valid:
                    valid_str_set.add(sout)
        for sout in valid_str_set:
            print(sout)
            Nscales+=1
    print(f'Nscales = {Nscales}')

def CountMinorScales():
    """_summary_
    """    
    Nscales = 0
    for i in range(12):
        print(f'===> i={i}')
        valid_str_set = set()
        for prefer_sharp in [True, False]:
            for prefer_natural in [True, False]:
                sout, valid = printMinorScale(i, prefer_sharp=prefer_sharp, prefer_natural=prefer_natural, all_names=False)
                if valid:
                    valid_str_set.add(sout)
        for sout in valid_str_set:
            print(sout)
            Nscales+=1
    print(f'Nscales = {Nscales}')

def CountScales(minor=False):
    """_summary_

    Args:
        minor (bool, optional): _description_. Defaults to False.
    """    
    start_scale = ''
    scale_dict_sharp = dict()
    scale_dict_flat = dict()
    Nscales = 0
    for i in range(12):
        print(f'===> i={i}')
        valid_str_set = set()
        for prefer_sharp in [True, False]:
            for prefer_natural in [True, False]:
                (sout, valid, sharp_count, flat_count) = getScale(i, prefer_sharp=prefer_sharp, prefer_natural=prefer_natural, all_names=False, minor=minor)
                if valid:
                    valid_str_set.add(sout)
                    if sharp_count == flat_count == 0:
                        start_scale = sout
                    else:
                        if sharp_count>0:
                            # if sharp_count in scale_dict_sharp.keys():
                            #     print(f'key #{sharp_count} already in!:')
                            #     print(f'    old: {scale_dict_sharp[sharp_count]}')
                            #     print(f'    new: {sout}')
                                # raise
                            scale_dict_sharp[sharp_count] = sout
                        # print('flat_count',flat_count)
                        if flat_count>0:
                            # if flat_count in scale_dict_flat.keys():
                            #     print(f'key b{flat_count} already in!:')
                            #     print(f'    old: {scale_dict_flat[flat_count]}')
                            #     print(f'    new: {sout}')
                                # raise
                            scale_dict_flat[flat_count] = sout
        for sout in valid_str_set:
            print(sout)
            Nscales+=1
    print(f'Nscales = {Nscales}')
    print('===> Start scale:')
    print(start_scale)
    print('===> Sorted sharp scales:')
    for k,v in sorted(scale_dict_sharp.items()):
        print(f'#={k} -> {v}')
    print('===> Sorted flat scales:')
    for k,v in sorted(scale_dict_flat.items()):
        print(f'♭={k} -> {v}')

# CountMajorScales()
# CountMinorScales()
# printStandardScale()
# printCircleOfFifths()
# print('==================== Counting major scales start')
# CountScales(minor=False)
# print('==================== Counting major scales end')
# print('==================== Counting minor scales start')
# CountScales(minor=True)
# print('==================== Counting minor scales end')

# printMajorScales()
for i in range(12):
    print(printMajorScale(i))
