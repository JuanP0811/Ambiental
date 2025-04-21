#Sequence of Images Video Temperature
#Libraries Import
import cv2
import numpy as np
import os

#In and Out Paths
path ='c:/Users/USER/Devi/Investigacion/Avances/Cuenca/PNG/TEMP/00_LT/'
out_path = 'c:/Users/USER/Devi/Investigacion/Avances/Cuenca/VID/'
out_video_name = 'TEMP.mp4'
full_video_name = out_path + out_video_name

#Add the names of the images to a pre image array
pre_img_array = os.listdir(path)
#We create a void array to store the images 
img = []
#Adding the path to the name of each file in img array
for i in pre_img_array:
    i=path+i
    img.append(i)
# Creating the video variables for CODEC and size, 'X','V','I','D'
fourcc= cv2.VideoWriter_fourcc(*'mp4v')
frame= cv2.imread(img[0])
# Create an array of three elements (height, width, layers)
size=list(frame.shape)
# Delete the layer element
del size[2]
# Reverse the order of the remaining elements to input the following method)
size.reverse()
# Use the method VideoWriter to set the path+name, CODEC, fps (frames per second), size and isColor (0 = original)
video = cv2.VideoWriter(full_video_name,fourcc,0.7,size)
#Loop to set each image to the video in a sequence, 24 images in total
for j in range(len(img)):
    video.write(cv2.imread(img[j]))
    print(img[j])
#Show video output location
print('Output video to:',full_video_name)
#Release video in the corresponding folder
video.release()
#Close any open window, end of the program
cv2.destroyAllWindows()
