from __future__ import unicode_literals  # for python2 compatibility
# -*- coding: utf-8 -*-
# created at UC Berkeley 2015
# Authors: Christopher Hench & Alex Estes © 2016
# ==============================================================================

import string


def cleantext(text):
    text = ''.join([x for x in text if not x.isdigit()])

    remove_char = string.punctuation + '»«˃˂〈〉♦•—¿·'
    for char in text:
        if char in remove_char:
            text = text.replace(char, '')

    return (text.split())  # return list of words, alt tokenize
