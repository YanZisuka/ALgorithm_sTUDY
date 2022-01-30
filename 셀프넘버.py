#4673 셀프넘버
num_list=[]
for i in range (1,100):
    i+= sum(map(int,list(str(i))))
    num_list.append(i)

for i in range(1,100):
    if i not in num_list:
        print(i)
