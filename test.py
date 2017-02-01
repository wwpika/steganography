# -*- coding:utf-8 -*-
#map()示范
def add100(x):
	return x+100
h=[11,22,33]
a=map(add100,h)
print (list(a))

#map()示范2 如果给出了额外的可迭代参数，则对每个可迭代参数中的元素‘并行’的应用‘function’
def abc(a,b,c):
	return a*100+b*10+c
list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]
b=map(abc,list1,list2,list3)
print(list(b))

#join():将序列中的元素以指定的字符连接，生成一个新的字符串
seq=("a","b","c")
print(' - '.join(seq))

#enumerate()示范
seq=["one","two","three"]
for i,element in enumerate(seq):
	seq[i]='%d:%s'%(i,seq[i])
print(list(seq))

seq=["one","two","three"]
print(['%d:%s' %(i,element) for i,element in enumerate(seq)])

#移位运算
r=9
#右移1位相当于除以2，左移一位相当于乘以2
print(r>>1)
print(r<<1)

#bytearray()示范:将字符串转换为整数值序列0--255，数值序列由字符串的字节数据转换而来
data=bytearray('你好世界','utf-8')
print(len(data),data)
for i in data:
	print(i,type(i))




