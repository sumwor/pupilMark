# utility functions of the pupil mark
import os
from scipy.io import loadmat
import numpy as np


def get_files(filePath):
    """
    :param filePath: the full path of the directory
    :return: a list of .mat files from the directory
    """

    files = []
    for file in os.listdir(filePath):
        if file.endswith(".mat"):
           files.append(os.path.join(filePath, file))

    return files


def get_mat(files):
    """
    read in all the .mat files, convert to a picture format
    :param files: full file path of a .mat files
    :return: a data matrix
    """
    mat = loadmat(files)
    data = mat['data']

    return data


def get_frame(files):
    """
    a function to get the dimension of the full session of recordings
    :param files: a list of all recordings
    :return: number of frames
    """
    frames = 0
    for file in files:
        data = get_mat(file)
        frame = np.shape(data)[0]
        frames += frame

    return frames
