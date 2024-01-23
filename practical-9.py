fh=open('output9.txt','w')
n=int(input('enter the number:'))
for i in range(1,11):
    print(n,'*',i,'=',n*i)
    t=n*i
    fh.write(f'{str(n)} * {str(i)} = {str(t)}\n')
fh.close()
   