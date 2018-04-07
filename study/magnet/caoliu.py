#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-08 00:00:08
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import sys
sys.path.append(os.getcwd())
import magnet
from bs4 import BeautifulSoup 
import requests







html = requests.get('http://liuyoub.ml/htm_data/2/1712/2828585.html')
# get link
soup = BeautifulSoup(html.content, 'html5lib')














f = magnet.FileWithMagnet('title')
print(f)

