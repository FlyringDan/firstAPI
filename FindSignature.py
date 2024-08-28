import cv2
import pytesseract

RED = (0, 0, 255)
BLUE = (255, 0, 0)


def find_signature(path_to_dec_image):
    global client_sig, operator_sig
    img = cv2.imread(path_to_dec_image)
    data = pytesseract.image_to_data(path_to_dec_image, lang='rus')
    # print(data)
    x, y, w, h = 0, 0, 0, 0
    for i, el in enumerate(data.splitlines()):
        if i == 0:
            continue

        # find coordinates of signature
        el = el.split()
        if el[-1] == 'Новый':
            x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
            x = x
            y = y + h
            w = x + w * 7
            h = y + 40
            client_sig = presence_of_signature(x, y, w, h, img)
            #cv2.rectangle(img, (x, y), (w, h), RED, 1)
        if el[-1] == "Представитель":
            x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
            x = x
            y = y + h
            w = x + w * 3
            h = y + 40
            operator_sig = presence_of_signature(x, y, w, h, img)
            #cv2.rectangle(img, (x, y), (w, h), BLUE, 1)

    # draw rec to see the signature
    #cv2.imshow("result", img)
    #cv2.waitKey(0)

    return operator_sig, client_sig


def presence_of_signature(x, y, w, h, img):
    signature_img = img[y:h, x:w]
    white = 0
    not_white = 0
    for i in range(signature_img.shape[0]):
        for j in range(signature_img.shape[1]):
            b, g, r = signature_img[i, j]
            if (181 <= b <= 255) and (181 <= g <= 255) and (181 <= r <= 255):
                white += 1
            else:
                not_white += 1
    percent_of_line = 1103 / (8977 + 1103) * 100
    if not_white / (white + not_white) * 100 > percent_of_line:
        return True
    else:
        return False
