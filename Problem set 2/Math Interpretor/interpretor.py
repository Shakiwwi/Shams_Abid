#user input to get the expression and split it into components with use of .split()

expression = input("what type of calculation would you like to do?").strip().lower()
x, y, z = expression.split()   
x, z = float(x), float(z)
#convert number into float values for .0 in output


if y == "+": 
    result = x + z

elif y == "-": 
    result = x - z
  
elif y == "*": 
    result = x * z

elif y == "/": 
    result = x / z

else: 
    print("invalid type of calculation")
    exit()

print(f"{result:.1f}")
#outputing to 1 dp as question specifies