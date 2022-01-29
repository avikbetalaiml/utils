import os
import cv2
import glob

root ="/home/ispeck/current_project/face_img"
img_paths=[str(img_path) for img_path in glob.glob(os.path.join(root, '*.jpg'))]

result = cv2.VideoWriter('Test.avi',cv2.VideoWriter_fourcc(*'MJPG'),10, (400,400))

for img in img_paths:
	frame = cv2.imread(img)
	frame = cv2.resize(frame,(400,400))
	result.write(frame)
	cv2.imshow('Frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

result.release()
cv2.destroyAllWindows() 
