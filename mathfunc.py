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
#quadratic equation function
'''
Quadratic equation root calculator
'''
def roots(a, b, c):
	D = (b*b - 4*a*c)**0.5
	x_1 = (-b + D)/(2*a)
        x_2 = (-b - D)/(2*a)
        print('x1: {0}'.format(x_1))
        print('x2: {0}'.format(x_2))
if __name__ == '__main__':     #save in a file and run
    a = input('Enter a: ')
    b = input('Enter b: ')
    c = input('Enter c: ')
    roots(float(a), float(b), float(c))

# is prime number function
def is_prime(n):
	for i in range(2,n):
		if not (n%i):
			return False
		return True
for n in range(1,20):
	if is_prime(n):
		print(n)
		
# function which checks if a number is a factor of another number		
def is_factor(a, b):
	if b % a == 0:
		return True
        else:
		 return	False	
		
