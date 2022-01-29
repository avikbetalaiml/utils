import json
import cv2
import os

json_file = r"/home/ispeck/Downloads/new2.json"
image_dir = r"/home/ispeck/current_project/zone_data"

with open(json_file, "r") as j:
    data = json.load(j)

for i in data:
    file = data.get(i)
    filename = file.get("filename")
    img = os.path.join(image_dir, filename)
    text = img.replace(".jpg", ".txt")
    regions = file.get("regions")
    if len(regions) >= 1:
        print(filename)
        for region_d in regions:
            shape = region_d.get("shape_attributes")
            x = shape.get("all_points_x")
            y = shape.get("all_points_y")
            # xmin = min(x)
            # xmax = max(x)
            # ymin = min(y)
            # ymax = max(y)
            # coor = f"{xmin} {ymin} {xmax} {ymax}"
            region = region_d.get("region_attributes")
            # for k in region:
            #     if region[k]:
            #         coor = f"{region[k]} {coor}\n"
            with open(text, "a+") as f:
                for i in range(len(x)):
                    f.write(f"({x[i]},{y[i]}),")
    else:
        print(filename, "blank")
