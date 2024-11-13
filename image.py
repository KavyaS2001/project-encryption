from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    with Image.open(image_path) as img:
        print(f"Image opened: {image_path}")
        img_array = np.array(img)
        print(f"Image array shape: {img_array.shape}")
        key_stream = np.random.RandomState(key).randint(0, 256, img_array.shape, dtype=np.uint8)
        encrypted_array = np.bitwise_xor(img_array, key_stream)
        encrypted_img = Image.fromarray(encrypted_array)
        return encrypted_img

def decrypt_image(encrypted_img, key):
    encrypted_array = np.array(encrypted_img)
    print(f"Encrypted array shape: {encrypted_array.shape}")
    key_stream = np.random.RandomState(key).randint(0, 256, encrypted_array.shape, dtype=np.uint8)
    decrypted_array = np.bitwise_xor(encrypted_array, key_stream)
    decrypted_img = Image.fromarray(decrypted_array)
    return decrypted_img


image_path = 'img.jpg'
encryption_key = 12345  


encrypted_image = encrypt_image(image_path, encryption_key)
if encrypted_image:
    encrypted_image.save('encrypted_image.png')  
    print("Encrypted image saved as 'encrypted_image.png'")


if encrypted_image:
    decrypted_image = decrypt_image(encrypted_image, encryption_key)
    if decrypted_image:
        decrypted_image.save('decrypted_image.png') 
        print("Decrypted image saved as 'decrypted_image.png'")

print("Encryption and decryption completed successfully.")
