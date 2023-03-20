#task3 Words combination 1st try

input_string = input("Please input any word ")
print(''.join(random.sample(input_string,len(input_string))))

#task3 2nd attempt

another_input_str = input("Please input any word:  ")
for i in range(0, len(another_input_str)):
    print("".join(random.sample(another_input_str,len(another_input_str))))