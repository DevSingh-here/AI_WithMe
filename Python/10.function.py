'''
def avg(a,b,c):
    sum=a+b+c
    return (sum/3)
a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))
print(avg(a,b,c))
'''
num=int(input("Enter number : "))
def fact(num,res=1):
    if num==1:
        return res
    else:
        return num*fact(num-1)
print(fact(num))