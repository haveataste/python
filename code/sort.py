import random
import datetime

l=10
s=[int(random.random()*100) for i in range(l)]
print(s,"\n")

#冒泡排序
arr=s.copy()
starttime=datetime.datetime.now()
for i in range(l):
    for j in range(l-i-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
endtime=datetime.datetime.now()
print("usedtime:",endtime-starttime,"\n")

#插入排序
arr=[]
starttime=datetime.datetime.now()
arr.append(s[0])
for i in range(1,l):
    for j in range(len(arr)):
        if arr[j]>s[i]:
            arr.insert(j,s[i])
            break
    if j==len(arr)-1:
        arr.append(s[i])
print(arr)
endtime=datetime.datetime.now()
print("usedtime:",endtime-starttime,"\n")

#python列表自带排序函数
starttime=datetime.datetime.now()
print(sorted(s))
endtime=datetime.datetime.now()
print("usedtime:",endtime-starttime,"\n")
            
