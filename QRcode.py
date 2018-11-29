"""
Make and Decode a QR code
"""

import qrcode
from pyzbar.pyzbar import decode
import cv2 as cv
import numpy as np

image = qrcode.make('This is the data of the QR Code')
image.save('test.png')
result = decode(cv.imread('test.png'))
# print(result[0][3])
print(result)

def image_detect():
    src = cv.imread("D:/images/wechat_id.jpg")
    # result, code_image = qr_detector.detect(src)
    # text_content = decode(code_image)
    text_content = decode(src)
    if text_content is not None:
        print("content : %s"% text_content[0][0])
        cv.imshow("input", src)
        
def video_detect():
    capture = cv.VideoCapture(0)
    height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
    width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
    out = cv.VideoWriter("D:/qrcode_demo.mp4", cv.VideoWriter_fourcc('D', 'I', 'V', 'X'), 15,
                         (np.int(width), np.int(height)), True)
    while True:
        ret, frame = capture.read()
        if ret is True:
            frame = cv.flip(frame, 1)
            cv.imshow("frame", frame)
            # result, code_image = qr_detector.detect(frame)
            #if code_image is not None:
                #text = decode(code_image)
            if frame is not None:
                text = decode(frame)
                if len(text) > 0:
                    cv.putText(result, text[0][0].decode("utf-8"), (20, 100), cv.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2, 8)
                    cv.imwrite("D:/result.png", result)
                    print(text[0][0].decode("utf-8"))
            out.write(result)
            cv.imshow("result", result)

            c = cv.waitKey(5)
            if c == 27:
                break
        else:
            break
    cv.waitKey(0)
    cv.destroyAllWindows()
