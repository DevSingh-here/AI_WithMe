
n = int(input("Enter length of the array: "))
arr = []

for i in range(n):
    arr.append(int(input("Enter the elements: ")))

largest = float('-inf')
second_largest = float('-inf')

for x in arr:
    if x > largest:
        second_largest = largest
        largest = x
    elif x > second_largest and x < largest:
        second_largest = x

if second_largest == float('-inf'):
    print("No second largest distinct element")
else:
    print(second_largest)
