#Q8

def count_vowels(string):
    count = 0
    for char in string:
        if char in "aeiouAEIOU":
            count += 1
    return count

string = "Hello, World!"
print("Number of vowels:", count_vowels(string))
