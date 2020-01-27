import sys
import os
import glob
import json
path_to_folder = '../predicted'
os.chdir(path_to_folder)
if not os.path.exists("backup"):
  os.makedirs("backup")
json_list = glob.glob('*.json')
if len(json_list) == 0:
  print("Error: no .json files found in predicted")
  sys.exit()
for tmp_file in json_list:
  with open(tmp_file.replace(".json", ".txt"), "a") as new_f:
    data = json.load(open(tmp_file))
    for obj in data:
      obj_name = obj['label']
      conf = obj['confidence']
      left = obj['topleft']['x']
      top = obj['topleft']['y']
      right = obj['bottomright']['x']
      bottom = obj['bottomright']['y']
      new_f.write(obj_name + " " + str(conf) + " " + str(left) + " " + str(top) + " " + str(right) + " " + str(bottom) + '\n')
  os.rename(tmp_file, "backup/" + tmp_file)
print("Conversion completed!")
