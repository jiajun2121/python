#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: jiajun

import os
import json
import threading




with open('save.json','r',encoding='utf-8') as f:
	hosts = json.loads(f.read())
h = ''.join(str(str(s)+'\n') for s in hosts)

print(h)











for h in hosts:
	if "#"  in h:
		pass
	else:
		pass


