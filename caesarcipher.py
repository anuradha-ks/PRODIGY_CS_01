def caesar_cipher(msg, shift, op='encrypt'):
    result = ""
    
    # Adjust the shift for decryption
    if op == 'decrypt':
        shift = -shift
    
    for char in msg:
        if char.isalpha():
            # Handle uppercase and lowercase letters separately
            a_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - a_offset + shift) % 26 + a_offset)
        else:
            # Non-alphabetic characters remain unchanged
            result += char
            
    return result

def main():
    while True:
        print("\nCaesar Cipher")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            msg = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            ecmsg = caesar_cipher(msg, shift, op='encrypt')
            print(f"Encrypted message: {ecmsg}")
        
        elif choice == '2':
            msg = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            dmsg = caesar_cipher(msg, shift, op='decrypt')
            print(f"Decrypted message: {dmsg}")
        
        elif choice == '3':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
