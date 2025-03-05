#Q2

def count_lines(filename):
    with open(filename, 'r') as file:
        return len(file.readlines())

filename = "demo.txt"
print("Number of lines:", count_lines(filename))