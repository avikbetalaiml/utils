import cv2
import glob, os
import shutil

root ="/home/ispeck/Downloads/sub_sequence/select"
store = "/home/ispeck/Downloads/sub_sequence/nut"

txt_files = [str(img_path) for img_path in glob.glob(os.path.join(root, '*.txt'))]

for txt in txt_files:
	img = txt.replace('.txt','.jpg')
	t = []
	with open(txt,'r') as f:
		for line in f:
			if "nut_sequence" in line:
				print(line)
				t.append(1)
	if sum(t) >= 1:
		shutil.move(img,img.replace(root,store))

