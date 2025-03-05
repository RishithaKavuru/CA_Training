#Q2
s = input()
letters = 0
digits = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digits += 1
    
print(f"Alphabets:{letters} & Number:{digits}")