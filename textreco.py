import numpy
import cv2

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract



cap = cv2.VideoCapture(0)

while True:
    ret, image_np = cap.read()

    cv2.imshow('Testing', cv2.resize(image_np, (800, 600)))
    print (pytesseract.image_to_string(image_np))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
