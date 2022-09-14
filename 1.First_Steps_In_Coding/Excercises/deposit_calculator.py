deposit_amount = float(input())
deposit_deadline = int(input())
yearly_interest = float(input())

interest = deposit_amount * (yearly_interest / 100)
monthly_interest = interest / 12
total = deposit_amount + (deposit_deadline * monthly_interest)

print(total)