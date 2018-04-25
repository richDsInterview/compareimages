# -*- coding: utf-8 -*-
from . import helpers
import cv2
import numpy

def get_hmm():
    """Get a thought."""
    return 'hmmm...'

def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())

def compareImagesNumpy(file1, file2):
    return np.array_equal(cv2.imread(file1), cv2.imread(file2))
