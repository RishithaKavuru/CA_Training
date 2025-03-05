#Q9

def encoding(s):
    encoded_str = ""
    count = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            encoded_str += s[i] + str(count)
            count = 1
    encoded_str += s[-1] + str(count)
    return encoded_str

input_string = "wwwwaaadebbbbbw"
print("Output:", encoding(input_string))
