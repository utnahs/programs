# WAP to find the median of list of numbers
def median(listt):
    length=len(listt)
    temp=0
    for i in range(length-1):
        for j in range(length-1-i):
            if listt[j]>listt[j+1]:
                temp=listt[j]
                listt[j]=listt[j+1]
                listt[j+1]=temp
    print(listt)
    if length%2==1:
        median=int((length)/2)
        return listt[median]
    else:
        median=int(((length/2)+(length/2+1))/2)
        avg=int((listt[median]+listt[median-1])/2)
        return avg
median([10,30,20,40,50,60])
