n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
print("First number is ", n1)
print("Second number is ", n2)
print("Third number is ", n3)
if n1 > n2:
    if n1 > n3:
        print(f"First Number ({n1}) is the largest number")
    elif n1 < n3:
        print(f"Third Number ({n3}) is the largest number")
    else:
        print(f"First ({n1}) &Third Number ({n3}) both are the largest number")
elif n1 < n2:
    if n2 > n3:
        print(f"Second Number ({n2}) is the largest number")
    elif n2 < n3:
        print(f"Third Number ({n3}) is the largest number")
    else:
        print(f'Second ({n2}) &Third({n3}) both are the largest number')
else:
    if n1 > n3:
        print(f"First ({n1}) &Second ({n2}) both are the largest number")
    elif n1 < n3:
        print(f"Third Number ({n3}) is the largest number")
    else:
        print(f"First ({n1}), Second ({n2}) &Third Number ({n3}) all are the largest number")

print("End")