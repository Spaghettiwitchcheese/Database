


#this one takes the text from a file and encrypts it with a caesar cipher
#it writes the encrypted text to a new file
def cesar_cypher(salat, key):
    result = ""
    for char in salat:
        if char.isalpha():  # Check if the character is a letter
            base = 65 if char.isupper() else 97
            result += chr((ord(char) + key - base) % 26 + base)
        elif char.isdigit():  # Check if the character is a digit
            result += str((int(char) + key) % 10)  # Apply the Caesar cipher for digits
        else:
            result += char  # Keep non-alphanumeric characters as they are
    return result

input_file = r"C:\Users\lukas.vachtl023.SKOLAVDF\Caffeine\Python\prelude.txt"  # Replace with the actual input file name
output_file = r"C:\Users\lukas.vachtl023.SKOLAVDF\Caffeine\Python\Cipher.txt"  # Replace with the desired output file name
key = 3  # Replace with the desired key for the Caesar cipher

with open(input_file, 'r') as file:
    data = file.read()
    ciphered_text = cesar_cypher(data, key)

with open(output_file, 'w') as file:
    file.write(ciphered_text)