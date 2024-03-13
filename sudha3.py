#Eg:3
# ? take values of length and breadth of a
# ? from user and check if it is square or not.
length = int(input())
breadth = int(input())
if length == breadth:
    print("its a square")
else:
    print("its not square")

    
#Eg:4
# python program to check whether the
# given integer is a multiple of both 5 and 7
n = int(input("enter the number: "))
if n%5==0 and n%7==0:
    print("yes")
else:
        print("no")

Eg:5
# write a program to accept the cost price of a bike and display the
# road tax to be paid
#according to the following criteria :

price=int(input("enter the price: "))
total =0
if price>=100000:
    discount  = price*(6/100)
    valu =price-discount
    tax=value+tax
else:
    tax=price*(5/100)
    total=price+tax
print("the onroad cost of bike is:",total)


#----> if elif else
#eg:1
a=7
b=9
c=30

if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("")

