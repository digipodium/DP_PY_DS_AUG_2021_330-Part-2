import cv2

cap = cv2.VideoCapture(0)
while True:
    state, frame = cap.read()
    if state:
        out = cv2.Canny(frame,100,200)
        cv2.imshow('original',frame)
        cv2.imshow('edges',out)
        if cv2.waitKey(1) == 27:
            break
cap.release()
cv2.destroyAllWindows()