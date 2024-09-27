from PIL import Image
import numpy as np

def text_to_bin(text):
    ''' convert text to binary
    '''
    return ''.join(format(ord(i), '08b') for i in text)

def embed_text(image_path, text, output_path):
    ''' embed text into an image
    '''
    # open image
    image = Image.open(image_path)
    pixels = np.array(image)

    # convert text to binary
    binary_text = text_to_bin(text) + '1111111111111110' # 16 bit terminator
    
    # flatten pixel array and modify it
    flat_pixels = pixels.flatten()
    for i in range(len(binary_text)):
        flat_pixels[i] = (flat_pixels[i] & ~1) | int(binary_text[i])

    # reshape the array and save the modified image
    modified_pixels = flat.pixels.reshape(pixels.shape)
    modified_image = Image.fromarray(modified.pixels.astype(np.uint8))
    modified_image.save(output_path)
    
embed_text('jerry.png', 'cat', 'secret_jerry.png')
