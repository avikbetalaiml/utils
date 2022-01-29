import json
import cv2
import os,glob
json_file = r"C:\Users\bhask\Desktop\annotation\2_2.json" 
image_dir = r"C:\Users\bhask\Desktop\annotation\2"




with open(json_file,"r") as j:
    data = json.load(j)
print(f"####################{json_file}###############################")
for i in data:
    file = data.get(i)
    filename = file.get("filename")
    img = os.path.join(image_dir,filename)
    text = img.replace(".jpg",".txt")
    regions = file.get("regions")
    if len(regions)>=1:
        print(filename)
        for region_d in regions:
            shape = region_d.get("shape_attributes")
            coor = f"{shape.get('x')} {shape.get('y')} {shape.get('width')+shape.get('x')} {shape.get('height')+shape.get('y')}"
            region = region_d.get("region_attributes")
            for k in region:
                if region[k]:
                    coor = f"{region[k]} {coor}\n"
            with open(text,"a+") as f:
                f.write(coor)
    else:
        print(filename,"blank")