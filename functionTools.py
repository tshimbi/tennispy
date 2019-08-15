#tools function
import re
import numpy as np

def larger(l, nb):
    l = list(set(l))
    return l[-nb:]

def smaller(l, nb):
    l = list(set(l))
    return l[:nb]

def right(s, amount):
    return s[-amount:]

def left(s, amount):
    return s[:amount]

def extractNumberFromString(s):
    regex = re.compile(r'\d+')
    return regex.findall(s)