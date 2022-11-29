digit = int(input("Enter a number for generating multiplication table: "))
limit = int(input("Enter the limit: "))
for x in range(1,limit+1):
    print(digit," * ", x ," = ",(digit*x))
