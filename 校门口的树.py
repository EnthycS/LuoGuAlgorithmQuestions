r=list(input().split())
l=int(r[0])
m=int(r[1])
a=[1]*(l+1)
n=0
for i in range(m):
	s=list(input().split())
	left=int(s[0])
	right=int(s[1])
	for j in range(left,right+1):
		if(a[j] != 0):
			a[j]=0
			n+=1


print(l-n+1)

