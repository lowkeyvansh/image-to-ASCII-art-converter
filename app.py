from PIL import Image

def image_to_ascii(image_path, output_width=100):
    img = Image.open(image_path)
    width, height = img.size
    aspect_ratio = height/width
    new_height = int(output_width * aspect_ratio)
    img = img.resize((output_width, new_height))
    img = img.convert('L')
    pixels = img.getdata()
    chars = "".join(["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."][pixel//25] for pixel in pixels)
    ascii_image = "\n".join([chars[index:index+output_width] for index in range(0, len(chars), output_width)])
    return ascii_image

ascii_art = image_to_ascii("path/to/image.jpg")
print(ascii_art)
