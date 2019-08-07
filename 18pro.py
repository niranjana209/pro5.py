sav,sowr=map(int,input().split())
dak=[]
tele=0
for i in range(sav):
    sak.append(list(map(int,input().split())))   
for i in range(sav):
    for j in range(sow-1):
        for k in range(j+1,sow+1):
            if dak[i][j:k]==[1]*len(dak[i][j:k]):
                 if all(dak[p+i][j:k]==[1]*len(dak[p+i][j:k]) for p in range(len(dak[i][j:k])-1)):
                     if len(dak[i][j:k])>tele:
                        tele=len(dak[i][j:k])
if len(dak)==1 and len(dak[0])==1 and dak[0][0]==1:
    print(1)
for i in range(tele):
    print(*[1]*tele)
