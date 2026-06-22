def main():
    plate = input("Plate: ")
    print("Valid" if is_valid(plate) else "Invalid")
 
 
def is_valid(s):
    return (has_valid_length(s) and starts_with_two_letters(s) and no_punctuation(s) and numbers_at_end(s))
 
 
def has_valid_length(s):
    return 2 <= len(s) <= 6
 
 
def starts_with_two_letters(s):
    return len(s) >= 2 and s[0].isalpha() and s[1].isalpha()
 
 
def no_punctuation(s):
    return all(c.isalpha() or c.isdigit() for c in s)
 
 
def numbers_at_end(s):
    
    first_digit = None
    for i, c in enumerate(s):
        if c.isdigit():
            if first_digit is None:
                if c == "0":
                    return False
                first_digit = i
        elif first_digit is not None:
            
            return False
    return True
 
 
main()