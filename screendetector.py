import time
from PIL import ImageGrab, Image

# todo find out the width of a cell and just make it so we only need the top of the game window and get the rest of the
# cells using the size of a cell and print what you see to console

# region Screenshot
cellSize = 36
gridWid = 10
gridHei = 20
startX = 398
startY = 261
endX = (cellSize * gridWid) + startX
endY = (cellSize * gridHei) + startY
speed = 1  # speed at which images are taken in seconds


# endregion


def takeSs():
    ss_region = (startX, startY, endX, endY)  # this will be pain
    ss_img = ImageGrab.grab(ss_region).convert("L")
    ss_img.save("screenshot.jpg")
    return ss_img


def main():
    while True:
        img = takeSs()
        #img = loadImg()
        pixelData = getPixels(img)
        time.sleep(speed)


def loadImg():
    img = Image.open("screenshot.jpg")
    return img


# gets the positions of the pieces in a given image
def getPixels(img):
    pixelData = ""
    test = ""
    for y in range(gridHei):
        for x in range(gridWid):
            pixel = img.getpixel(((cellSize * x) + cellSize / 2, (cellSize * y) + cellSize / 2))
            test += str(pixel) + ":"
            if pixel != 0:
                pixelData += "0"
            else:
                pixelData += "."
        pixelData += "\n"
        test += "\n"
    print(pixelData)
    return pixelData


if __name__ == '__main__':
    main()
