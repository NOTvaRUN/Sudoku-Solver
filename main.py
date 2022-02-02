import cv2
from PIL import Image, ImageOps
import pytesseract
import solver
path = 'sudoku.jpeg'
flag = 1
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\varun\.conda\envs\tesseract\Library\bin\tesseract.exe'

# img = cv2.imread("sudoku.jpeg")
img = cv2.imread("easy.jpg")

# imgCanny = cv2.Canny(img, 150, 200)
# cv2.imshow('Canny Image', imgCanny)
# cv2.waitKey(0)

array = []
ex = 9
why = 9

adderX = 0
adderY = 0

incrementX = 58
incrementY = 58
# incrementX = 55
# incrementY = 53
startingX = 16
startingY = 232

def cropper(x_ray, y_axis):
    img2 = img.copy()
    x = x_ray
    y = y_axis
    w = 45
    h = 49
    rect = cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cropped = img2[y:y + h, x:x + w]
    imgCanny = cv2.Canny(cropped, 150, 200)
    text = pytesseract.image_to_string(cropped, config='--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789')
    # print(len(text))
    # print(text)
    t = text.strip()
    # print(t)
    # cv2.imshow('Canny Image', img2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    if t:
        # print(t)
        return int(t)
    else:
        # print(0)
        return 0

    # return 0

mother = []


for whe in range(why):
    children = []
    img2 = img.copy()
    if whe == 0:
        adderY = startingY
    else:
        adderY += incrementY
    for exe in range(ex):
        if exe == 0:
            adderX = startingX
        else:
            adderX += incrementX

        children.append(cropper(adderX, adderY))
    mother.append(children)

print(mother)
# mother = [[0, 8, 2, 0, 5, 0, 0, 0, 0], [0, 0, 3, 2, 0, 0, 0, 0, 4], [0, 0, 0, 8, 0, 0, 0, 0, 0], [9, 0, 0, 0, 1, 6, 0, 0, 0], [4, 0, 0, 0, 0, 0, 0, 3, 0], [0, 5, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 9, 0, 5, 4, 0, 0], [0, 0, 0, 0, 0, 0, 2, 0, 3], [0, 0, 0, 0, 0, 7, 5, 0, 0]]
mother = [[0, 0, 0, 9, 6, 0, 5, 0, 4], [0, 2, 0, 1, 0, 0, 0, 6, 0], [5, 0, 0, 0, 0, 0, 8, 0, 9], [0, 3, 2, 0, 0, 0, 0, 5, 1], [1, 9, 6, 7, 5, 3, 0, 0, 2], [0, 0, 5, 0, 0, 0, 0, 9, 0], [9, 8, 4, 5, 0, 1, 0, 0, 6], [2, 0, 0, 0, 0, 9, 1, 0, 0], [0, 0, 0, 8, 2, 7, 9, 0, 0]]
solver.solve_sudoku(mother)
# solver.executer(mother)
# cv2.imshow('Canny Image', img2)
# cv2.waitKey(0)

# cropper(15, 290)

        # cropper(incrementX, incrementY)
