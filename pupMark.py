from PIL import Image, ImageEnhance
from pylab import *
from pupUtils import *
import numpy as np



# changing the contrast of the frame to get optimal marking
contrast = 1.5
sharpness = 5
brightness = 1.5

# edit the repeat number to save different files
repeat = 0  # the number of repeat times (you need to repeatedly mark the frames to get a mean and standard deviation

# get the files
filePath = 'E:\labcode\pupilMarkData\data'
savePath = filePath + '\markResults\pupPos' + str(repeat) + '.npy'
sessionPath = filePath + '\sessionData.npy'

# create the directory that stores the mark results
if not os.path.exists(filePath + '\markResults'):
    os.mkdir(filePath + '\markResults')
matFiles = get_files(filePath)

# remove the first recording because it is too long XD
matFiles.pop(0)

numFrames = get_frame(matFiles)

# read in all the frames (guess it is not too big)
if os.path.exists(sessionPath):
    sessionData = np.load(sessionPath)
else:
    sessionData = np.zeros((200, 320, numFrames))
    i = 0
    for file in matFiles:
        data = get_mat(file)
        for ii in range(len(data)):
            sessionData[:, :, i] = get_mat(file)[ii,0]
            i += 1
            if (i % 100) == 0:
                print(i)

    if i == numFrames:
        print("success!")

    np.save(sessionPath, sessionData)


print("there are %i frames in the session, good luck! " % numFrames)
# a matrix to save all the entries

pupPos = np.zeros((5, 2, numFrames))
# five positions in total
# up, down, left, right, center

# the main loop to show frames one by one to mark the positions


# check how many frames are marked so far
if os.path.exists(savePath):
    pupPos = np.load(savePath)
    nonZeroInd = np.where(pupPos[0, 0, :] != 0)
    lastEntry = nonZeroInd[0][-1]
else:
    lastEntry = -1


for ii in range(lastEntry+1, numFrames):
    # checking whether there is saved data
    frame = sessionData[:, :, ii]
    img = Image.fromarray(frame)
    # img.save('test.png')
    # im = array(Image.open('test.jpg'))
    # adjusting the imaging quality
    img = ImageEnhance.Sharpness(img).enhance(sharpness)
    img = ImageEnhance.Brightness(img).enhance(brightness)
    img = ImageEnhance.Contrast(img).enhance(contrast)

    imshow(img)
    print('Please click 5 points in the order of up, down, left, right, center')
    x = ginput(5)

    i = 0
    for pos in x:
        # in the order of up, down, left, right, center
        pupPos[i, :, ii] = list(x[i])
        i += 1

    np.save(savePath, pupPos)
    # print('you clicked:', x)

    show()
