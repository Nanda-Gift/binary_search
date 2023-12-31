import random
import time

def native_search(l,target):
    for i in range(len(l)):
        if l[i]==target:
            return i
    return -1


def binary_serach(l,target,low=None,high=None ):
    if low is None:
        low =  0
    if high is None:
        high = len(l) - 1
    if high<low:
        return -1

    midpoint=((low + high)//2)

    if l[midpoint]==target:
        return midpoint
    elif target < l[midpoint]:
        return binary_serach(l,target,low,midpoint-1)
    else:
        return binary_serach(l,target,midpoint+1,high)
    
if __name__ == "__main__":
    length=1000
    # l =[1,3,5,10,12]

    # target=10

    # print(native_search(l,target))
    # print(binary_serach(l,target))
    sorted_list =set()
    while len(sorted_list)< length:
        sorted_list.add(random.randint(-3*length,3*length))
    sorted_list=sorted(list(sorted_list))
    start= time.time()
    for target in sorted_list:
        native_search(sorted_list,target)
    end=time.time()
    print("native search time: ",(end-start)/length, "seconds")

    for target in sorted_list:
        binary_serach(sorted_list,target)
    end=time.time()
    print("binary search time: ",(end-start)/length, "seconds")
