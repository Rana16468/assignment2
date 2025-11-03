# problem 7
palindrome=str(input("Enter The Palindrome String: "))
checked=palindrome[::-1]
if checked and len(checked)==len(palindrome) and  checked==palindrome:
  print("this string is palindrome")
else:
  print("is not palindrome string")