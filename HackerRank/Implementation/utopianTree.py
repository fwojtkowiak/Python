
def utopianTree(n):
    H=1
    for i in range(n):
        if(i%2==0):
            H=H*2
        else:
            H+=1
    return(H)
    
def utopianTree(n):
    if(n%2==0):
        H=2**(n/2-1)*2+1
        
    else:
        H=(2**(n/2+1)-1)*2
        
    return H