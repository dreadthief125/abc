import os
import cv2
path = 'C:/Users/KskYm/Downloads/PRO-C105-Project-Images-main (1)/PRO-C105-Project-Images-main/Images/img'
images = []


for img in path:
  if img:
    images.append(img)
frame=cv2.imread(images[0])
height,width,players=frame.shape
size=(width,height)
out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 5, size)
for i in range(path-1,0,-1):
  frame=cv2.imread(images[i])
  out.write(frame)



