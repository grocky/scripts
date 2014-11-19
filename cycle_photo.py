#!/usr/bin/env python

import time
import os
import shutil
from glob import glob

photoDir = "C:/Users/tov619/Pictures/terminal_photos"
print "Starting..."
os.chdir(photoDir)

if os.path.isfile("cur.jpg"):
    os.remove("cur.jpg")

images = glob("*.jpg")

num_images = len(images)

i = 1
while True:
    if i > num_images:
        i = 1
    print str(i) + ".jpg"
    shutil.copy2(str(i) + ".jpg", "cur.jpg")
    i = i + 1
    time.sleep(4)
