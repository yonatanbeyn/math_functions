def per_inc(x,y):
    ''' function which calculates the percentage of increase or decrease of a number '''
    old=y #old value
    new=x   #new value
    ret=new-old #return
    ret1=ret/old*100  # the percentage return value
	
    if ret1 < 0:
        
        print('decrease ',end='')
        print(ret1,'%')
    else:
        print('increase ',end='')
        

	print({ret1:0.2f},'%')#only prints 2 digit floating point
	
	
### another function#######

def linear_eq(eq):
	''' function which evaluates linear equation and prints x to y values '''
    first=int(eq[2])
    
    y=int(eq[5])
    for i in range(-2,3):
		print('for ',i,'==',first*i+y)	
###example
"""linear_eq('y=2x+3')
for  -2 == -1
for  -1 == 1
for  0 == 3
for  1 == 5
for  2 == 7"""
