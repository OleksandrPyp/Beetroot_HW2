#Task 3 List Comprehension exercise
import random
var_i = random.randint(1,10)

result_list = [(i,i**2) for i in range(var_i)]
print(result_list)

