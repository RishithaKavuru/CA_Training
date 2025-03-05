#Q11

Input = ['Red', 'Blue', 'Black', 'White', 'Pink']
output_list = []

for word in Input:
    char_list = []
    for char in word:
        char_list.append(char)
    output_list.append(char_list)

print("Output:", output_list)
