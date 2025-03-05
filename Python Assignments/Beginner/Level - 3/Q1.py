#Q1

def file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    result = []
    for line in lines:
        words = line.split()
        even_words = []
        for word in words:
            if len(word) % 2 == 0:
                even_words.append(word)
        result.append(" ".join(even_words))
    
    return "\n".join(result)

filename = "doc.txt"
print(file(filename))
