#advance python 

def check_even(n):
    return n%2==0

numbers=[1,2,3,4,5,6,7,8,9,10]
result=filter(check_even,numbers)
print(list(result))