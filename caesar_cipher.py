def caesar_encrypt(text, shift):
    """
    Encrypts text using Caesar Cipher algorithm.
    
    Args:
        text (str): The message to encrypt
        shift (int): The number of positions to shift each letter
    
    Returns:
        str: The encrypted message
    """
    result = ""
    
    for char in text:
        if char.isupper():
            # Shift uppercase letters
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            # Shift lowercase letters
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result


def caesar_decrypt(text, shift):
    """
    Decrypts text using Caesar Cipher algorithm.
    
    Args:
        text (str): The message to decrypt
        shift (int): The number of positions that were used to shift each letter
    
    Returns:
        str: The decrypted message
    """
    # Decryption is just encryption with negative shift
    return caesar_encrypt(text, -shift)


def main():
    """
    Main function to run the Caesar Cipher program.
    """
    print("=" * 50)
    print("       CAESAR CIPHER - ENCRYPTION & DECRYPTION")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '3':
            print("\nThank you for using Caesar Cipher!")
            break
        
        if choice not in ['1', '2']:
            print("\nInvalid choice! Please enter 1, 2, or 3.")
            continue
        
        # Get user input
        message = input("\nEnter your message: ")
        
        try:
            shift = int(input("Enter shift value (integer): "))
        except ValueError:
            print("\nError: Shift value must be an integer!")
            continue
        
        # Perform encryption or decryption
        if choice == '1':
            encrypted = caesar_encrypt(message, shift)
            print(f"\nOriginal Message: {message}")
            print(f"Shift Value: {shift}")
            print(f"Encrypted Message: {encrypted}")
        else:
            decrypted = caesar_decrypt(message, shift)
            print(f"\nEncrypted Message: {message}")
            print(f"Shift Value: {shift}")
            print(f"Decrypted Message: {decrypted}")

1
if __name__ == "__main__":
    main()
