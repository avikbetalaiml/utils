import os, glob

root = r"/home/ispeck/current_project/ITE/Cam2/cam2_text"

text_path = os.listdir(root)
path = "datasets/cam2/train/new_set/images/"

for txt in text_path:
	img = txt.replace("txt","jpg")
	with open("img_path.txt","a+") as f:
		f.write(f"{path}{img}\n")