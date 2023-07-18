list_a=list(map(int,input().split()))  
result=0
for i in list_a:
    result=result^i
print(result)
