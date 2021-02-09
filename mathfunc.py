def per_inc(x,y):
    ''' function which calculates the percentage of increase or decrease of a number '''
    old=y
    new=x
    ret=new-old
    ret1=ret/old*100
	
    if ret1 < 0:
        
        print('decrease ',end='')
        print(ret1,'%')
    else:
        print('increase ',end='')
        

	print(ret1,'%')
def linear_eq(eq):
    first=int(eq[2])
    
    y=int(eq[5])
    for i in range(-2,3):
        print('for ',i,'==',first*i+y)	
