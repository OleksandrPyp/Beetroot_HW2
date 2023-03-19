#Task 4 days of week dictionary
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days_num = [1, 2, 3, 4, 5, 6, 7]
dict_result = dict(zip(week_days,days_num))
print(dict_result)

#dict_1 = {}
#for day in week_days:
   # dict_1[day] = 1

#print(dict_1)

reversed_dict = {v:k for k,v in dict_result.items()}
print(reversed_dict)