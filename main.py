img = Image.open('ZZZENDOFFILE.png')

Mirror_Image=img.transpose(Image.FLIP_LEFT_RIGHT)

Mirror_Image.save(r'mirrortest.png')

Image.open('mirrortest.png') #mirrored Image
