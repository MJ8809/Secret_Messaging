def caesar_cipher(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            # Shift the character by the specified amount
            shifted_char = chr((ord(char.lower()) - 97 + shift) % 26 + 97)
            # Preserve the case of the original character
            if char.isupper():
                shifted_char = shifted_char.upper()
            cipher_text += shifted_char
        else:
            # Non-alphabetic characters are left unchanged
            cipher_text += char
    return cipher_text


# Get user input for the message and shift value
message = input("Enter the message to encrypt: ")
shift = int(input("Enter the shift value: "))

# Encrypt the message using the Caesar cipher
encrypted_message = caesar_cipher(message, shift)
print("Encrypted message:", encrypted_message)

# Decrypt the message using the same shift value
decrypted_message = caesar_cipher(encrypted_message, -shift)
print("Decrypted message:", decrypted_message)