name = input("camelCase: ")
 
snake = ""
for char in name:
    if char.isupper():
        snake += "_" + char.lower()
    else:
        snake += char
 
print("snake_case:", snake)