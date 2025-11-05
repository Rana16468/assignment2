grades=int(input("Enter The Grades : "))
if grades>=90:
  print("Got A+")
elif grades>=80 and grades<=89:
  print("Got A")
elif grades>=70 and grades<=79:
  print("Got B")
elif grades>=60 and grades<=69:
  print("Got C")
elif grades<60:
  print("Fail")