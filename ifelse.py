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