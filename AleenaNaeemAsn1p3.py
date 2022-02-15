#Aleena Naeem - Assignment 1C

#Part3A

def calculate(a,s):
    w=((1/(s-a))-(1/s))*60
    c=(a/(s-a))-(a/s)
    return (w,c)
#Input
a=float(input('Enter average arrival rate of customers per hour:'))
s=float(input('Enter average service rate of ATM per hour:'))

#Process
(w,c) = calculate(a,s)

#output
print('Average wait time per minute per customer is', round(w,2))
print('Average number of customers in line is',round(c))

#Part3B
a= 30
s_old = 45
s_fast= 55
s_faster = 60

#process
(w1,c1)=calculate(a, s_old)
(w2,c2)=calculate(a,s_fast)
(w3,c3)=calculate(a,s_faster)

#output

print('Average wait time per minute per customer at old ATM is', round(w1,2))
print('Average number of customers in line is',round(c1))

print('Average wait time per minute per customer at Fast ATM is', round(w2,2))
print('Average number of customers in line is',round(c2))

print('Average wait time per minute per customer at Faster ATM is', round(w3,2))
print('Average number of customers in line is',round(c3))