


a = open('2049短篇.txt','r',encoding='utf8')

b = open('2049长篇.txt','r',encoding='utf8')

aa = a.readlines()
for each in range(len(aa)):
    aa[each] = aa[each].split('\t')[2]


bb = b.readlines()
for each in range(len(bb)):
    bb[each] = bb[each].split('\t')[2]


for eachb in bb:
    for eacha in aa:
        if eacha ==eachb:
            print(eachb)

print('over')
a.close()
b.close()
