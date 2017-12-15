flag = 1
sn = 0
for i in range(1,100,2):
    print(i*flag,end=',')
    sn += i * flag
    i += 2
    flag = flag * -1 
print(sn)