# WAP to find the square root of a given number using babylonian method
def sqrt(num):
    temp=num/2
    for i in range(8):
        temp = (temp+(num/temp))/2
    return temp         
sqrt(15)
