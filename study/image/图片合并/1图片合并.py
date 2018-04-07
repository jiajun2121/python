#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-01 19:12:52
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from PIL import Image

im_file = [
    '微信图片_20180301192856.jpg',
    '微信图片_20180301192859.jpg',
    '微信图片_20180301192902.jpg',
    '微信图片_20180301192905.jpg',
    '微信图片_20180301192907.jpg',
    '微信图片_20180301192910.jpg',
    '微信图片_20180301192914.jpg',
    '微信图片_20180301192917.jpg',
    '微信图片_20180301192920.jpg',
    '微信图片_20180301192923.jpg',
    '微信图片_20180301192932.jpg',
    '微信图片_20180301192935.jpg',
    '微信图片_20180301192941.jpg']
for file in im_file:
    with Image.open(im_file[0]).crop((118, 90, 2040, 1050)) as i:
        width, height = i.size

im = Image.new("RGB", (width, height * 13))
local = 0
for file in im_file:
    with Image.open(file).crop((118, 90, 2040, 1050)) as i:
        n = i
        width, height = i.size
        im.paste(i, (0, local, width, local + height))
        local += height
        print(n)
# im.show()

im.show()
im.save('hebing.jpg')
