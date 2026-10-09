'''


count=5
while count>0:
    print("Alive")
    count-=1
#to print numbers 1 to n
num=int(input("Enter number : "))
val=1
while val<=num:
    print(val)
    val+=1
#reverse print
while num>0:
    print(num)
    num-=1
'''

#multiplication table
num=int(input("Enter the num : "))
val=1
while val<=10:
    print(f"{num} x {val} = {num*val}" )
    val+=1
