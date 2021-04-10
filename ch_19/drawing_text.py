from PIL import Image, ImageDraw, ImageFont
import os
img = Image.new('RGBA', (200,200), 'white')
draw = ImageDraw.Draw(img)
draw.text((20,50), 'Hello', fill='red')
fonts = '/System/Library/Fonts/Supplemental' # macOS
font = ImageFont.truetype(os.path.join(fonts, 'Silom.ttf'), 40)
draw.text((50,120), 'Howdy', fill='blue', font=font)
img.save('text.png')
