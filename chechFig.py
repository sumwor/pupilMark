from PIL import Image, ImageEnhance
from pylab import *
from pupUtils import *

filePath = 'F:\\pupildata\\pupil\\M883_phase2_algo2_WithPupil_1905230811\M883_phase2_algo2_WithPupil_1905230811_001.mat'
data = get_mat(filePath)

frame = data[0,0]

img = Image.fromarray(frame)
# for i in range(20):
# img = ImageEnhance.Contrast(img).enhance(1.6)
img = ImageEnhance.Sharpness(img).enhance(5)
img = ImageEnhance.Brightness(img).enhance(1.5)
imshow(img)
show()
#print('Please click 3 points')
#x = ginput(3)
#print('you clicked:', x)
#show()