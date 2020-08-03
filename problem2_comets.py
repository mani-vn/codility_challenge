comets=[-2,-1,1,2]

def solution(comets):
    list=[]
    flag=False
    length=len(comets)
    counter=0
    for x in range(0,length):
        if(flag):
            flag=False
            continue
        if(x==length-1):
            if(comets[x]<0 and comets[x-1]<0):
                list.append(comets[x])
            elif(comets[x]>0):
                list.append(comets[x])
            break
        if(comets[x]>0 and comets[x+1]<0):
            counter=counter+1
            if(comets[x]>abs(comets[x+1])):
                list.append(comets[x])
                flag=True
            elif(comets[x]==abs(comets[x+1])):
                flag=True
        else:
            list.append(comets[x])
    if(counter>0):
        list=solution(list)
    return list

return_value=solution(comets)
print(return_value)





