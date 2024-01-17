import jwt

SECRET_KEY = "470c934124ce848f0ead05b52ffab0c502fb918c3623af321b74a60312fa4f77"

print("\n - Starting -")

# Setting the text
text = "CitricSheep"
print("\nText:", text)

# Building the list, each element is the ascii representation of the char
ascii_list = [ord(char) for char in text]
print("\nASCII list:", ascii_list)

# Associating the text length to a variable
text_length = len(text)
print("\nText length:", text_length)

# Multiplying every character with the text_length
ascii_list_multiplied_by_text_length = [value * text_length for value in ascii_list]
print("\nASCII values multiplied by the text length:", ascii_list_multiplied_by_text_length)

# Taking the sum of all list's element
values_sum = sum(ascii_list_multiplied_by_text_length)
print("\nValue of the sum of the chars in the list:", values_sum)

# Building The jwt
jwt_encoded = jwt.encode({"value": str(values_sum)}, SECRET_KEY, algorithm="HS256")
print("\nJWT encoded:",  jwt_encoded, end="\n")

# Transforming the result to hexadecimal
hex_string = jwt_encoded.encode("utf-8").hex()

print("\nHexadecimal representation:", hex_string)

print("\n - Finished -\n")
