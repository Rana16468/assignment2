#problem 10
a = "100"
b = "25"
c = "10.5"

def main_program(a, b, c):
    try:
       if  type(a).__name__=="str" and type(b).__name__=="str" and type(c).__name__=="str":
        firstresult=int(a) + int(b)
        if type(firstresult).__name__=="int":
           converfloat=float(c)
        if type(firstresult).__name__=="int" and type(converfloat).__name__=="float":
          return str(firstresult-converfloat)



        return ""
    except Exception as e:
        print(e)

print("type: " + type(main_program(a, b, c)).__name__ + " "+"output: "+ main_program(a, b, c))

