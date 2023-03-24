#Task1 String manipulation

Trial_str = input("Please enter the string: ")
task_str = ""

task_str += (Trial_str[0:2] + Trial_str[-2:])
if len(Trial_str) < 2:
    print("Empty String")
else:
    print(task_str)
