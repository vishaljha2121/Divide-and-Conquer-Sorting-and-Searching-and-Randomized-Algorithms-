
def kara_mul(x,y):
    """
    The Karatsuba Integer Multiplication Algorithm.
    """
    
    # base case
    if len(str(x))==1 or len(str(y))==1:
        return x*y
    else:
        n = max(len(str(x)), len(str(y)))
        n_half = n//2
        
        a = x//(10**n_half)
        b = x % (10**n_half)
        c = y//(10**n_half)
        d = y%(10**n_half)
     
        
        
        ac = kara_mul(a,c)
        bd = kara_mul(b,d)
        ad_plus_bc = kara_mul(a+b, c+d) -ac -bd
        
        product = 10**(2*n_half)*ac +10**(n_half)*(ad_plus_bc) + bd
        return product

if __name__ == '__main__':
        # x, y = int(input()), int(input())
        x = 3141592653589793238462643383279502884197169399375105820974944592
        y = 2718281828459045235360287471352662497757247093699959574966967627
        print(kara_mul(int(x), int(y)))