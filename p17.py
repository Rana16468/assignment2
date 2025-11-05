a=int(input("Enter The Fist Number : "))
b=int(input("Enter The Second Number: "))
c=int(input("Enter The Third Number:"))
if a+b>c and b+c >a and c+a>b:
  if a==b==c:
    print("his is an Equilateral Triangle")
  elif  a==b or b==c or c==a:
    print("This is an Isosceles Triangle.")
  else:
    print("This is a Scalene Triangle.")
else:
   print("The given sides do not form a valid triangle.")