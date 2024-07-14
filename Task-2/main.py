# Program Used To Encrypt and Decrypt The Image Using Pixel Manipulation.

from PIL import Image 

import numpy as np

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    
    img_array = np.array(img)
    

    encrypted_array = (img_array + key) % 255
    
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save('encrypted_image.png')
    print("Image encrypted and saved as encrypted_image.png")

def decrypt_image(encrypted_image_path, key):

    encrypted_img = Image.open(encrypted_image_path)

    encrypted_array = np.array(encrypted_img)
    
    decrypted_array = ( encrypted_array-key ) % 255
    
 
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_img.save('decrypted_image.png')
    print("Image decrypted and saved as decrypted_image.png")

key = int(input("Enter The Key Value : "))
encrypt_image('sampleimg.png', key)
decrypt_image('encrypted_image.png', key)