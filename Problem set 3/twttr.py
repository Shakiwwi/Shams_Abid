text = input("Input: ")
print("Output:", "".join(c for c in text if c not in "aeiouAEIOU"))