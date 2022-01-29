import os
import glob
import shutil

root = r"C:\Users\bhask\Desktop\annotation\2"
store = r"C:\Users\bhask\Desktop\annotation\select"
text_paths=[str(img_path) for img_path in glob.glob(os.path.join(root, '*.txt'))]

for txt in text_paths:
    img = txt.replace(".txt",".jpg")
    try:
        shutil.move(img,img.replace(root,store))
        shutil.move(txt,txt.replace(root,store))
    except:
    	print(txt)
        