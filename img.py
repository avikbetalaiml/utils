import cv2

root = r"D:\project_data\Sequenceing\raw_video\frontal view.avi"
store = r"D:\project_data\Sequenceing\image\front"

video = cv2.VideoCapture(root)
c=0
while True:
	ret, frame = video.read()
	if ret:
		c+=1
		if c%1==0:
			cv2.imwrite(f"{store}\\front_1_{c}.jpg",frame)
		cv2.imshow("f",frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break
video.release()
cv2.destroyAllWindows()    	    
