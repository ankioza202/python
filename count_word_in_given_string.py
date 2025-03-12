# From given string, find number of occurrence of 'Awesome'
s1 = "XYZ is awesome, work environment is awesome"
s2= s1.split(" ")
count = 0
for s in s2:
    final_string = s.replace(",","").lower()
    if final_string == 'awesome':
        count+=1
print(count)
