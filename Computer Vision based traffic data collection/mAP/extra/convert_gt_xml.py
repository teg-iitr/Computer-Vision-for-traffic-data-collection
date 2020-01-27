import sys
import os
import glob
import xml.etree.ElementTree as ET

path_to_folder = '../ground-truth'
os.chdir(path_to_folder)
if not os.path.exists("backup"):
  os.makedirs("backup")
xml_list = glob.glob('*.xml')
if len(xml_list) == 0:
  print("Error: no .xml files found in ground-truth")
  sys.exit()
for tmp_file in xml_list:
  with open(tmp_file.replace(".xml", ".txt"), "a") as new_f:
    root = ET.parse(tmp_file).getroot()
    for obj in root.findall('object'):
      obj_name = obj.find('name').text
      bndbox = obj.find('bndbox')
      left = bndbox.find('xmin').text
      top = bndbox.find('ymin').text
      right = bndbox.find('xmax').text
      bottom = bndbox.find('ymax').text
      new_f.write(obj_name + " " + left + " " + top + " " + right + " " + bottom + '\n')
  os.rename(tmp_file, "backup/" + tmp_file)
print("Conversion completed!")
