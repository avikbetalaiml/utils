import os
import glob
import cv2
import numpy as np
from tqdm import tqdm

'''
Raw annotation in format [ClassName Xmin Ymin Xmax Ymax]
Keep all the raw annotation images,texts and classes.txt in a particular folder and pass the location in root
Make another folder where all the images and YOLO format annotations will be stored and pass the location in store  
'''
change = {
    "spanner_17mm" :            "spanner_17",
    "hand_wheel": "handwheel",
    "gland_flange": "glandflange",
    "gland_packing": "gland_packing_extractor"
}

def convert(image, coords):
    coords[2] -= coords[0]
    coords[3] -= coords[1]
    x_diff = int(coords[2] / 2)
    y_diff = int(coords[3] / 2)
    coords[0] = coords[0] + x_diff
    coords[1] = coords[1] + y_diff
    coords[0] /= int(image.shape[1])
    coords[1] /= int(image.shape[0])
    coords[2] /= int(image.shape[1])
    coords[3] /= int(image.shape[0])
    return coords


root =  r"C:\Users\bhask\Desktop\annotation\select"
store = r"C:\Users\bhask\Desktop\annotation\yolo"
classes = {}
with open(os.path.join(root, "classes.txt"), "r") as myFile:
    for num, line in enumerate(myFile, 0):
        line = line.rstrip("\n")
        classes[line] = num
    myFile.close()
print(classes)

img_paths = [str(img_path) for img_path in glob.glob(os.path.join(root, '*.jpg'))]

for img in tqdm(img_paths):
    txt = img.replace(".jpg", ".txt")
    with open("img_list.txt","a+") as f:
        f.write(f"{img}\n")
    image = cv2.imread(img)
    annotation = list()
    try:
        with open(txt, "r") as file:
            for line in file:
                labels = line.split()
                labels[0] = change.get(labels[0],labels[0])
                ####################################################################################
                ck = labels[0]
                none_checker = classes.get(labels[0])
                ####################################################################################
                labels[0] = classes.get(labels[0])
                if none_checker == None:
                    with open("error.txt","a+") as f:
                        f.write(f"{ck}  {img}\n")

                coords = [float(i) for i in labels[1:]]
                labels[1:] = convert(image, np.asarray(coords))
                labels = [str(value) for value in labels]
                annotation.append(" ".join(labels))
            file.close()

    except FileNotFoundError as fnf_error:
        print(fnf_error)
        pass
    cv2.imwrite(img.replace(root, store), image)
    with open(txt.replace(root, store), "a+") as outfile:
        for line in annotation:
            outfile.write(line)
            outfile.write("\n")
        outfile.close()
