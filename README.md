# pupilMark

## Usage
### pupMark.py

1. variables to change:

    a) *contrast*, *brightness*, *sharpness*: the display parameters of the recording frames. Change the parameters to achieve a
        optimal boundary of the pupil.
    
    b) *repeat*: Since you need multipul entris to estimate standard deviation and mean, you need to mark the same validate set 
        several times. This parameter allows you to set the number of repeats. Change it every time you start from the beginning.
        
    b) *filePath*: the directory that stores the validate data set (raw data as in .mat)

2. start marking. 
  
    a) There are five points in total. You should click in the exact order: **UP, DOWN, LEFT, RIGHT, CENTER**
    
    b) Next frame will pop up automatically when you are done with the previous one
    
    c) if you have to go in the middle, just close the window. The script will be able to start at the break point the next time 
       you run it
 
 ### checkFig.py
 1. This script is to help with the parameters setting in 1a.
 
 2. *filePath*: change this to **a .mat file** from the validation dataset
 
 3. change the values of the three parameters, run the script to examine the results
 
 ### script to analyze the result and compare with the DeepLabCut results
 
 1. coming soon
