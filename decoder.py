from PIL import Image
import sys
import numpy as np

im =Image.open(sys.argv[1])

pix = np.array(im)

def is_black(pixel):
    if np.any(pixel != 0):
        return False

    return True

def is_white(pixel):
    if np.any(pixel != 255):
        return False

    return True

def is_green(pixel):
    if pixel == (178,219,55):
        print 't'
        return True
    return False



binary = ''

count = 1
print pix[0][0]

for i in range(len(pix)):
    for j in range(len(pix[i])):

        # if is_black(pix[i][j]):
        #     binary = binary + '0'
        # if is_white(pix[i][j]):
        #     binary = binary + '1'
        
        
        # if count < 8:
        #     count = count + 1
        # else:
        #     count = 1
        #     binary = binary + ' '

        if is_green(pix[i][j]):
            pix[i][j] = [178,219,55,255]
        else:
            pix[i][j] = [0,0,0,255]


im2 = Image.fromarray(pix)
im2.save("result.png")