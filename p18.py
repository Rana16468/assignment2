import cmath
a=float(input("Enter coefficient a : "))
b=float(input("Enter coefficient b: "))
c=float(input("Enter coefficient c: "))
root1= -b+ cmath.sqrt((b*b)-4*a*c).real/2*a
root2=-b - cmath.sqrt((b*b)-4*a*c).real/2*a
print(root1)
print(root2)