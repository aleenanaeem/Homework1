#Aleena Naeem - Assignment 1B

#Part 2A
def calculate (initial_investment, up_value, down_value):
    expected_end_value=(up_value+down_value)/2
    expected_return=((expected_end_value-initial_investment)/(initial_investment))*100 #calculating percentage
    risk=(up_value-down_value)/2
    return (expected_end_value, expected_return, risk)

#input

print("PartA")
initial_investment=float(input('Please enter start value:'))
up_value=float(input('Please enter up value:'))
down_value=float(input('Please enter down value:'))

#output
(expected_end_value, expected_return, risk) = calculate(initial_investment, up_value, down_value)
print('Output:\n')
print('Expected end value: ', expected_end_value)
print('Expected return in % =:', expected_return)
print('Risk equals:',risk)

#Part 2B

print("\nPartb")
#CashFund
d1 = 1000
u1 = 1010
#BondFund
d2 = 970
u2 = 1050
#StockFund
d3 = 950
u3 = 1100

initial_investment = 1000

(expected_value, return1, risk1) = calculate(initial_investment, u1, d1)
(expected_value, return2, risk2) = calculate(initial_investment, u2, d2)
(expected_value, return3, risk3) = calculate(initial_investment, u3, d3)

highest_return = max(return1, return2, return3)
lowest_risk = min(risk1, risk2, risk3)
print("Calculated returns are: CashFund:", return1, ", BondFund:", return2, ", StockFund:", return3)
print("Highest return is: " , highest_return)

print("\nCalculated risks are: CashFund: ", risk1, ", BondFund:", risk2, ", StockFund:", risk3)
print("Lowest risk is: ", lowest_risk)

