
# Program Used to Encrypt And Decrypt The Given Text Using Caesar Cipher Technique.

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


plain_text = input("Enter The Text : ")
shift = int(input("enter the shift value : "))

encrypted_text = caesar_encrypt(plain_text, shift)
print("Encrypted Text:" ,encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Decrypted Text:" ,decrypted_text)