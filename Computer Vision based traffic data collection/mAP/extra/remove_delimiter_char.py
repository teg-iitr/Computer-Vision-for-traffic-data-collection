import glob
import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--char', required=True, type=str, help='specific character to be removed (e.g. ";").')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-g', '--ground-truth', help="if to remove that char from the ground-truth files.", action="store_true")
group.add_argument('-p', '--predicted', help="if to remove that char from the predicted objects files.", action="store_true")
args = parser.parse_args()

def file_lines_to_list(path):
  with open(path) as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  return content
if len(args.char) != 1:
  print("Error: Please select a single char to be removed.")
  sys.exit(0)
if args.predicted:
  os.chdir("../predicted/")
else:
  os.chdir("../ground-truth/")
backup_path = "backup"
if not os.path.exists(backup_path):
  os.makedirs(backup_path)
files_list = glob.glob('*.txt')
files_list.sort()
for txt_file in files_list:
  lines = file_lines_to_list(txt_file)
  is_char_present = any(args.char in line for line in lines)
  if is_char_present:
    os.rename(txt_file, backup_path + "/" + txt_file)
    # create new file
    with open(txt_file, "a") as new_f:
      for line in lines:
        #print(line)
        if args.predicted:
          class_name, confidence, left, top, right, bottom = line.split(args.char)
          # remove any white space if existent in the class name
          class_name = class_name.replace(" ", "")
          new_f.write(class_name + " " + confidence + " " + left + " " + top + " " + right + " " + bottom + '\n')
        else:
          # ground-truth has no "confidence"
          class_name, left, top, right, bottom = line.split(args.char)
          # remove any white space if existent in the class name
          class_name = class_name.replace(" ", "")
          new_f.write(class_name  + " " + left + " " + top + " " + right + " " + bottom + '\n')
print("Conversion completed!")
