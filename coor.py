import cv2
import os
import glob
import random
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
thickness = 2
n=3
root =r"D:\project_data\fire\select_fake"
store = r"D:\project_data\fire\annotated"
image_paths = map(str,glob.glob(os.path.join(root, '*.jpg')))
classes_db = {
	'Smoke': (13,90,244), #244, 90, 13 
	'Mary': (0,255,0),
}

for img_path in image_paths:
	#print(img_path)
	frame = cv2.imread(img_path)
	with open(img_path.replace('.jpg','.txt'),"r") as f:
		for line in f:
			line = line.rstrip('\n')
			classes,xmin,ymin,xmax,ymax = line.split(" ")
			xmin = int(xmin) + random.randint(-n, +n)
			ymin = int(ymin) + random.randint(-n, +n)
			xmax = int(xmax) + random.randint(-n, +n)
			ymax = int(ymax) + random.randint(-n, +n)
			frame=cv2.rectangle(frame, (xmin,ymin), (xmax,ymax),classes_db.get(classes), 2)
			#frame = cv2.rectangle(frame, (xmin, ymin - 30),((xmin + len(classes)*20), ymin),(0,255,0), 2)
			frame= cv2.rectangle(frame, (xmin, ymin),
                        (xmin+(len(classes_db.get(classes)))*40, ymin-30), classes_db.get(classes), -1)
			frame= cv2.putText(frame, classes,(xmin, ymin), font,fontScale,(255,255,255), thickness, cv2.LINE_AA)
			#cv2.putText(frame, classes,,, 0.75,classes_db.get(classes),2)
		cv2.imshow('img',frame)
		cv2.waitKey(1)
	cv2.imwrite(img_path.replace(root,store),frame)
# frame = cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (255,255,255), 2)
# frame =cv2.rectangle(frame, (int(bbox[0]), int(bbox[1]-30)), (int(bbox[0])+(len(class_name)+len(str(track.track_id)))*17, int(bbox[1])), (255,255,255), -1)