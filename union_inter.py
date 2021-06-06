#User function Template for python3

def doUnion(a,n,b,m):
    
    #code here
    a = set(a)
    b = set(b)
    count = 0
    result_set = a.union(b)
    for item in result_set:
        count = count + 1
    return count



#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        
        
        print(doUnion(a,n,b,m))
# } Driver Code Ends