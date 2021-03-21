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
---
title: {3}

event: {1}
event_url: ""
draft: false
location: {2}
#address:
#  street: 450 Serra Mall
#  city: Stanford
#  region: CA
#  postcode: '94305'
#  country: United States

summary: ""
abstract: ""

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: "{0}"
#date_end: "{0}"
all_day: true

# Schedule page publish date (NOT talk date).
publishDate: {0}"

authors: []
tags: [{4}]

# Is this a featured talk? (true/false)
featured: false

image:
  caption: 'Image credit'
  focal_point: Right

#links:
#- icon: twitter
#  icon_pack: fab
#  name: Follow
#  url: https://twitter.com/georgecushen
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: [{5}]
---
""".format(row[0], row[1], row[2], row[3],'"'+'","'.join((row[4].replace(" ", "")).split(","))+'"' , '"'+'","'.join((row[5].replace(' ', '')).split(","))+'"' )
        with open(row[0]+"/index.md", "w") as f:
            f.write(s)
