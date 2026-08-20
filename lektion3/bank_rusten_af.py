
############
# ØVELSE 2 #
############

mylist = [1,5,4,3,2,2,8,1,5]
x=len(mylist) 

for i in mylist:
    if i==2:
        x-=i
    else:
        x+=i

x=x/2


print(x)



############
# ØVELSE 2 #
############

yourlist = [1,5,3,2,3,2,8,1,5]

x=yourlist[-1]
i=0

while yourlist[i] != 2:
    x+=yourlist[i]
    i+=1

x+=i
print(x)