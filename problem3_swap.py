from collections import Counter
S="xxyyxyxyxxyx"
T="xyyxyxxxyxxy"

def solution(S,T):
    list=[]
    if(len(S)!=len(T)):
        return -1
    for i,j in zip(S,T):
        if(i!=j):
            list.append(i)
    count_dict=dict(Counter(list))
    no_of_swaps=0
    total_mismatch=0
    for item in count_dict.keys():
        total_mismatch=total_mismatch + count_dict.get(item)
    if(total_mismatch%2!=0):
        return -1
    for item,count_val in count_dict.items():
        no_of_swaps=no_of_swaps + int(count_val/2) + count_val%2
    return int(no_of_swaps)

return_value=solution(S,T)
print(return_value)
