# Manual item list
item=['26 december 2016','bread',5]
#print(item[0])

#unpacked list

date,name,price=['26 december 2016','bread',5]
#print(name)

# count average of middle number in the list where middle

def avg_middle_grades(grades):
    first,*middle,last=grades
    avg=sum(middle)/len(middle)
    print(avg)

avg_middle_grades([30,10,10,20,10,10,40])
