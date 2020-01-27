import os
import re
IN_FILE = 'result.txt'
OUTPUT_DIR = os.path.join('..', 'predicted')
SEPARATOR_KEY = 'Enter Image Path:'
IMG_FORMAT = '.jpg'
outfile = None
with open(IN_FILE) as infile:
    for line in infile:
        if SEPARATOR_KEY in line:
            if IMG_FORMAT not in line:
                break
            image_path = re.search(SEPARATOR_KEY + '(.*)' + IMG_FORMAT, line)
            image_name = os.path.basename(image_path.group(1))
            if outfile is not None:
                outfile.close()
            outfile = open(os.path.join(OUTPUT_DIR, image_name + '.txt'), 'w')
        elif outfile is not None:
            class_name, info = line.split(':', 1)
            confidence, bbox = info.split('%', 1)
            bbox = bbox.replace(')','') # remove the character ')'
            left, top, width, height = [int(s) for s in bbox.split() if s.lstrip('-').isdigit()]
            right = left + width
            bottom = top + height
            outfile.write("{} {} {} {} {} {}\n".format(class_name, float(confidence)/100, left, top, right, bottom))
