def staircase(n):
    [print (' '*(n-i)+'#'*i)for i in range(1,n+1)]
    
if __name__ == '__main__':
    n = int(input())

    staircase(n)