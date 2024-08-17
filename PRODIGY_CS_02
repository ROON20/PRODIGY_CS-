from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    
    image = Image.open(image_path)
    pixels = np.array(image)
    encrypted_pixels = (pixels + key) % 256  
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    return encrypted_image

def decrypt_image(image_path, key):
    
    image = Image.open(image_path)
    pixels = np.array(image)
    decrypted_pixels = (pixels - key) % 256  
    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
    return decrypted_image

def save_image(image, output_path):
   
    valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp')
    if not output_path.lower().endswith(valid_extensions):
        raise ValueError(f'Unsupported file format. Please use one of {valid_extensions}.')
    image.save(output_path)

def process_image():
    
    print("Choose an option:")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    
    choice = input("Enter your choice (1 or 2): ")
    key = int(input('Enter the encryption/decryption key (integer): '))

    if choice == '1':
        image_path = input('Enter the path to the image you want to encrypt: ')
        encrypted_image_path = input('Enter the path to save the encrypted image (with .png, .jpg, .jpeg, or .bmp extension): ')

        # Encrypt image
        encrypted_image = encrypt_image(image_path, key)
        save_image(encrypted_image, encrypted_image_path)
        print(f'Image encrypted and saved to {encrypted_image_path}')

    elif choice == '2':
        encrypted_image_path = input('Enter the path to the image you want to decrypt: ')
        decrypted_image_path = input('Enter the path to save the decrypted image (with .png, .jpg, .jpeg, or .bmp extension): ')

        # Decrypt image
        decrypted_image = decrypt_image(encrypted_image_path, key)
        save_image(decrypted_image, decrypted_image_path)
        print(f'Image decrypted and saved to {decrypted_image_path}')

    else:
        print('Invalid choice. Please select 1 or 2.')

if __name__ == '__main__':
    process_image()
