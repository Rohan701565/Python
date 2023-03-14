# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n

def cms(ichs):
    return (ichs * 2.54)

ichs = 10
f = cms(ichs)
print(str(ichs) + " Inches is " + str(f)+ " cms ")
