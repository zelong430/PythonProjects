from PIL import Image
import argparse
import string
from TextToImage import text_image

# Parse Commandline Argument
parser = argparse.ArgumentParser(description='Convert an image into an new image consist of ASCII chars')

parser.add_argument('file',
                    help='Path to the input image file.')
parser.add_argument('--output','-o',
                    help='Path to the output txt file.')
parser.add_argument('--width',
                    type=int,
                    help='Width of the resulting image',
                    default=80)
parser.add_argument('--height',
                    type = int,
                    help='Height of the resulting image',
                    default = 80)

# Read in argument
args = parser.parse_args()
IMG = args.file
WIDTH =args.width
HEIGHT = args.height
OUTPUT = args.output

# Define list of ascii chars used to create a new image
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
def get_char(r,g,b,alpha = 256):
    """
    Convert the RGB value of a pixel to a character in the ascii character list

    :param r: the r value of the pixel
    :param g: the g value of th pixel
    :param b: the b value of the pixel
    :param alpha: the alpha value of the pixel
    :return: a character representing the original input RGB
    """
    if alpha == 0 or (r == g == b == 255):
        return '.'
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]



def main():

    # Read in
    im = Image.open(IMG)
    im = im.convert("RGBA")
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    result = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            pixel = im.getpixel((j, i))
            r,g,b,alpha = pixel
            char = get_char(r,g,b,alpha)
            result += char
        result += "\n"

    out_file = OUTPUT if OUTPUT is not None else "output"
    # if OUTPUT:
    with open(out_file + '.txt', "w") as f:
        f.write(result)
    text_image(result, WIDTH, HEIGHT, 10, out_file)

if __name__ == "__main__":
    main()