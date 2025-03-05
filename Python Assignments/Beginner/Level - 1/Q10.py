#Q10

def reverse_sentence(input_sentence):
    return ' '.join(input_sentence.split()[::-1])

input_sentence = "Hello, World! Welcome to Python programming."
output_sentence = reverse_sentence(input_sentence)

print("Output after reverse:", output_sentence)
