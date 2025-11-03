def data_type_checker(value):
   return type(value).__name__

print("data type checker: ",data_type_checker(10))
print("data type checker: ",data_type_checker(10.5))
print("data type checker: ",data_type_checker("daffodil International University Bangladesh"))
print("data type checker: ",data_type_checker(10.585))
print("data type checker: ",data_type_checker(True))