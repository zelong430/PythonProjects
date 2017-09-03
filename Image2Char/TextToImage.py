import PIL
import PIL.Image
import PIL.ImageFont
import PIL.ImageOps
import PIL.ImageDraw

PIXEL_ON = 0  # PIL color to use for "on"
PIXEL_OFF = 255

def text_image(text, width, height, font_size, output):
    grayscale = 'L'

    text = text.split("\n")
    # choose a font (you can see more detail in my library on github)
    font_path = 'cour.ttf'
    try:
        font = PIL.ImageFont.truetype(font_path, size=font_size)
    except IOError:
        font = PIL.ImageFont.load_default()
        print('Could not use chosen font. Using default.')

    image = PIL.Image.new(grayscale, (width * font_size * 2, height * font_size *2), color=PIXEL_OFF)
    draw = PIL.ImageDraw.Draw(image)

    # draw each line of text
    line_spacing = font_size//1.3 # reduced spacing seems better

    vertical_position = 3
    for line in text:
        draw.text((0, vertical_position),
                  line, fill=PIXEL_ON, font=font)
        vertical_position += line_spacing
    # crop the text
    c_box = PIL.ImageOps.invert(image).getbbox()
    image = image.crop(c_box)
    image.save(output+".jpg")
