n = int(input("Enter the number you want to find the power of: "))
power=1
p = int(input("Enter the number you want to find the power BY : "))

for i in range(1,p+1):
    power = power*n
print(n,"to the power of", p, "is:", power)

