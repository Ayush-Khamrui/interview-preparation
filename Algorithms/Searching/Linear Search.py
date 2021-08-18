print("Enter the list of the number")
mylist=list(map(int,input().split()))
num=int(input("Enter the number for searching\n"))
for i in mylist:
    if i==num:
        print("Value is in the list")
        break
else:
    print("Value is not in your list")
