def bank(principal, rate, time):
    interest = (principal * rate * time) / 100
    total = principal + interest
    return interest , total

principal = int (input('اصل پول: ')) #اصل پول
rate = int (input('نرخ سود سالانه: ')) #نرخ سود سالانه
time = int (input('مدت زمان سرمایه گذاری: ')) #مدت زمان سرمایه گذاری (به سال)

print(bank(principal, rate, time))