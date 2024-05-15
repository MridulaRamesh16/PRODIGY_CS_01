def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    text = input("Enter any preffered text: ")
    shift = int(input("Enter the shift value: "))
    
    encrypted_text = encrypt(text, shift)
    print("Encrypted:", encrypted_text)
    
    decrypted_text = decrypt(encrypted_text, shift)
    print("Decrypted:", decrypted_text)

if __name__ == "__main__":
    main()
