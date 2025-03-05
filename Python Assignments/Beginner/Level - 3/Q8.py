#Q8

def encoded_string(string):
    values = string.split("0")
    final_values = []
    for value in values:
        if value:
            final_values.append(value)
    return {"first_name": final_values[0], "last_name": final_values[1], "id": final_values[2]}

string = "Robert000Smith000123"
Output = encoded_string(string)
print("Output:", Output)
