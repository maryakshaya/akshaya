num = int(input("Enter any  number:"))
flag = num %2
if flag==0:
    print(num,"is a even number")
elif flag == 1:
    print(num,"is a odd number")
else:
    print("error,invalid input")
