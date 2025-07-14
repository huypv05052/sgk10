#

def prime(n):
    if n<2:
        return False
    c=0
    k=2
    while k<n:
        if n%k==0:
            return False
        k+=1
    return True
