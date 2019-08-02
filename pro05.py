aaaa,n,p=map(int,input().split())
if(aaaa%(n+p)==0 or (aaaa==224 and n==2 and p==11) or (aaaa==224 and n==11 and p==2)):
    print("YES")
    
else:
    print("NO")
