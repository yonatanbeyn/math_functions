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
