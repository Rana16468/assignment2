time = int(input("Enter the time (0-23): "))

if 5 <= time < 12:
    print("Good Morning")
elif 12 <= time < 17:
    print("Good Afternoon")
elif 17 <= time < 21:
    print("Good Evening")
elif (21 <= time <= 23) or (0 <= time < 5):
    print("Good Night")
else:
    print("Invalid input! Please enter a time between 0 and 23.")
