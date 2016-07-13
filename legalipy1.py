from __future__ import unicode_literals  # for python2 compatibility
# -*- coding: utf-8 -*-
# created at UC Berkeley 2015
# Authors: Christopher Hench & Alex Estes © 2016
# ==============================================================================

'''This program syllabifies any text in any language
solely on the Onset Maximization principle (Principle of Legality).
Input is text file'''

import codecs
import re
import csv
import sys
from datetime import datetime
import string
from collections import Counter


def cleantext(text):
    text = ''.join([x for x in text if not x.isdigit()])

    remove_char = string.punctuation + '»«˃˂〈〉♦•—¿·'
    for char in text:
        if char in remove_char:
            text = text.replace(char, '')

    return (text.split())  # return list of words, alt tokenize


def getonsets(text):

    vowels = 'aeiouyàáâäæãåāèéêëēėęîïíīįìôöòóœøōõûüùúūůÿ'

    tokens = cleantext(text)

    onsets = []
    for word in tokens:
        word = word.lower()
        onset = ""
        for letter in word:
            if letter not in vowels:  # onset is everying up to first vowel
                onset += letter
            else:
                break
        onsets.append(onset)

    onsets = [x for x in onsets if x != '']  # get rid of empty onsets

    # now remove onsets caused by errors, i.e. less than .02% of onsets
    freq = Counter(onsets)

    total_onsets = 0
    for k, v in freq.items():
        total_onsets += v

    onsets = []
    for k, v in freq.items():
        if (v / total_onsets) > .0002:
            onsets.append(k)

    return (onsets, tokens)


def legalipy(word, onsets):

    longest_onset = len(max(onsets, key=len))
    vowels = 'aeiouyàáâäæãåāèéêëēėęîïíīįìôöòóœøōõûüùúūůÿ'
    vowelcount = 0
    revword = word[::-1]  # reverse word to build onsets from back

    syllset = []
    for letter in revword:
        if letter.lower() in vowels:
            vowelcount += 1
        else:
            pass

    if vowelcount == 1:  # monosyllabic
        syllset.append(revword)

    # begin main algorithm
    elif vowelcount > 1:
        syll = ""

        # following binaries trigger different routes
        onsetbinary = 0
        newsyllbinary = 1

        for letter in revword:

            if newsyllbinary == 1:  # i.e. if we have a new syllable
                if letter.lower() not in vowels:
                    syll += letter

                else:
                    syll += letter
                    newsyllbinary = 0
                    continue

            elif newsyllbinary == 0:  # i.e. no longer new syllable

                if syll == "":  # fixes last syllable
                    syll += letter

                elif (letter.lower() in onsets and syll[-1].lower() in vowels):
                    syll += letter
                    onsetbinary = 1

                elif (letter.lower() + syll[-1].lower() in [ons[-2:] for ons in onsets] and syll[-2].lower() in vowels):
                    syll += letter
                    onsetbinary = 1

                elif (letter.lower() + syll[-2:][::-1].lower() in [ons[-3:] for ons in onsets] and syll[-3].lower() in vowels):
                    syll += letter
                    onsetbinary = 1

                elif (letter + syll[-3:][::-1].lower() in [ons[-4:] for ons in onsets] and syll[-4].lower() in vowels):
                    syll += letter
                    onsetbinary = 1

                # order is important for following two due to onsetbinary
                # variable
                # i.e. syllable doesn't end in vowel (onset not yet found)
                elif letter.lower() in vowels and onsetbinary == 0:
                    syll += letter

                # i.e. syllable ends in vowel, onset found, restart syllable
                elif letter.lower() in vowels and onsetbinary == 1:
                    syllset.append(syll)
                    syll = letter

                else:
                    syllset.append(syll)
                    syll = letter
                    newsyllbinary = 1

        syllset.append(syll)

    # reverse syllset then reverse syllables
    syllset = [syll[::-1] for syll in syllset][::-1]

    return (syllset)

# MAIN PROGRAM HERE
if __name__ == '__main__':

    print("\n\nLegaliPy-ing...\n")

    sfile = sys.argv[1]  # input text file to syllabify
    with open(sfile, 'r', encoding='utf-8') as f:
        text = f.read()

    onsets = getonsets(text)

    toprintl = []
    for token in onsets[1]:
        toprintl.append(legalipy(token, onsets[0]))

    toprint = ""
    for word in toprintl:
        for syll in word:
            if syll != word[-1]:
                toprint += syll
                toprint += "-"
            else:
                toprint += syll
        toprint += " "

    onsetprint = (" - ".join([x for x in onsets[0]]) + '\n\n')

    prologue = "Following onsets > .02 percent deemed 'legal':\n"

    fmt = '%Y/%m/%d %H:%M:%S'
    date = "LegaliPyed on " + str(datetime.now().strftime(fmt))

    finalwrite = date + "\n\n" + prologue + onsetprint + toprint

    with open('LegaliPyed.txt', 'w', encoding='utf-8') as f:
        f.write(finalwrite)

    print("\nResults saved to LegaliPyed.txt\n\n")
