def per_inc(x,y):
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
