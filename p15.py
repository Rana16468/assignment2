ch = input("Enter a single alphabet: ")
# print(ch.lower() in ["a", "e", "i", "o", "u"])
if len(ch) == 1 and ch.isalpha():
    if ch.lower() in ["a", "e", "i", "o", "u"]:
        print(f"{ch} is a vowel.")
    else:
        print(f"{ch} is a consonant.")
else:
    print("Only a single alphabet character is accepted.")
