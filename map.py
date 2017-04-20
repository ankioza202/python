income=[10,20,30,40]

def double_money(dollars):
    return dollars*2


final_money = list(map(double_money,income))
print(final_money)