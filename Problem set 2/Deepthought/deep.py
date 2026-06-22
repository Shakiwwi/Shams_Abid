x = input("What is the answer to the Ultimate Question of Life, The Universe, and Everything? ").strip().lower()
#prompt user for input and convert to lowercase and remove whitespace

if x == "42":
    print("Yes!")
elif x == "forty-two":
    print("Yes!")
elif x == "forty two":
    print("Yes!")
else:
    print("No!")    

#use if loop to check if the answer is correct and print appropriate response