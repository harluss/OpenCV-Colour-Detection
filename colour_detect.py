import cv2
import numpy as np

# Get the camera
device = cv2.VideoCapture(0)

# Dummy function req by trackbars
def dummyFunction(x):
    pass

# Window with HSV trackbars (default values set to Red-ish)
cv2.namedWindow("HSV Values")
cv2.createTrackbar("Low H", "HSV Values", 160, 180, dummyFunction)
cv2.createTrackbar("Low S", "HSV Values", 155, 255, dummyFunction)
cv2.createTrackbar("Low V", "HSV Values", 85, 255, dummyFunction)
cv2.createTrackbar("High H", "HSV Values", 180, 180, dummyFunction)
cv2.createTrackbar("High S", "HSV Values", 255, 255, dummyFunction)
cv2.createTrackbar("High V", "HSV Values", 255, 255, dummyFunction)

while True:
    _, frame = device.read()
    # Change the frame from RGB to HSV colour space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_h = cv2.getTrackbarPos("Low H", "HSV Values")
    low_s = cv2.getTrackbarPos("Low S", "HSV Values")
    low_v = cv2.getTrackbarPos("Low V", "HSV Values")
    high_h = cv2.getTrackbarPos("High H", "HSV Values")
    high_s = cv2.getTrackbarPos("High S", "HSV Values")
    high_v = cv2.getTrackbarPos("High V", "HSV Values")

    lower_range = np.array([low_h, low_s, low_v])
    upper_range = np.array([high_h, high_s, high_h])

    # Puts mask over the frame isolating select range of colours
    mask = cv2.inRange(hsv, lower_range, upper_range)

    # Remove noise
    maskMedian = cv2.medianBlur(mask, 15)

    # Draw bounding box
    conts, _ = cv2.findContours(
        maskMedian, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Draw contours
    # cv2.drawContours(frame, conts, -1, (255, 0, 0), 3)

    for cont in conts:
        x, y, w, h = cv2.boundingRect(cont)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Show without noise reduction
    cv2.imshow("Masked", mask)
    # Show with noise reduced
    cv2.imshow("maskMedian", maskMedian)
    # Show original frame
    cv2.imshow("Frame", frame)

    # Show with colour mask (isolating selected colour range)
    # result = cv2.bitwise_and(frame, frame, mask=maskMedian)
    # cv2.imshow("Result", result)

    # Press ESC to quit
    if cv2.waitKey(1) == 27:
        break

device.release()
cv2.destroyAllWindows()