


""" compound interest formula is amount = p(1+r/100)**t
ci = amount - P
"""


p = float(input("Enter the principal Amount: "))
r = float(input("Enter the interest rate: "))
t = float(input("Enter the time period: "))

amount = p*(1+r/100)**t
ci = amount-p

print(round(amount,2))

print("Compound Interest:",ci)
