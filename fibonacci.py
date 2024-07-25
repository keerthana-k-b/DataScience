num=int(input("enter the limit:"))
a = 0
b = 1
print("Fibonacci Series: ")
for i in range(0,num):
    print(a,end = " ")
    c = a+b
    a = b
    b = c