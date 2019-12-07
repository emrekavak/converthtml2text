# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import glob
import errno
import html2text
path="C:/Users/emrek/.spyder-py3/CT/*.html"
files=glob.glob(path)

for name in files:
    try:
        with open(name, encoding="utf-8") as f:
            base=os.path.splitext(name)[0]
            with open (name,encoding="utf-8") as fp:
                line=fp.readline()
                while line:
                    with open(base+"txt", 'a', encoding="utf-8") as the_file:
                        line=line.replace("&uuml;","ü")
                        line=html2text.html2text(line)
                        line=line.replace("**","")
                        the_file.write(line)
                        line=fp.readline()
    except IOError as exc:
        if exc.errno!=errno.EISDIR:
            raise