#Task 1 Files
with open("myfile.txt", "w") as f:
    f.write("Hello file world!")

with open("myfile.txt") as new_f:
    a = new_f.read()
    print(a)