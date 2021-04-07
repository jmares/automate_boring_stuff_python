# Resizes all images in current working directory to fit in a 
# 300x300 square, and adds catlogo.png to the lower-right corner

import os
from PIL import Image
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'
logo_orig = Image.open(LOGO_FILENAME)
logo_img = logo_orig.resize((81, 77))
logo_width, logo_height = logo_img.size

os.makedirs('with_logo', exist_ok=True)

# Loop over files in the working directory
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue
    img = Image.open(filename)
    width, height = img.size

    # check if image needs to be resized
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # calculate the new width and height to resize to
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        
        # resize image
        print('Resizing %s ...' % (filename))
        img = img.resize((width, height))

        # add the logo
        print('Adding logo to %s ...' % (filename))
        img.paste(logo_img, (width - logo_width, height - logo_height), logo_img)
        # save changes
        img.save(os.path.join('with_logo', filename))