


import sys
import math
import codecs
import string



fil = codecs.open("SinaWeibo_FollowNumber.txt",'r','utf-8')

infm = fil.readline()
infm = fil.readline()

fensitemp = infm[20:len(infm)]
fensitemp = fensitemp.rstrip()
fensitemp = fensitemp.lstrip()	








while (infm != ""):
	date = infm[:10]
	tim = infm[11:19]
	fensitemp = infm[20:len(infm)]
	fensitemp = fensitemp.rstrip()
	fensitemp = fensitemp.lstrip()	
	infm = fil.readline()



fil.close()


