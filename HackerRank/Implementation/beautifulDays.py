def beautifulDays(i, j, k):
    result = sum(1 if (a-int(str(a)[::-1]))%k==0 else 0 for a in range(i,j+1) )    
    return result
