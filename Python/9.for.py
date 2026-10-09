string="Maximus is here"
#to print all characters
for var in string:
    print(var)
#to check if char exists or not
if 'm' in string:
    print("m Exists in string")
#to check occurence of particular char
count=0
for ch in string:
    if ch=='s':
        count+=1

print(count)