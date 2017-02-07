from __future__ import unicode_literals  # for python2 compatibility
# -*- coding: utf-8 -*-
# created at UC Berkeley 2015
# Authors: Christopher Hench & Alex Estes © 2016
# ==============================================================================

'''This program syllabifies words based on the Sonority Sequencing Principle (SSP)'''

import codecs


def SonoriPy(word):

    def no_syll_no_vowel(ss):
        # no syllable if no vowel
        nss = []
        front = ""
        for i, syll in enumerate(ss):
            # if following syllable doesn't have vowel,
            # add it to the current one
            if not any(char in vowels for char in syll):
                if len(nss) == 0:
                    front += syll
                else:
                    nss = nss[:-1] + [nss[-1] + syll]
            else:
                if len(nss) == 0:
                    nss.append(front + syll)
                else:
                    nss.append(syll)

        return nss

    # SONORITY HIERARCHY, MODIFY FOR LANGUAGE BELOW
    # categories can be collapsed into more general groups
    vowels = 'aeiouy'
    approximates = ''
    nasals = 'lmnrw'  # resonants and nasals
    fricatives = 'zvsf'
    affricates = ''
    stops = 'bcdgtkpqxhj'  # rest of consonants

    # SONORITY HIERARCHY for IPA
    # # categories can be collapsed into more general groups
    # vowelcount = 0  # if vowel count is 1, syllable is automatically 1
    # sylset = []  # to collect letters and corresponding values
    # for letter in word.strip(".:;?!)('" + '"'):
    #     if letter.lower() in 'aɔʌã':
    #         sylset.append((letter, 9))
    #         vowelcount += 1  # to check for monosyllabic words
    #     elif letter.lower() in 'eéẽɛøoõ':
    #         sylset.append((letter, 8))
    #         vowelcount += 1  # to check for monosyllabic words
    #     elif letter.lower() in 'iu':
    #         sylset.append((letter, 7))
    #         vowelcount += 1  # to check for monosyllabic words
    #     elif letter.lower() in 'jwɥh':
    #         sylset.append((letter, 6))
    #     elif letter.lower() in 'rl':
    #         sylset.append((letter, 5))
    #     elif letter.lower() in 'mn':
    #         sylset.append((letter, 4))
    #     elif letter.lower() in 'zvðʒ':
    #         sylset.append((letter, 3))
    #     elif letter.lower() in 'sfθʃ':
    #         sylset.append((letter, 2))
    #     elif letter.lower() in 'bdg':
    #         sylset.append((letter, 1))
    #     elif letter.lower() in 'ptkx':
    #         sylset.append((letter, 0))
    #     else:
    #         sylset.append((letter, 0))

    vowelcount = 0  # if vowel count is 1, syllable is automatically 1
    sylset = []  # to collect letters and corresponding values
    for letter in word.strip(".:;?!)('" + '"'):
        if letter.lower() in vowels:
            sylset.append((letter, 5))
            vowelcount += 1  # to check for monosyllabic words
        elif letter.lower() in approximates:
            sylset.append((letter, 4))
        elif letter.lower() in nasals:
            sylset.append((letter, 3))
        elif letter.lower() in fricatives:
            sylset.append((letter, 2))
        elif letter.lower() in affricates:
            sylset.append((letter, 1))
        elif letter.lower() in stops:
            sylset.append((letter, 0))
        else:
            sylset.append((letter, 0))

    # below actually divides the syllables
    newsylset = []
    if vowelcount == 1:  # finalize word immediately if monosyllabic
        newsylset.append(word)
    if vowelcount != 1:
        syllable = ''  # prepare empty syllable to build upon
        for i, tup in enumerate(sylset):
            if i == 0:  # if it's the first letter, append automatically
                syllable += tup[0]
            # lengths below are in order to not overshoot index
            # when it looks beyond
            else:
                # add whatever is left at end of word, last letter
                if i == len(sylset) - 1:
                    syllable += tup[0]
                    newsylset.append(syllable)

                # MAIN ALGORITHM BELOW
                # these cases DO NOT trigger syllable breaks
                elif (i < len(sylset) - 1) and tup[1] < sylset[i + 1][1] and \
                        tup[1] > sylset[i - 1][1]:
                    syllable += tup[0]
                elif (i < len(sylset) - 1) and tup[1] > sylset[i + 1][1] and \
                        tup[1] < sylset[i - 1][1]:
                    syllable += tup[0]
                elif (i < len(sylset) - 1) and tup[1] > sylset[i + 1][1] and \
                        tup[1] > sylset[i - 1][1]:
                    syllable += tup[0]
                elif (i < len(sylset) - 1) and tup[1] > sylset[i + 1][1] and \
                        tup[1] == sylset[i - 1][1]:
                    syllable += tup[0]
                elif (i < len(sylset) - 1) and tup[1] == sylset[i + 1][1] and \
                        tup[1] > sylset[i - 1][1]:
                    syllable += tup[0]
                elif (i < len(sylset) - 1) and tup[1] < sylset[i + 1][1] and \
                        tup[1] == sylset[i - 1][1]:
                    syllable += tup[0]

                # these cases DO trigger syllable break
                # if phoneme value is equal to value of preceding AND following
                # phoneme
                elif (i < len(sylset) - 1) and tup[1] == sylset[i + 1][1] and \
                        tup[1] == sylset[i - 1][1]:
                    syllable += tup[0]
                    # append and break syllable BEFORE appending letter at
                    # index in new syllable
                    newsylset.append(syllable)
                    syllable = ""

                # if phoneme value is less than preceding AND following value
                # (trough)
                elif (i < len(sylset) - 1) and tup[1] < sylset[i + 1][1] and \
                        tup[1] < sylset[i - 1][1]:
                    # append and break syllable BEFORE appending letter at
                    # index in new syllable
                    newsylset.append(syllable)
                    syllable = ""
                    syllable += tup[0]

                # if phoneme value is less than preceding value AND equal to
                # following value
                elif (i < len(sylset) - 1) and tup[1] == sylset[i + 1][1] and \
                        tup[1] < sylset[i - 1][1]:
                    syllable += tup[0]
                    # append and break syllable BEFORE appending letter at
                    # index in new syllable
                    newsylset.append(syllable)
                    syllable = ""

    newsylset = no_syll_no_vowel(newsylset)

    return (newsylset)

if __name__ == '__main__':
    print(SonoriPy("justification"))
