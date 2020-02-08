from feet import *

COUNT = 30   # count of pixels for annotation
arr = []


def follow_seed(a, b, pix, count):
    if x == a and y == b and count != 30:
        return arr

    if count==0:
        arr.append([x,y])
        count = 30

    if pixels[a+1,b]==255:
        count -= 1
        follow_seed(a+1, b, pix, count)

    elif pixels[a,b+1] == 255:
        count -= 1
        follow_seed(a, b+1, pix, count)

    elif pixels[a, b-1] == 255:
        count -= 1
        follow_seed(a, b-1, pix, count)

    elif pixels[a-1, b] == 255:
        count -= 1
        follow_seed(a-1,b, pix, count)


arr = follow_seed( x, y, pixels, COUNT)

print(arr.shape)