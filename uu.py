import cv2
import os
import glob
import random

l =[]
root =r"D:\project_data\pharma\result"
store = r"D:\project_data\video"
image_paths = map(str,glob.glob(os.path.join(root, '*.jpg')))
for img_path in image_paths:
	#print(img_path)
	
	frame = cv2.imread(img_path)
	with open(img_path.replace('.jpg','.txt'),"r") as f:
		for line in f:
			line = line.rstrip('\n')
			classes,xmin,ymin,xmax,ymax = line.split(" ")
			print(classes)
			l.append(classes)

print(list(set(l)))
