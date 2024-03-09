class people:
    def employee():
        name = input()
        salary = float(input())
        sales_amount = ((float(input())*15)/100)+salary
        return f'TOTAL = R$ {sales_amount:.2f}'
        
chama = people.employee()
print(chama)