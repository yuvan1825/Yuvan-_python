print("area of triangle")
l=int(input("enter the l value:"))
b=int(input("enter the b value:"))
c=(0.5*l*b)
print(c)

print("area of rectangle")
l=int(input("enter the l value:"))
b=int(input("enter the b value:"))
c=(l*b)
print(c)

print("perimeter of circle")
r=int(input("enter the radius:"))
area=(2*3.14*r)
print("area of the circle:",area)

a=int(input("enter the password:"))
if a==1234:
    print("Correct password.")
else:
 print("Wrong password.")
 for a in range(1,6,1):
    a=int(input("enter the password:"))
    if a==1234:
     print("Correct password.") 
    else:
      print("Wrong Password.") 
 else:
    print("Wait for 30 second.")

for i in range (10,1):
  print(i)

  a=int(input("Enter a number:"))
  i=1
  while(i<11):
    print(a,"x",i,"=",a*i)
    i=i+1

    for i in range (1,5,1):
     for j in range(1,5,1):
        print(i*j,end=" ")
    print() 
    
for i in range (1,6,1)	:
    for j in range(0,i,1):
        print(i*j,end=" ")
    print()          

b=1
while(b<11):
    print(11,"*",b,"=",11*b)
    b=b+1


for s in range(1,9,1):
    print(s,"^","2=",2**s)

a=0   
for i in range(1,11,1):
    a=a+i
print(a)
 
a=5
for i in range(1,50,1):
    a=a^i
    print(a)
    
    print(a)
    print("hello")
