from __future__ import unicode_literals  # for python2 compatibility
# -*- coding: utf-8 -*-
# created at UC Berkeley 2015
# Authors: Christopher Hench & Alex Estes © 2016

import string


def cleantext(text):
    '''
    cleans text of numbers, punctuation, and other non-syllabifiable characters
    '''
    text = ''.join([x for x in text if not x.isdigit()])
    text = ''.join(
        [x for x in text if x not in string.punctuation + '»«˃˂〈〉♦•—¿·'])

    return text
