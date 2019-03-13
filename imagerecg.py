import cv2

img=cv2.imread('puppy-development.jpg')

while True:

    cv2.imshow('puppy',img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()