#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zipfile

z = zipfile.ZipFile("11.zip", "r")
for filename in z.namelist():
        print filename
        bytes = z.read(filename)
        print len(bytes)