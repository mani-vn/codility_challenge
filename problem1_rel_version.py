rel_1="1.0.1"
rel_2="1"

def solution(string1,string2):
    s1=string1.split(".")
    s2=string2.split(".")
    if(len(s1)>len(s2)):
        length_diff=len(s1)-len(s2)
        for x in range(0,length_diff):
            s2.append("0")
    elif(len(s2)>len(s1)):
        length_diff=len(s2)-len(s1)
        for x in range(0,length_diff):
            s1.append("0")

    s=zip(s1,s2)
    for i,j in s:
        if(i!="0"):
            i=i.strip("0")
        if(j!="0"):
            j=j.strip("0")
        if(i>j):
            return 1
        elif(i<j):
            return -1
    return 0

return_value=solution(rel_1,rel_2)
print(return_value)