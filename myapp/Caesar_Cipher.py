def caesar_cipher(text, shift):
    """
    Encrypts a string using the Caesar cipher.

    Parameters:
        text (str): The string to encrypt.
        shift (int): The number of positions to shift the letters.

    Returns:
        str: The encrypted string.
    """
    result = ""

    # Loop through each character in the text
    for i in range(len(text)):
        char = text[i]

        # If the character is a letter, shift it by the specified amount
        if char.isalpha():
            # Get the ASCII code for the character
            code = ord(char)

            # Shift the code by the specified amount
            shifted_code = code + shift

            # If the shifted code is outside the range of A-Z or a-z, wrap it around
            if char.isupper():
                if shifted_code > ord('Z'):
                    shifted_code -= 26
                elif shifted_code < ord('A'):
                    shifted_code += 26
            elif char.islower():
                if shifted_code > ord('z'):
                    shifted_code -= 26
                elif shifted_code < ord('a'):
                    shifted_code += 26

            # Convert the shifted code back to a character and add it to the result
            result += chr(shifted_code)
        else:
            # If the character is not a letter, leave it unchanged
            result += char

    return result
