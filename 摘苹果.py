a=list(input().split())
b=int(input())
n=0
for i in a:
	if(int(i)-30<=b):
		n+=1

print(n)