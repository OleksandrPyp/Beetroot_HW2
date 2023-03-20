#Task2 The valid phone number program.

phone_num = input("Please enter the phone number: ")
if len(phone_num) == 10 and phone_num.isnumeric():
    print("This is a phone number")
else:
    print("Phone number could only be 10 digits and consist of numbers")