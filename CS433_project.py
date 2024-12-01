#CS433 project

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

def encrypt_to_morse(text):
    encrypted_text = ''
    for char in text.upper():  # Convert text to uppercase to match the dictionary
        if char != ' ':
            encrypted_text += MORSE_CODE_DICT.get(char, '') + ' '
        else:
            encrypted_text += '  '  # Add two spaces between words
    return encrypted_text


def decrypt_from_morse(morse_code):
    morse_code += ' '  # Add a space at the end to recognize the last Morse code character
    plain_text = ''
    morse_char = ''
    for symbol in morse_code:
        if symbol != ' ':
            morse_char += symbol  # Accumulate Morse symbols for a character
        else:
            if morse_char:  # If a Morse character is complete
                plain_text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morse_char)]
                morse_char = ''
            else:
                plain_text += ' '  # Add a space between words
    return plain_text


def encrypt_to_atbash(text_char):
    # Check if the character is an alphabet letter
    if text_char.isalpha():
        # Determine whether the letter is lowercase or uppercase
        first_alpha_letter = 'a'  
        if text_char.isupper():
            first_alpha_letter = 'A'  
        
        # Calculate the original position of the letter in the alphabet
        old_char_position = ord(text_char) - ord(first_alpha_letter)
        
        # Reflect the position to calculate the new position
        new_char_position = -(old_char_position + 1) % 26
        
        # Convert the new position back to a character and return it
        return chr(new_char_position + ord(first_alpha_letter))    
    # If the character is not a letter return it 
    return text_char


def encrypt_decrypt(text):
    new_text = ''  # Initialize an empty string to hold the result
    for char in text:
        # Encrypt or decrypt each character using the Atbash cipher
        new_text += encrypt_to_atbash(char)
    return new_text  # Return the fully encrypted or decrypted text



def main():
    # Loop until user enters a valid choice for encryption algorithm
    while True:
        print("Choose an encryption algorithm:")
        print("Enter 1 for Morse Code")
        print("Enter 2 for Atbash Cipher")
        choice = input("Enter 1 or 2: ")

        if choice == '1' or choice == '2':
            break  # Valid input, exit the loop
        else:
            print("Error: Invalid choice. Please enter 1 or 2.")

    # Loop until user enters a valid mode (encode or decode)
    while True:
        if choice == '1':
            print("Morse Code algorithm selected.")
            text = input("Enter TEXT to encode/decode: ")
            mode = input("Enter 'encode' or 'decode': ").lower()
            if mode == 'encode':
                print("Plain text: ", text)
                print("Encoded Morse code:", encrypt_to_morse(text))
                break
            elif mode == 'decode':
                print("Cipher text: ", text)
                print("Decoded Morse code:", decrypt_from_morse(text))
                break
            else:
                print("Invalid mode. Please choose 'encode' or 'decode'.")
        elif choice == '2':
            print("Atbash Cipher algorithm selected.")
            text = input("Enter TEXT to encode/decode: ")
            mode = input("Enter 'encode' or 'decode': ").lower()
            if mode == 'encode':
                print("Plain text: ", text)
                print("Encoded Atbash text:", encrypt_decrypt(text))
                break
            elif mode == 'decode':
                print("Cipher text: ", text)
                print("Decoded Atbash text:", encrypt_decrypt(text))
                break
            else:
                print("Invalid mode. Please choose 'encode' or 'decode'.")


if __name__== "__main__":
    main()