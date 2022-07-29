k=[]#创建一个列表存放质因数
def su(n):#判断素数的函数
	for i in range(2,n):
		if (n%i==0):
			return 0
		else:
			continue
	return 1
def fen(n):#将数分开
	for j in range(n):#控制循环次数
		for i in range (2,n):#进行内层循环找出n的因数
			if n%i==0:
				if su(i):
					k.append(i);n=n//i
					if su(n):#判断此时的n是否为素数
						k.append(n)
					break
n=int(input())
fen(n)
s=len(k)
print(n,'=',k[0],end='')
for i in range(1,s):
	print('*%d'%k[i],end='')
