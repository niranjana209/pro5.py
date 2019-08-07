akk,say=map(int,input().split())
bake=[]
jim=[]
wave=[int(m) for m in input().split() ]
for i in range(0,say):
    uu,vv=map(int,input().split())
    for j in range(uu-1 ,vv):
        jim.append(wave[j])
    adh=sorted(jim)
    bake.append(min(jim))
    del jim[:]
for z in range(0,len(bake)):
    print(bake[z])
