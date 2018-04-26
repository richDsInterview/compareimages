# -*- coding: utf-8 -*-
from . import helpers
import numpy as np
import imageio
import cv2
from PIL import Image
import dhash

# compare_images_exact: a method to compare whether two images are precisely the same
def compare_images_exact(image_path1, image_path2):
    try:
        im1 = imageio.imread(image_path1)
        im2 = imageio.imread(image_path2)
    except FileNotFoundError: # file does not exist
        print("compare_images_phash: one of the file arguments does not exist")
        return None
    except ValueError: # file is not an image file
        print("compare_images_exact: one of the file arguments is not an image file")
        return None
    except Exception: # unexpected/unknown exception
        print("compare_images_exact: unexpected/unhandled behaviour in image file reading process")
        return None

    # check whether the numpy representations of the images match
    if np.array_equal(im1, im2):
        return 1.0
    else:
        return 0.0


# compare_images_scaled: a method to compare two images that are possibly scaled versions of each
# other. Optional arguments are to first convert to thumbnail representations, to quantise
# colour information (make greyscale), and quantise pixel values.
def compare_images_scaled(image_path1, image_path2, thumb=True, grey=False, pixelQuant=8, gridsize=16):
    # unlike imageio, cv2 won't throw an error if a file is not an image,
    # or does not exist, but simply returns Nonetype object
    im1 = cv2.imread(image_path1)
    im2 = cv2.imread(image_path2)

    if im1 is None or im2 is None:
        return None

    # if desired, convert both images to thumbnails of specified size
    if thumb:
        im1 = cv2.resize(im1, dsize=(gridsize, gridsize))
        im2 = cv2.resize(im2, dsize=(gridsize, gridsize))
    # otherwise, convert images to a common grid, the smallest of the two
    # assumes reasonable scale relationship between images
    else:
        if im1.size<im2.size:
            im2 = cv2.resize(im2, dsize=(im1.shape[1], im1.shape[0]))
        else:
            im1 = cv2.resize(im1, dsize=(im2.shape[1], im2.shape[0]))
    # if desired, convert images to greyscale using the OpenCV library
    if grey:
        im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
        im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    #scale by the pixel quantisation amount
        im1 = im1//pixelQuant
        im2 = im2//pixelQuant

    # return the Hamming difference between the two images and the difference image
    # score, diff = helpers.
    score = 1 - np.count_nonzero(im1 != im2)/im1.size
    diff = np.abs(im1-im2)
    return score, diff


def compare_images_phash(image_path_1, image_path_2):
    try: # open images, error checking inputs
        image_1 = PIL.Image.open(image_path_1)
        image_2 = PIL.Image.open(image_path_2)
    except FileNotFoundError:# file does not exist
        print("compare_images_phash: one of the file arguments does not exist")
        return None
    except OSError:# filename not an image file
        print("compare_images_phash: one of the specified files is not an image file: can't compare")
        return None

    # hash each image file with a difference hashing algorithm
    dh1 = dhash.dhash_int(image_1)
    dh2 = dhash.dhash_int(image_2)

    # return a 'score' of the Hamming distance between the two hashes (normalised by hash length), and the diff vector
    score = 1 - dhash.get_num_bits_different(dh1, dh2) / dh1.bit_length()
    diff = np.array([hex(dh1 ^ dh2)])
    return score, diff

def hello():
    return "hello"

def get_hmm():
    """Get a thought."""
    return 'hmmm...'

def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())
