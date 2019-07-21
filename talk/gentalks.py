#!/bin/bash

import csv
import os
def makedir(path): 
    base = os.getcwd()
    try:
        os.mkdir(base+"/"+path)
    except OSError:  
        print ("Creation of the directory %s failed" % path)
    else:  
        print ("Successfully created the directory %s" % path)
with open('talks.csv') as csvfile:
   reader = csv.reader(csvfile)
   first=True
   for row in reader:
        if first:
            first = False
            continue
        path = row[0]
        base = os.getcwd()
        if (os.path.isdir(base+"/"+path)):
            print ("Directory %s already exists" % path)
            continue
        else:
            #print ("Directory %s does not exist" % path)
            makedir(row[0])

        s= \
"""
+++
title = "{3}"
date = {0}
all_day = true
publishDate = {0}
location = "{2}"
event = "{1}"
event_url = ""
abstract = ""
featured = false
tags =  [{4}]
url_slides = ""
projects =  [{5}]
url_pdf = ""
# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
[image]
  # Caption (optional)
  caption = ""

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = ""
+++
""".format(row[0], row[1], row[2], row[3],'"'+'","'.join((row[4].replace(" ", "")).split(","))+'"' , '"'+'","'.join((row[5].replace(' ', '')).split(","))+'"' )
        with open(row[0]+"/index.md", "w") as f:
            f.write(s)
