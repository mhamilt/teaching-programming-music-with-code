#!/usr/bin/env python3

'''
https://piano-music-theory.com/2016/05/31/major-scales/
https://12tonemusic.wordpress.com/2014/08/28/12-sounds-21-symbols-and-15-major-keys-by-mike-overly/
https://en.wikipedia.org/wiki/Major_and_minor
https://en.wikipedia.org/wiki/Circle_of_fifths
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

PREFER_SHARP=True
PREFER_NATURAL=True
ALL_NAMES=False

# print(len(note_name))

def getNoteName(idx_in, prefer_sharp=PREFER_SHARP, prefer_natural=PREFER_NATURAL, all_names=ALL_NAMES):
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
    return [getNoteName(idx, prefer_sharp=prefer_sharp, prefer_natural=prefer_natural, all_names=all_names) for idx in idx_list]

def printCircleOfFifths():
    for i in range(13):
        # print(i, 7*i, 7*i/12, (7*i)%12)
        note_idx = (7*i)%12
        print(i, note_idx, note_name[note_idx])

def printMajorScales():
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
    print(' - '.join(getNoteNames(range(12))))

def printStandardScale():
    for i in range(13):
        print(i, getNoteName(i, all_names=True))

def CountMajorScales():
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
CountScales(minor=False)
CountScales(minor=True)
