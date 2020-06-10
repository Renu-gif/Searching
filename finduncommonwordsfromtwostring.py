def uncommon(s1,s2):
    a=s1.split()
    b=s2.split()
    print(a)
    print(b)
    result=[]
    count=0
    for i in a:
        if i not in b:
            count+=1
            result.append(i)
    for i in b:
        count=0
        if i not in a:
            count+=1
            result.append(i)
    return " ".join(result)

s1="Geeks for Geeks"

print(s1)
s2="Learning from Geeks for Geeks"
print(uncommon(s1,s2))