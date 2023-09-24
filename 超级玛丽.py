  #回文字判断

a=input('输入字符串:')

for i in range(0,(len(a)//2)):
    if(a[i] != a[len(a)-1-i]):
        print('No')
        break
else:print('Yes')

