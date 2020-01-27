import sys
import os
import glob
import cv2


def convert_yolo_coordinates_to_voc(x_c_n, y_c_n, width_n, height_n, img_width, img_height):
  x_c = float(x_c_n) * img_width
  y_c = float(y_c_n) * img_height
  width = float(width_n) * img_width
  height = float(height_n) * img_height
  half_width = width / 2
  half_height = height / 2
  left = int(x_c - half_width) + 1
  top = int(y_c - half_height) + 1
  right = int(x_c + half_width) + 1
  bottom = int(y_c + half_height) + 1
  return left, top, right, bottom
with open("class_list.txt") as f:
  obj_list = f.readlines()
  obj_list = [x.strip() for x in obj_list]
path_to_folder = '../ground-truth'
os.chdir(path_to_folder)
if not os.path.exists("backup"):
  os.makedirs("backup")
txt_list = glob.glob('*.txt')
if len(txt_list) == 0:
  print("Error: no .txt files found in ground-truth")
  sys.exit()
for tmp_file in txt_list:
  image_name = tmp_file.split(".txt",1)[0]
  for fname in os.listdir('../images'):
    if fname.startswith(image_name):
      img = cv2.imread('../images/' + fname)
      img_height, img_width = img.shape[:2]
      break
  else:
    print("Error: image not found, corresponding to " + tmp_file)
    sys.exit()
  with open(tmp_file) as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  os.rename(tmp_file, "backup/" + tmp_file)
  with open(tmp_file, "a") as new_f:
    for line in content:
      obj_id, x_c_n, y_c_n, width_n, height_n = line.split()
      obj_name = obj_list[int(obj_id)]
      left, top, right, bottom = convert_yolo_coordinates_to_voc(x_c_n, y_c_n, width_n, height_n, img_width, img_height)
      new_f.write(obj_name + " " + str(left) + " " + str(top) + " " + str(right) + " " + str(bottom) + '\n')
print("Conversion completed!")
