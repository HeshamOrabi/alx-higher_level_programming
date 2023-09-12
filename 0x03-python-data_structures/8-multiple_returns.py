#!/usr/bin/python3

def multiple_returns(sentence):
    tub = ()
    if sentence[0] == '':
        sentence[0] = None
    tub = len(sentence), sentence[0]

    return tub
